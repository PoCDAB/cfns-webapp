from rest_framework import serializers
from ..models import dabModel

class dabSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = dabModel
        fields = ['id', 'message_id', 'message_type', 'message', 'ship_id']