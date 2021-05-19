from django.shortcuts import render

def world_borders_page(request):
    return render(request, 'world_borders.html', {'' : ''})