from django.shortcuts import render

# Create your views here.

def home_page(request):
    return render(request, 'index.html', {'' : ''})

def world_borders_page(request):
    return render(request, 'world_borders.html', {'' : ''})

def api_page(request):
    return render(request, '', {'' : ''})
