from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from ..forms import SelectDABType, SendDABForm_point, SendDABForm_circle, SendDABForm_polygon
from ..models import dabModel
from ..code import createGeoNotification

from django.conf import settings

@login_required(login_url='/login/')
def send_dab_view(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        startform = SelectDABType(request.POST)

        if "messagetype" in request.POST or  ("message" in request.POST and "ship_id" in request.POST):
            messagetype = int(request.POST["messagetype"])

            form = None
            if messagetype == 1:
                form = SendDABForm_point(request.POST)
            if messagetype == 2:
                form = SendDABForm_circle(request.POST)
            if messagetype == 3:
                form = SendDABForm_polygon(request.POST)
            
            # check whether first form is valid:
            if startform.is_valid():
                # check whether it's valid:
                if form and form.is_valid():
                    dabmessage = dabModel.objects.create(message=request.POST["message"], message_type=int(request.POST["messagetype"]), ship_id=request.POST["ship_id"])
                    createGeoNotification(dabmessage, request.POST)

                    return  render(request, 'send_dab.html', {'startform': startform, 'form': form, 'info_msg': 'DAB+ has been send!', 'info_type': 'alert-success'})
                else:
                    if form and ("message" not in request.POST and "ship_id" not in request.POST):
                        return  render(request, 'send_dab.html', {'startform': startform, 'form': form})
                    return  render(request, 'send_dab.html', {'startform': startform, 'form': form, 'info_msg': 'Sometime went wrong! Please try again', 'info_type': 'alert-danger'})
        
    startform = SelectDABType()
    return render(request, 'send_dab.html', {'startform': startform})
