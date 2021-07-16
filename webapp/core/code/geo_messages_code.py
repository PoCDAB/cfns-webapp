import json
from django.contrib.gis.geos import Point, Polygon, GEOSGeometry
from ..models import geoMessageModel, geoPointModel, geoCircleModel, geoPolygonModel
from re import search

def createGeoNotification(dabmessage, POSTdata):
    if dabmessage.message_type == 0:
        return geoMessageModel.objects.create(
            dab = dabmessage,
            message = dabmessage.message,
        )
    elif dabmessage.message_type == 1:
        return geoPointModel.objects.create(
            dab = dabmessage,
            message = dabmessage.message,
            location = format_pointstr_from_osmwidget(POSTdata['point'], Point),
        )
    elif dabmessage.message_type == 2:
        return geoCircleModel.objects.create(
            dab = dabmessage,
            message = dabmessage.message,
            location = format_pointstr_from_osmwidget(POSTdata['point'], Point),
            radius = POSTdata["radius"],
        )
    elif dabmessage.message_type == 3:
        return geoPolygonModel.objects.create(
            dab = dabmessage,
            message = dabmessage.message,
            polygon = format_pointstr_from_osmwidget(POSTdata['polygon'], Polygon),
        )
    else:
        return None

def alterGeoNotification(message_id, aisEncoded = None, aisDecoded = None):
    notification = geoMessageModel.objects.get(id=message_id)
    if aisEncoded is not None:
        notification.aisEncoded = aisEncoded
    if aisDecoded is not None:
        notification.aisDecoded = aisDecoded
    notification.save()

def format_pointstr_from_osmwidget(osm_output, type):
    srid = 3857
    c = find_between(osm_output, ':[', ']}').split(',')

    if type is Point:
        return"SRID=" + str(srid) + ";POINT(" + c[0] + " " + c[1] + ")"
    elif type is Polygon:
        c = str(c).replace("['[[", '(').replace("]]']", ')').replace("]', '[", ', ').replace("', '", ' ')
        return "SRID=" + str(srid) + ";POLYGON(" + c + ")"

def find_between( s, first, last ):
    try:
        start = s.index( first ) + len( first )
        end = s.index( last, start )
        return s[start:end]
    except ValueError:
        return ""