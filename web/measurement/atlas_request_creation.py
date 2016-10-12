from datetime import datetime
from secret_file import *
from .models import Target
import time
import datetime
from ripe.atlas.cousteau import (
  Ping,
  Traceroute,
  AtlasSource,
  AtlasCreateRequest
)



def atlas_api_call():
    #ATLAS_API_KEY = ""
    q=Target.objects.all().last()

    if (q.specification.one_off is True):
        traceroute = Traceroute(
            af=4,
            target=str(q.target),
            description=str(q.description),
            protocol=str(q.specification.protocol),

        )
    else:
        traceroute = Traceroute(
            af=4,
            target=str(q.target),
            description=str(q.description),
            protocol=str(q.specification.protocol),
            interval=int(q.specification.interval),
        )


    source=[]
    for i in range(0,q.probes.all().count()):
        l=q.probes.all()[i]
        #new[i]='source'+i
        source.append(AtlasSource(
            type="country",
            value=str(l.country),
            requested=int(l.number),
            tags={"exclude": ["system-anchor"]}
        ))

    if (q.specification.one_off is True):
        atlas_request = AtlasCreateRequest(
            start_time=int(time.time()),
            key=ATLAS_API_KEY,
            measurements=[traceroute],
            sources=source,
            is_oneoff=q.specification.one_off
        )
    else:
        atlas_request = AtlasCreateRequest(
            start_time=int(time.time()),
            stop_time=int(time.mktime(q.specification.stop_time.timetuple())),
            key = ATLAS_API_KEY,
            measurements = [traceroute],
            sources = source,
            is_oneoff = q.specification.one_off
        )





    (is_success, response) = atlas_request.create()
    print response
    return response


