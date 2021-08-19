from rest_framework import serializers
from ..models import lorawanModel

class lorawanSerializer(serializers.HyperlinkedModelSerializer):
    def create(self, validated_data):
        return lorawanModel(**validated_data)

    class Meta:
        model = lorawanModel
        fields = ['geom', 'ack', 'msg', 'rssi', 'hdop', 'alt']
