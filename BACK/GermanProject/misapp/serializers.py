from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Categoria, Articulos
from django.contrib.auth.hashers import make_password



class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True
    )
    username = serializers.CharField(
        required=True
    )
    password = serializers.CharField( 
        min_length=8
    )
    #heredamos del modelo de autenticacion de dJAngo email, usuario y contraseña
    class Meta:
        model = get_user_model()
        field=('email','username', 'password')
    #hashea el valor de la contraseña y las compara para ver si es la correcta.
    def validate_password(self,value):
        return make_password(value)

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model: Categoria
        field= '__all__'


class ArticuloSerializer(serializers.ModelSerializer):
    class Meta:
        model: Articulos
        field= '__all__'

