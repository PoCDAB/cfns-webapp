from rest_framework import serializers
from ..models import lorawanModel

# decoded-payload field in uplink_message in the JSON
class decoded_payloadSerializer(serializers.Serializer):
    alt = serializers.IntegerField()
    hdop = serializers.DecimalField(max_digits=19, decimal_places=2)
    lat = serializers.DecimalField(max_digits=19, decimal_places=2)
    lon = serializers.DecimalField(max_digits=19, decimal_places=2)
    class Meta:
        fields = ['alt', 'hdop', 'lat', 'lon']

# Uplink_message field in data in the JSON
class uplink_messageSerializer(serializers.Serializer):
    decoded_payload = decoded_payloadSerializer()
    class Meta:
        fields = ['decoded_payload']

# Data field in the JSON
class dataSerializer(serializers.Serializer):
    uplink_message = uplink_messageSerializer()
    class Meta:
        fields = ['uplink_message']

###
# Top layer of JSON
####
class lorawanSerializer(serializers.HyperlinkedModelSerializer):
    data = dataSerializer()

    def validate(self, data):
        print("LORAWAN validate: ", data)
        for d in data:
            print(d, data[d])
        return data

    def create(self, validated_data):
        print("LORAWAN create: ", validated_data)
        for d in validated_data:
            print(d, validated_data[d])
        return lorawanModel.objects.create(**validated_data)

    class Meta:
        model = lorawanModel
        fields = ['received_at', 'geom', 'ack', 'msg', 'rssi', 'hdop', 'alt']
