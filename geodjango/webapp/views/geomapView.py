from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def geomapView(request):
    return render(request, 'geomap.html', {'' : ''})