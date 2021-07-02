from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from ..forms import SendDABForm
from ..models import DAB

@login_required(login_url='/login/')
def send_dab_view(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SendDABForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            #DAB.objects.create(message=request.POST["message"], message_type=request.POST["messagetype"], ship_id=request.POST["ship_id"])
            
            # HIERR

            return  render(request, 'send_dab.html', {'form': form, 'info_msg': 'DAB+ has been send!'})
        else:
            return  render(request, 'send_dab.html', {'form': form, 'info_msg': 'Sometime went wrong! Please try again'})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = SendDABForm()

    return render(request, 'send_dab.html', {'form': form})