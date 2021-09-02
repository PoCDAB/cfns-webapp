from rest_framework import serializers
from django.contrib.gis.geos import Point
from pyais import decode_msg
from ..models import aisDecodedModel

# This AIS serializer is activated when an API call is received
# It decoded the AIS message and puts the correct fields into a new DB record
class aisSerializer(serializers.HyperlinkedModelSerializer):
    def create(self, validated_data):
        decodedAIS = aisDecodedModel.objects.create(**validated_data)
        msg = decode_msg(validated_data['message'])
        if 'mmsi' in msg:
            setattr(decodedAIS, 'mmsi', msg['mmsi'])
        if 'shipname' in msg:
            setattr(decodedAIS, 'name', msg['shipname'])
        if 'lat' and 'lon' in msg:
            setattr(decodedAIS, 'geom', Point(msg['lon'], msg['lat'])) # x = lon, y = lat
        if 'course' in msg:
            setattr(decodedAIS, 'course', msg['course'])
        decodedAIS.save()
        return decodedAIS

    class Meta:
        model = aisDecodedModel
        fields = ['id', 'received_from', 'received_at', 'message','mmsi', 'name', 'geom', 'course', 'ack', 'msg', 'rssi', 'created_at', 'updated_at']
