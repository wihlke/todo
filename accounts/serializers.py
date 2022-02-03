from rest_framework import serializers
from .models import User


class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(required=True , write_only = True)
    
    class Meta:
        model = User
        fields = ('email', 'password', 'name')


class UserSerializer(UserRegisterSerializer):
    class Meta:
        model = User
        fields = [
             'email', 
             'password',
        ]