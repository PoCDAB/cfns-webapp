#
# CFNS - Rijkswaterstaat CIV, Delft © 2020 - 2021 <cfns@rws.nl>
#
# Copyright 2020 - 2021 Daniël Geerts <daniel.geerts@rws.nl>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from ..forms import SelectDABType, SendDABForm_message, SendDABForm_point, SendDABForm_circle, SendDABForm_polygon
from ..models import dabModel
from ..code import createGeoData

from django.conf import settings

# returns the sen DAB+ template
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

# returns the correct model through dab_id
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
