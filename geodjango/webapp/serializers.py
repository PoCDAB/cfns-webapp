from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model
User = get_user_model()
from .models import AIS
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['id', 'url', 'name']


class AISSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AIS
        fields = ['id', 'received_from', 'message', 'created_at', 'updated_at']