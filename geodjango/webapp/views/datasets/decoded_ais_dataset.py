from django.core.serializers import serialize
from django.http import HttpResponse
from ...models import aisDecoded

# Retrieve AIS dataset from the database (for the GIS/geomap)
def decoded_ais_dataset(request):
    decoded_ais_messages = serialize('geojson', aisDecoded.objects.all())
    return HttpResponse(decoded_ais_messages, content_type='json')