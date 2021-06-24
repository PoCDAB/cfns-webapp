from django.core.serializers import serialize
from django.http import HttpResponse
from ...models import DAB

# Retrieve DAB dataset from the database (for the GIS/geomap)
def dab_dataset(request):
    dab_messages = serialize('geojson', DAB.objects.all())
    return HttpResponse(dab_messages, content_type='json')