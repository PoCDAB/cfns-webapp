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

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import json
from ..models import dabModel, aisDecodedModel, lorawanModel
from ..models import geoPointModel, geoCircleModel, geoPolygonModel

from ..code import alterGeoData

# returns fakeAcknowledgement template
@login_required(login_url='/login/')
def fakeAcknowledgementView(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        if 'dab_id' in request.POST and 'ack_type' in request.POST:
            parent = getParentByDABid(request.POST['dab_id'])
            obj = None
            
            # search for Model with correct dab_id
            if 'ais' in request.POST['ack_type']:
                obj = aisDecodedModel.objects.create()
            elif 'lorawan' in request.POST['ack_type']:
                obj = lorawanModel.objects.create()

            alterGeoData(parent, obj)

    objects = []
    # search for geoModels with coresponding dab_id
    for x in dabModel.objects.all():
        obj = getParentByDABid(x.id)
        if obj:
            objects.append(obj)
    
    return render(request, 'fake_acknowledgement.html', {'all_objects': objects })

# returns the correct model through dab_id
def getParentByDABid(dab_id):
    if geoPointModel.objects.filter(dab=dab_id):
        return geoPointModel.objects.get(dab=dab_id)
    elif geoCircleModel.objects.filter(dab=dab_id):
        return geoCircleModel.objects.get(dab=dab_id)
    elif geoPolygonModel.objects.filter(dab=dab_id):
        return geoPolygonModel.objects.get(dab=dab_id)
