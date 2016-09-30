from __future__ import division

from datetime import datetime
from ripe.atlas.cousteau import AtlasResultsRequest
from ripe.atlas.sagan import TracerouteResult
import geoip2.database
import collections
from django.core.files import File
import json



def atlas_api_result_call(msm_idvar,start_date,stop_date,count):
    kwargs = {
        "msm_id": msm_idvar,
        "start": start_date,
        "stop": stop_date,
    }


    is_success, results = AtlasResultsRequest(**kwargs).create()
    pathlist=[]
    hopslist=[]
    timelist=[]
    IPlistcomp=[]
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
    h=open('countries.txt','w')
    for i in range(0, len(IPlistcomp)):
        try:
            response = reader.country(IPlistcomp[i])
        except:
            h.write("none" + "\n")

        else:
            if response.country.name is None:
                h.write("none" + "\n")
            else:
                new = (response.country.name).encode('ascii', 'ignore')
                h.write(new + "\n")


    h.close()

    with open("countries.txt") as f:
        content = f.readlines()

    f.close()

    content = map(lambda s: s.strip(), content)
    counter = collections.Counter(content)
    sum=0
    for key, value in counter.iteritems():
        sum=sum+value
        counter[key]=[counter[key]]

    for key, value in counter.iteritems():
        var1=(int((counter[key])[0])/sum)*100
        counter[key].append(var1)

    key = "sum"
    counter.setdefault(key, [])
    counter[key].append(sum)

    #key = "loss data"
    #counter.setdefault(key, [])
    #var2=(int((counter["none"])[0])/sum)*100
    #counter[key].append(var2)

    counter1 = collections.OrderedDict(sorted(counter.items()))
    json.dump(counter1, open("countries_stat.txt", 'w'))




    #print hopslist










