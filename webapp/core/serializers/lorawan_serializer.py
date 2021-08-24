from rest_framework import serializers
from django.contrib.gis.geos import Point
from ..models import lorawanModel

# decoded-payload field in uplink_message in the JSON
class decodedPayloadSerializer(serializers.Serializer):
    class Meta:
        fields = ['alt', 'hdop', 'lat', 'lon']

# Uplink_message field in data in the JSON
class rxMetadataSerializer(serializers.Serializer):
    class Meta:
        fields = ['rssi', '', 'lat', 'lon']

# Data field in the JSON
class dataSerializer(serializers.Serializer):
    rx_metadata = rxMetadataSerializer(many=True, source="*")
    decoded_payload = decodedPayloadSerializer(source="*")

###
# Top layer of JSON
####
class lorawanSerializer(serializers.HyperlinkedModelSerializer):
    data = dataSerializer(source="*")

    def create(self, validated_data):
        rx_metadata = validated_data.pop('data').pop('rx_metadata')
        decoded_payload = validated_data.pop('data').pop('decoded_payload')
        print("LORAWAN create: ", validated_data)

        for d in rx_metadata:
            print(d, rx_metadata[d])
        for d in decoded_payload:
            print(d, decoded_payload[d])
        for d in validated_data:
            print(d, validated_data[d])

        lora_obj = lorawanModel.objects.create(**validated_data)
        lora_obj['geom'] = Point(decoded_payload['lat'], decoded_payload['lon'])
        lora_obj['hdop'] = decoded_payload['hdop']
        lora_obj['alt'] = decoded_payload['alt']
        lora_obj['rssi'] = rx_metadata['rssi']

        return lora_obj

    class Meta:
        model = lorawanModel
        fields = ['received_at', 'data', 'geom', 'ack', 'msg', 'rssi', 'hdop', 'alt']
