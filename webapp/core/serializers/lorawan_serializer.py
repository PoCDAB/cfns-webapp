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
    uplink_message = uplinkMessageSerializer(source="*")

    class Meta:
        model = DataModel
        fields = '__all__'

###
# Top layer of JSON
####
class lorawanSerializer(serializers.HyperlinkedModelSerializer):
    data = dataSerializer()

    def create(self, validated_data):
        print("LORAWAN create: ", validated_data)
        data = validated_data.pop('data')
        print(data)
        lora_obj = lorawanModel.objects.create(**validated_data)
        return lora_obj

    class Meta:
        model = lorawanModel
        fields = '__all__'
