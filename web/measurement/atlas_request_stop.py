from ripe.atlas.cousteau import AtlasStopRequest
from .models import Target

def atlas_api_stop_call(msm_id_var):
    ATLAS_STOP_API_KEY = "48184dec-6138-46d0-94fe-1b29fe2ea34f"

    atlas_request = AtlasStopRequest(msm_id=msm_id_var, key=ATLAS_STOP_API_KEY)

    (is_success, response) = atlas_request.create()