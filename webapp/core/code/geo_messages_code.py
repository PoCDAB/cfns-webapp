from django.contrib.gis.geos import Point
from ..models import geoMessageModel, geoPointModel, geoCircleModel, geoPolygonModel

def createGeoNotification(dabmessage, POSTdata):
    if dabmessage.message_type == 0:
        return geoMessageModel.objects.create(
            dab = dabmessage,
            message = dabmessage.message,
        )
    elif dabmessage.message_type == 1:
        print("Point")
        return geoPointModel.objects.create(
            dab = dabmessage,
            message = dabmessage.message,
            location = POSTdata["point"],
        )
    elif dabmessage.message_type == 2:
        print("Radius")
        return geoCircleModel.objects.create(
            dab = dabmessage,
            message = dabmessage.message,
            location = POSTdata["point"],
            radius = POSTdata["radius"],
        )
    elif dabmessage.message_type == 3:
        print("Polygon")
        return geoPolygonModel.objects.create(
            dab = dabmessage,
            message = dabmessage.message,
            polygon = POSTdata["polygon"],
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
