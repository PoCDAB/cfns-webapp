from django.core.serializers import serialize
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from ...models import DAB

# Retrieve DAB dataset from the database (for the GIS/geomap)
@login_required
def dab_dataset(request):
    dab_messages = serialize('geojson', DAB.objects.all())
    return HttpResponse(dab_messages, content_type='json')