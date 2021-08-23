import json
from django.contrib.gis.geos import Point, Polygon, GEOSGeometry
from ..models import aisDecodedModel, lorawanModel
from ..models import geoMessageModel, geoPointModel, geoCircleModel, geoPolygonModel
from re import search

##
# Function creates GeoData object in database. Switches between different kind of GeoTypes
##
def createGeoData(dabmessage, POSTdata):
    if dabmessage.message_type == 0:
        return geoMessageModel.objects.create(
            dab = dabmessage,
            message = POSTdata['message'],
        )
    elif dabmessage.message_type == 1:
        return geoPointModel.objects.create(
            dab = dabmessage,
            location = POSTdata['point'],
            message = POSTdata['message'],
        )
    elif dabmessage.message_type == 2:
        return geoCircleModel.objects.create(
            dab = dabmessage,
            location = POSTdata['point'],
            radius = POSTdata["radius"],
            message = POSTdata['message'],
        )
    elif dabmessage.message_type == 3:
        return geoPolygonModel.objects.create(
            dab = dabmessage,
            polygon = POSTdata['polygon'],
            message = POSTdata['message'],
        )
    else:
        return None

##
# Function can alter a GeoData object. Add new technologie
##
def alterGeoData(parent, object):
    if type(object) is aisDecodedModel:
        parent.aisDecoded = object
    if type(object) is lorawanModel:
        parent.lorawan = object
    parent.save()
    return parent
