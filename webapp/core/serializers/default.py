from django.contrib.auth.models import Group
from django.contrib.auth.models import User

from rest_framework import serializers

# This User serializer is activated when an API call is received
# It creates a new DB record
class UserSerializer(serializers.HyperlinkedModelSerializer):
    def create(self, validated_data):
        return User.objects.create(**validated_data)

    class Meta:
        model = User
        fields = ['id', 'url', 'username', 'email', 'groups']

# This Group serializer is activated when an API call is received
# It creates a new DB record
class GroupSerializer(serializers.HyperlinkedModelSerializer):
    def create(self, validated_data):
        return Group.objects.create(**validated_data)

    class Meta:
        model = Group
        fields = ['id', 'url', 'name']

