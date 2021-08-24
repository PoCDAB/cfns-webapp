from rest_framework import serializers
from django.contrib.gis.geos import Point
from ..models import lorawanModel

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
    received_at = serializers.DateTimeField()
    ##uplink_message = uplinkMessageSerializer(source="*")

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
