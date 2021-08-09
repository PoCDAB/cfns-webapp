from rest_framework import serializers
from django.contrib.gis.geos import Point
from pyais import decode_msg
from ..models import aisEncodedModel, aisDecodedModel

class aisSerializer(serializers.HyperlinkedModelSerializer):
    def create(self, validated_data):
        decodedAIS = {}
        msg = decode_msg(validated_data['message'])
        if 'mmsi' in msg:
            decodedAIS['mmsi'] = msg['mmsi']
        if 'shipname' in msg:
            decodedAIS['name'] = msg['shipname']
        if 'lat' and 'lon' in msg:
            decodedAIS['geom'] = Point(msg['lon'], msg['lat'])
        if 'course' in msg:
            decodedAIS['course'] = msg['course']
        return decodedAIS

    class Meta:
        model = aisDecodedModel
        fields = ['id', 'received_from','message', 'received_at', 'mmsi', 'name', 'geom', 'course', 'created_at', 'updated_at']
