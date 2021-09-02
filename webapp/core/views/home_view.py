from django.shortcuts import render

# returns the home template
def homeView(request):
    return render(request, 'index.html')