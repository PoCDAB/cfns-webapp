#
# CFNS - Rijkswaterstaat CIV, Delft © 2020 - 2021 <cfns@rws.nl>
#
# Copyright 2020 - 2021 Daniël Geerts <daniel.geerts@rws.nl>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#

from rest_framework import serializers
from django.contrib.gis.geos import Point
from ..models import lorawanModel, gatewayModel, lorawanGatewayConnectionModel

# This LoRaWAN serializer is activated when an API call is received
# It creates a new DB record for the LoRaWAN message and creates new records for the used gateway, inclusive a join record
class lorawanSerializer(serializers.HyperlinkedModelSerializer):
    def create(self, validated_data):
        allJSONData = self.context["request"].data

        decoded_payload = allJSONData["uplink_message"]["decoded_payload"]
        decoded_payload_keys = ('lat', 'lon', 'alt', 'hdop', 'ack', 'msg')
        if decoded_payload and set(decoded_payload_keys).issubset(decoded_payload):
            lora_obj = lorawanModel.objects.create(**validated_data)
            lora_obj.alt = decoded_payload["alt"]
            lora_obj.hdop = decoded_payload["hdop"]
            lora_obj.ack = decoded_payload["ack"]
            lora_obj.msg = decoded_payload["msg"]

            lora_obj.geom = Point(decoded_payload["lon"], decoded_payload["lat"])  # x = lon, y = lat
            lora_obj.save()

            rx_metadata = allJSONData["uplink_message"]["rx_metadata"]
            if rx_metadata:
                gateway_keys = ('rssi', 'snr', 'gateway_ids')
                for gateway in rx_metadata:
                    if gateway and set(gateway_keys).issubset(gateway):
                        gateway_obj = gatewayModel.objects.create()
                        gateway_obj.rssi = gateway["rssi"]
                        gateway_obj.snr = gateway["snr"]
                        gateway_ids_keys = ('gateway_id', 'eui')
                        if set(gateway_ids_keys).issubset(gateway["gateway_ids"]):
                            gateway_obj.gateway_id = gateway["gateway_ids"]["gateway_id"]
                            gateway_obj.gateway_eui = gateway["gateway_ids"]["eui"]
                        gateway_obj.save()

                        linktoeachother = lorawanGatewayConnectionModel.objects.create()
                        linktoeachother.gateway = gateway_obj
                        linktoeachother.lorawan = lora_obj
                        linktoeachother.save()

            return lora_obj
        return None

    class Meta:
        model = lorawanModel
        fields = ['id', 'created_at', 'updated_at', 'ack', 'msg', 'hdop', 'alt', 'geom',]# 'gateways',]
