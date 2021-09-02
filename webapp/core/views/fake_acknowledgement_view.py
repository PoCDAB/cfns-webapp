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
