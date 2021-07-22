import json
from django.contrib.gis.geos import Point, Polygon, GEOSGeometry
from ..models import geoPointModel, geoCircleModel, geoPolygonModel
from re import search

##
# Function creates GeoData object in database. Switches between different kind of GeoTypes
##
def createGeoData(dabmessage, POSTdata):
    if dabmessage.message_type == 1:
        return geoPointModel.objects.create(
            dab = dabmessage,
            message = dabmessage.message,
            location = POSTdata['point'],
        )
    elif dabmessage.message_type == 2:
        return geoCircleModel.objects.create(
            dab = dabmessage,
            message = dabmessage.message,
            location = POSTdata['point'],
            radius = POSTdata["radius"],
        )
    elif dabmessage.message_type == 3:
        return geoPolygonModel.objects.create(
            dab = dabmessage,
            message = dabmessage.message,
            polygon = POSTdata['polygon'],
        )
    else:
        return None

##
# Function can alter a GeoData object. Add new technologie
##
def alterGeoData(message_id, aisEncoded = None, aisDecoded = None):
    #notification = .objects.get(id=message_id)
    #if aisEncoded is not None:
        #notification.aisEncoded = aisEncoded
    #if aisDecoded is not None:
        #notification.aisDecoded = aisDecoded
    #notification.save()
    return
