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
    def create(self, validated_data):
        print("=== self ===")
        print(self)
        print("=== fields ===")
        print(self.fields)
        print("=== data 1 ===")
        print(self.data)
        print("=== data 2 ===")
        print(self.fields["data"])
        print("=== uplink_message ===")
        print(self.fields["data"]["uplink_message"])
        print("=== decoded_payload ===")
        print(self.fields["data"]["uplink_message"]["decoded_payload"])
        print("====== data_set_serializer ======")
        print(self.fields["data"]["uplink_message"]["rx_metadata"])
        print("=================== DONE ===========================")

        lora_obj = lorawanModel.objects.create(**validated_data)
        return lora_obj

    class Meta:
        model = lorawanModel
        fields = ['id', 'created_at', 'updated_at', 'geom', 'ack', 'msg', 'rssi', 'hdop', 'alt', 'received_at', 'data']
