from django.core.serializers import serialize
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from ..models import dabModel

# Retrieve DAB dataset from the database (for the GIS/geomap)
@login_required
def dabDataset(request):
    dab_messages = serialize('geojson', dabModel.objects.all())
    return HttpResponse(dab_messages, content_type='json')