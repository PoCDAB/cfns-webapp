from rest_framework import serializers
from django.contrib.gis.geos import Point
from ..models import lorawanModel, gatewayModel

###
# Top layer of JSON
####
class lorawanSerializer(serializers.HyperlinkedModelSerializer):
    def create(self, validated_data):
        allJSONData = self.context["request"].data

        decoded_payload = allJSONData["uplink_message"]["decoded_payload"]

        print("=== context ===")
        print('alt', decoded_payload["alt"])
        print('hdop', decoded_payload["hdop"])
        print('lat', decoded_payload["lat"])
        print('lon', decoded_payload["lon"])
        print("=================== DONE ===========================")

        lora_obj = lorawanModel.objects.create(**validated_data)
        lora_obj.alt = decoded_payload["alt"]
        lora_obj.hdop = decoded_payload["hdop"]
        print(decoded_payload["lat"], decoded_payload["lon"])

        print('lora_obj.alt', lora_obj.alt)
        return lora_obj

    class Meta:
        model = lorawanModel
        fields = ['id', 'created_at', 'updated_at', 'ack', 'msg', 'hdop', 'alt', 'gateways', 'geom']
