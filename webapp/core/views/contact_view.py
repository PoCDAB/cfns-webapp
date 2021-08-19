from django.shortcuts import render
from ..forms import contactForm

def contactView(request):
    if request.method == 'POST':
        form = contactForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            return render(request, 'contact.html', {'form': form, 'info_msg': 'Contact form is not connected', 'info_type': 'alert-danger'})
    # if a GET (or any other method) we'll create a blank form
    else:
        form = contactForm()
    return render(request, 'contact.html', {'form': form})