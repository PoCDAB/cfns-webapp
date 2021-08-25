from rest_framework import serializers
from django.contrib.gis.geos import Point
from ..models import lorawanModel, gatewayModel

###
# LoRaWAN serializer
# POST data from TheThingsNetwork (TTN) is parsed to the 
####
class lorawanSerializer(serializers.HyperlinkedModelSerializer):
    def create(self, validated_data):
        allJSONData = self.context["request"].data
        lora_obj = lorawanModel.objects.create(**validated_data)

        decoded_payload = allJSONData["uplink_message"]["decoded_payload"]
        decoded_payload_keys = ('lat', 'lon', 'alt', 'hdop', 'alt')
        if decoded_payload and set(decoded_payload_keys).issubset(decoded_payload):
            lat = decoded_payload["lat"]
            lon = decoded_payload["lon"]

            lora_obj.geom = Point(lat, lon)
            lora_obj.alt = decoded_payload["alt"]
            lora_obj.hdop = decoded_payload["hdop"]
            lora_obj.alt = decoded_payload["alt"]
            rx_metadata =  allJSONData["uplink_message"]["rx_metadata"]
            if rx_metadata:
                for gateway in rx_metadata:
                    gateway_keys = ('rssi', 'snr', 'gateway_id', 'gateway_eui')
                    if set(gateway_keys).issubset(gateway):
                        gateway_obj = gatewayModel.objects.create()
                        gateway_obj.rssi = gateway["rssi"]
                        gateway_obj.snr = gateway["snr"]
                        gateway_obj.gateway_id = gateway["gateway_id"]
                        gateway_obj.gateway_eui = gateway["gateway_eui"]
                        gateway_obj.save()
                        lora_obj.gateways.add(gateway_obj)
            lora_obj.save()
        else:
            print("Something went wrong with the lorawanSerializer")
            return None
        return lora_obj

    class Meta:
        model = lorawanModel
        fields = ['id', 'created_at', 'updated_at', 'geom', 'ack', 'msg', 'hdop', 'alt', 'gateways']
