from rest_framework import serializers
from django.contrib.gis.geos import Point
from pyais import decode_msg
from ..models import AIS
from ..models import aisDecoded

class AISSerializer(serializers.HyperlinkedModelSerializer):
    def create(self, validated_data):
        encodedAIS = AIS.objects.create(**validated_data)
        decoded = {}
        decoded['encodedAIS'] = encodedAIS
        msg = decode_msg(validated_data['message'])
        if 'mmsi' in msg:
            decoded['mmsi'] = msg['mmsi']
        if 'shipname' in msg:
            decoded['name'] = msg['shipname']
        if 'lat' and 'lon' in msg:
            decoded['geom'] = Point(msg['lon'], msg['lat'])
        if 'course' in msg:
            decoded['course'] = msg['course']
        aisDecoded.objects.create(**decoded)
        return encodedAIS

    class Meta:
        model = AIS
        fields = ['id', 'received_from', 'received_at', 'message', 'created_at', 'updated_at']
