from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from django.contrib.gis.geos import Point
from rest_framework import serializers
from .models import AIS
from .models import aisDecoded
from pyais import NMEAMessage, decode_msg


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['id', 'url', 'name']


class AISSerializer(serializers.HyperlinkedModelSerializer):
    def create(self, validated_data):
        encodedAIS = AIS.objects.create(**validated_data)
        decoded = {}
        decoded['encodedAIS'] = encodedAIS
        print('==================================')
        print(validated_data['message'])
        msg = decode_msg(validated_data['message'])
        print(msg)
        print('==================================')
        if 'shipname' in msg:
            decoded['name'] = msg['shipname']
        if 'lat' and 'lon' in msg:
            decoded['geom'] = Point(msg['lon'], msg['lat'])
        if 'course' in msg:
            decoded['course'] = msg['course']
        decoded['received_from'] = validated_data['received_from']
        decoded['received_at'] = validated_data['received_at']
        decoded['received_at'] = validated_data['received_at']
        aisDecoded.objects.create(**decoded)
        return encodedAIS

    class Meta:
        model = AIS
        fields = ['id', 'received_from', 'message', 'created_at', 'updated_at']