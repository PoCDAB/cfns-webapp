from rest_framework import serializers
from django.contrib.gis.geos import Point
from django.shortcuts import get_object_or_404
from ..models import lorawanModel, ContextModel

# decoded-payload field in uplink_message in the JSON
class frmPayloadSerializer(serializers.Serializer):
    class Meta:
        fields = ['alt', 'hdop', 'lat', 'lon']

# Uplink_message field in data in the JSON
class rxMetadataSerializer(serializers.Serializer):
    class Meta:
        fields = ['rssi']

# Data field in the JSON
class uplinkMessageSerializer(serializers.Serializer):
    rx_metadata = rxMetadataSerializer(many=True, source="*")
    frm_payload = frmPayloadSerializer(source="*")
    class Meta:
        fields = ['rx_metadata', 'frm-payload']

# Data field in the JSON
class dataSerializer(serializers.Serializer):
    uplink_message = uplinkMessageSerializer(source="*")


# Data field in the JSON
class contextSerializer(serializers.Serializer):
    class Meta:
        model = ContextModel
        fields = '__all__'

###
# Top layer of JSON
####
class lorawanSerializer(serializers.HyperlinkedModelSerializer):
    #data = dataSerializer(read_only=True, source="*")
    rssi = serializers.ReadOnlyField(source='data.uplink_message.rx_metadata[0].rssi')
    lat = serializers.ReadOnlyField(source='data.uplink_message.decoded_payload.lat')
    lon = serializers.ReadOnlyField(source='data.uplink_message.decoded_payload.lon')
    alt = serializers.ReadOnlyField(source='data.uplink_message.decoded_payload.alt')
    hdop = serializers.ReadOnlyField(source='data.uplink_message.decoded_payload.hdop')

    def create(self, validated_data):
        print("LORAWAN create: ", validated_data)

        lora_obj = lorawanModel.objects.create(**validated_data)
        return lora_obj

    class Meta:
        model = lorawanModel
        fields = '__all__'
