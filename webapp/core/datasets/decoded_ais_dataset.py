from django.core.serializers import serialize
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from ..models import aisDecodedModel

# Retrieve AIS dataset from the database (for the GIS/geomap)
@login_required
def decodedAisDataset(request):
    objs = aisDecodedModel.objects.all().order_by('mmsi', '-updated_at').distinct('mmsi')
    decoded_ais_messages = serialize('geojson', objs)
    return HttpResponse(decoded_ais_messages, content_type='json')