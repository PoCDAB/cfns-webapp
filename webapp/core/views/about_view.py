from django.shortcuts import render

# returns the about us template
def aboutView(request):
    return render(request, 'about.html')