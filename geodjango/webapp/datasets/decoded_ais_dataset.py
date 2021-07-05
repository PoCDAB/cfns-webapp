from django.core.serializers import serialize
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from ..models import AISDecoded

# Retrieve AIS dataset from the database (for the GIS/geomap)
@login_required
def decoded_ais_dataset(request):
    decoded_ais_messages = serialize('geojson', AISDecoded.objects.all().order_by('mmsi', '-updated_at').distinct('mmsi'))

    return HttpResponse(decoded_ais_messages, content_type='json')