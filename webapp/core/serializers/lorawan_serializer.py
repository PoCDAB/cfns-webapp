from rest_framework import serializers
from ..models import lorawanModel

class lorawanSerializer(serializers.HyperlinkedModelSerializer):

    def validate(self, data):
        print("LORAWAN validate: ", data)
        return data

    def create(self, validated_data):
        print("LORAWAN create: ", validated_data)
        return lorawanModel.objects.create(**validated_data)

    class Meta:
        model = lorawanModel
        fields = ['received_at', 'geom', 'ack', 'msg', 'rssi', 'hdop', 'alt']
