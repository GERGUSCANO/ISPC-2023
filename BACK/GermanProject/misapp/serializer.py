from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import *
from django.contrib.auth.hashers import make_password


class ArticuloSerializer(serializers.ModelSerializer):
    class Meta:
        model: Articulos
        fields='__all__'

class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True)
    username = serializers.CharField(
        required=True)
    password = serializers.CharField(
        min_length=8)
    class Meta:
        model = get_user_model()
        fields = ('email', 'username', 'password')
    def validate_password(self, value):
        return make_password(value)
    

    #agregar doc