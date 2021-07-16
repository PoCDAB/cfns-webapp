from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from ..forms import GeoviewForm

# Retrieve (filterd) AIS dataset from the database for the GIS
@login_required(login_url='/login/')
def geomapView(request):
    if request.method == 'POST':
        form = GeoviewForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
          
            return render(request, 'geomap.html', {'form': form})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = GeoviewForm()
    return render(request, 'geomap.html', {'form': form})
