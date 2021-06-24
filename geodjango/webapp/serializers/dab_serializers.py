from rest_framework import serializers
from ..models import DAB

class DABSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = DAB
        fields = ['id', 'message_id', 'message_type', 'message', 'ship_id']