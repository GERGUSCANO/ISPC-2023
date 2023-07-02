from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth import  authenticate
from django.contrib.auth.hashers import make_password

class UserSerializer(serializers.ModelSerializer):
    'serializer para el objeto usuario'
    class Meta:
        model = User()
        fields = ('id','email', 'username')
    def validate_password(self, value):
        return make_password(value)
    
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')

        extra_kwargs = {
                            'password': { 
                                'write_only': True, 
                                'min_length': 5
                            }
                        }
        
    def create(self, validated_data):

        user = User.objects.create_user(**validated_data)

        return user
    
class AuthSerializer(serializers.Serializer):
    'serializer para el objeto de autenticación de usuario'
    username = serializers.CharField()
    password = serializers.CharField(
        style={'input_type': 'password'},
        trim_whitespace=False
    )    
    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')
        
        user = authenticate(
            request=self.context.get('request'),
            username=username,
            password=password
        )
        
        if not user:
            msg = ('Unable to authenticate with provided credentials')
            raise serializers.ValidationError(msg, code='authentication')

        attrs['user'] = user
        return 
    
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
