from django.core.serializers import serialize
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from ..models import lorawanModel

# Retrieve AIS dataset from the database (for the GIS/geomap)
@login_required
def lorawanDataset(request):
    objs = lorawanModel.objects.all()
    lorawan_messages = serialize('geojson', objs)
    return HttpResponse(lorawan_messages, content_type='json')