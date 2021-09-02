from django.shortcuts import render
from django.template import RequestContext

# returns the 404 'not found' template
def handler404(request, *args, **argv):
    response = render(request, '404.html', {})
    response.status_code = 404
    return response

# returns the 500 'internal server error' template
def handler500(request, *args, **argv):
    response = render(request, '500.html', {})
    response.status_code = 500
    return response