from rest_framework import serializers
from django.contrib.gis.geos import Point
from ..models import lorawanModel, DataModel, UplinkMessageModel, DecodedPayloadModel

# decoded-payload field in uplink_message in the JSON
class DecodedPayloadSerializer(serializers.Serializer):
    class Meta:
        model = DecodedPayloadModel
        fields = ['alt', 'hdop', 'lat', 'lon']

# Data field in the JSON
class uplinkMessageSerializer(serializers.Serializer):
    DecodedPayloadModel = DecodedPayloadSerializer(source="*")

    class Meta:
        model = UplinkMessageModel
        fields = '__all__'

# Data field in the JSON
class dataSerializer(serializers.Serializer):
    #uplink_message = uplinkMessageSerializer(source="*")

    class Meta:
        model = DataModel
        fields = ['type', 'received_at',]

###
# Top layer of JSON
####
class lorawanSerializer(serializers.HyperlinkedModelSerializer):
    #data = dataSerializer(source="*")

    def create(self, validated_data):
        print("LORAWAN create: ", validated_data)

        #print(validated_data["data"])
        print(self)
        print(self.fields)
        data_set_serializer = self.fields['data']
        print(data_set_serializer)

        data_validated_data = validated_data.pop('data')
        print(data_validated_data)

        newDataObj = data_set_serializer.create(data_validated_data)
        print(newDataObj)

        lora_obj = lorawanModel.objects.create(**validated_data)
        return lora_obj

    class Meta:
        model = lorawanModel
        fields = ['id', 'created_at', 'updated_at', 'geom', 'ack', 'msg', 'rssi', 'hdop', 'alt', 'received_at', 'data']
