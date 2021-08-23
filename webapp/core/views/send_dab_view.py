from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from ..forms import SelectDABType, SendDABForm_message, SendDABForm_point, SendDABForm_circle, SendDABForm_polygon
from ..models import dabModel
from ..code import createGeoData

from django.conf import settings

@login_required(login_url='/login/')
def sendDabView(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        startform = SelectDABType(request.POST)
        if startform.is_valid():
            if "messagetype" in request.POST or ("message" in request.POST and "ship_id" in request.POST):
                messagetype = int(request.POST["messagetype"])
           
                # check whether first form is valid:
                form = getCorrectForm(messagetype, request.POST)

                # check whether it's valid:
                if form and form.is_valid():
                    # create a new DABmessage
                    dabmessage = dabModel.objects.create(message=request.POST["message"], message_type=int(request.POST["messagetype"]), ship_id=request.POST["ship_id"])
                    # create new GEOdata for the GIS view
                    createGeoData(dabmessage, request.POST)
                    # clear form
                    clearedform = getCorrectForm(messagetype)

                    return  render(request, 'send_dab.html', {'startform': startform, 'form': clearedform, 'info_msg': 'DAB+ has been send!', 'info_type': 'alert-success'})
                else:
                    if form and ("message" not in request.POST and "ship_id" not in request.POST):
                        return  render(request, 'send_dab.html', {'startform': startform, 'form': form})
                    return  render(request, 'send_dab.html', {'startform': startform, 'form': form, 'info_msg': 'Sometime went wrong! Please try again', 'info_type': 'alert-danger'})
        
    startform = SelectDABType()
    return render(request, 'send_dab.html', {'startform': startform})


def getCorrectForm(messagetype, postRequest = None):
    if messagetype == 0:
        return SendDABForm_message(postRequest)
    elif messagetype == 1:
        return SendDABForm_point(postRequest)
    elif messagetype == 2:
        return SendDABForm_circle(postRequest)
    elif messagetype == 3:
        return SendDABForm_polygon(postRequest)
    else:
        return SendDABForm_message()