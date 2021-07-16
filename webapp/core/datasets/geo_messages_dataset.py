from django.core.serializers import serialize
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from ..models import geoMessageModel, geoPointModel, geoCircleModel, geoPolygonModel

# Retrieve DAB dataset from the database (for the GIS/geomap)
@login_required
def geoPointDataset(request):
    geo_messages = serialize('geojson', geoPointModel.objects.all())
    return HttpResponse(geo_messages, content_type='json')

@login_required
def geoCircleDataset(request):
    geo_messages = serialize('geojson', geoCircleModel.objects.all())
    return HttpResponse(geo_messages, content_type='json')

@login_required
def geoPolygonDataset(request):
    geo_messages = serialize('geojson', geoPolygonModel.objects.all())
    return HttpResponse(geo_messages, content_type='json')