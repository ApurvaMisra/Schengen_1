from ripe.atlas.cousteau import AtlasStopRequest
from .models import Target
from secret_file import *

def atlas_api_stop_call(msm_id_var):
    #ATLAS_STOP_API_KEY = ""

    atlas_request = AtlasStopRequest(msm_id=msm_id_var, key=ATLAS_STOP_API_KEY)

    (is_success, response) = atlas_request.create()