from rest_framework import serializers
from .models import User

from djoser.serializers import UserCreateSerializer


class UserSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        fields = ('id', 'email', 'password', 'name')
        read_only_fields = ['id']

