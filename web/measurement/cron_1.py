from django_cron import CronJobBase, Schedule
from __future__ import division

import datetime as DT
from ripe.atlas.cousteau import AtlasResultsRequest
from ripe.atlas.sagan import TracerouteResult
import geoip2.database
import collections
from django.core.files import File
from .models import *
import json


class MyCronJob(CronJobBase):
    RUN_EVERY_MINS = 120 # every 2 hours

    schedule = Schedule(run_every_mins=RUN_EVERY_MINS)
    code = 'my_app.my_cron_job'    # a unique code

    def do(self):
        all_target = Target.objects.all()
        for tar in all_target:
            kwargs = {
                "msm_id": tar.msm_id,
                "start": DT.date.today() - DT.timedelta(days=7),
                "stop": DT.date.today(),
            }

            is_success, results = AtlasResultsRequest(**kwargs).create()
            pathlist = []
            hopslist = []
            timelist = []
            IPlistcomp = []
            if is_success:
                for result in results:
                    parsed_result = TracerouteResult.get(result)
                    pathlist.append(parsed_result.ip_path)
                    hopslist.append(parsed_result.total_hops)
                    timelist.append(parsed_result.end_time)

            for i in range(0, len(pathlist)):
                for k in range(0, hopslist[i]):
                    try:
                        IPlistcomp.append(pathlist[i][k][0])
                    except:
                        IPlistcomp.append("0.0.0.0")

            reader = geoip2.database.Reader("/home/csg/Downloads/GeoLite2-Country.mmdb")
            h = open('countriescron.txt', 'w')
            for i in range(0, len(IPlistcomp)):
                try:
                    response = reader.country(IPlistcomp[i])
                except:
                    h.write("OO" + "\n")

                else:
                    if response.country.name is None:
                        h.write("OO" + "\n")
                    else:
                        new = (response.country.iso_code).encode('ascii', 'ignore')
                        h.write(new + "\n")

            h.close()

            with open("countriescron.txt") as f:
                countrylist = f.readlines()

            f.close()

            countrylist = map(lambda s: s.strip(), countrylist)

            desc = tar.description
            rel = int(filter(str.isdigit, str(desc)))
            desc = desc.replace(" ", "")
            desc = str(desc)
            rel = "Relation" + str(rel)
            m = 0
            for i in range(0, len(hopslist)):
                tar1 = eval(desc)(timestamp=timelist[i])
                tar1.save()
                for k in range(0, hopslist[i]):
                    b = Countries.objects.get(country=countrylist[m])
                    eval(rel).objects.create(traceroutemeasurement_id=int(tar1.id), countries_id=int(b.id))
                    m = m + 1



