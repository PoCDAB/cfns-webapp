from rest_framework import serializers
from ..models import lorawanModel

class lorawanSerializer(serializers.HyperlinkedModelSerializer):

    def validate(self, data):
        print("LORAWAN validate: ", data)
        for d in data:
            print(d, data[d])
        return data

    def create(self, validated_data):
        print("LORAWAN create: ", validated_data)
        for d in validated_data:
            print(d, validated_data[d])
        return lorawanModel.objects.create(**validated_data)

    class Meta:
        model = lorawanModel
        fields = ['received_at', 'geom', 'ack', 'msg', 'rssi', 'hdop', 'alt']
