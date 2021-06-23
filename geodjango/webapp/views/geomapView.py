from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.serializers import serialize
from django.http import HttpResponse
from ..models import aisDecoded

from ..forms import GeoviewForm

def geomapView(request):
    if request.method == 'POST':
        form = GeoviewForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
                return render(request, 'name.html', {'form': form})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = GeoviewForm()
    return render(request, 'geomap.html', {'form': form})

def decoded_ais_dataset(request):
    decoded_ais_messages = serialize('geojson', aisDecoded.objects.all())
    return HttpResponse(decoded_ais_messages, content_type='json')
