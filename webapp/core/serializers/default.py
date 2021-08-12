from django.contrib.auth.models import Group
from django.contrib.auth.models import User

from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    def create(self, validated_data):
        return User(**validated_data)

    class Meta:
        model = User
        fields = ['id', 'url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    def create(self, validated_data):
        return Group(**validated_data)

    class Meta:
        model = Group
        fields = ['id', 'url', 'name']

