from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import *
from django.contrib.auth.hashers import make_password


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
class RolSerializer(serializers.ModelSerializer):
    class Meta:
        model=ROL
        fields='__all__'

class EstadosSerializer(serializers.ModelSerializer):
    class Meta:
        model=Estados
        fields='__all__'

class ProveedoresSerializer(serializers.ModelSerializer):
    class Meta:
        model=Proveedores
        fields='__all__'

class IngresoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Ingreso
        fields='__all__'

class OrdenSerializer(serializers.ModelSerializer):
    class Meta:
        model= Orden
        fields='__all__'

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model= Categoria
        fields='__all__'

class EnvioSerializer(serializers.ModelSerializer):
    class Meta:
        model=Envio
        fields='__all__'

class ArticulosSerializer(serializers.ModelSerializer):
    class Meta:
        model=Articulos
        fields='__all__'

class DetalleVentaSerializer(serializers.ModelSerializer):
    class Meta:
        model=DetalleVenta
        fields='__all__'

class DetalleIngresosSerializer(serializers.ModelSerializer):
    class Meta:
        model=DetalleIngreso
        fields='__all__'    
