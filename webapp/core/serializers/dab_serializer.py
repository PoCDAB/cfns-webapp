from rest_framework import serializers
from ..models import dabModel

# This DAB+ serializer is activated when an API call is received
# It creates a new DB record
class dabSerializer(serializers.HyperlinkedModelSerializer):
    def create(self, validated_data):
        return dabModel.objects.create(**validated_data)

    class Meta:
        model = dabModel
        fields = ['id', 'message_id', 'message_type', 'message', 'ship_id']