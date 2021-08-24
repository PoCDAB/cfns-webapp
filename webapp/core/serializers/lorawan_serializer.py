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
    context = contextSerializer(read_only=True, many=True,source="*")

    def create(self, validated_data):
        #rx_metadata = validated_data.pop('data').pop('uplink_message').pop('rx_metadata')
        #frm_payload = validated_data.pop('data').pop('uplink_message').pop('frm_payload')
        print("LORAWAN create: ", validated_data)
        context = get_object_or_404(ContextModel, tentant_id=validated_data.get('tentant_id'))

        for d in context:
            print(d, context[d])
        #for d in rx_metadata:
            #print(d, rx_metadata[d])
        #for d in frm_payload:
            #print(d, frm_payload[d])
        for d in validated_data:
            print(d, validated_data[d])

        lora_obj = lorawanModel.objects.create(**validated_data)
        #lora_obj['geom'] = Point(frm_payload['lat'], frm_payload['lon'])
        #lora_obj['hdop'] = frm_payload['hdop']
        #lora_obj['alt'] = frm_payload['alt']
        #lora_obj['rssi'] = rx_metadata['rssi']

        return lora_obj

    class Meta:
        model = lorawanModel
        fields = '__all__'