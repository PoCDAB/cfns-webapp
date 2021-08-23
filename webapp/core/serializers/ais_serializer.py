from rest_framework import serializers
from django.contrib.gis.geos import Point
from pyais import decode_msg
from ..models import aisDecodedModel

class aisSerializer(serializers.HyperlinkedModelSerializer):
    def create(self, validated_data):
        decodedAIS = aisDecodedModel(**validated_data)
        msg = decode_msg(validated_data['message'])
        if 'mmsi' in msg:
            setattr(decodedAIS, 'mmsi', msg['mmsi'])
        if 'shipname' in msg:
            setattr(decodedAIS, 'name', msg['shipname'])
        if 'lat' and 'lon' in msg:
            setattr(decodedAIS, 'geom', Point(msg['lon'], msg['lat']))
        if 'course' in msg:
            setattr(decodedAIS, 'course', msg['course'])
        return decodedAIS

    class Meta:
        model = aisDecodedModel
        fields = ['id', 'received_from', 'received_at', 'message','mmsi', 'name', 'geom', 'course', 'ack', 'msg', 'rssi', 'created_at', 'updated_at']
