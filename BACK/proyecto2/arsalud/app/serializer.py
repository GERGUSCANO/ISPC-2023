from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from .models import *
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.serializers import ValidationError



class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True)
    username = serializers.CharField(
        required=True)
    password = serializers.CharField(
        min_length=8)

    def validate_password(self, value):
        return make_password(value)


    class Meta:
        model = get_user_model()
        #fields = ('email', 'username', 'password')
        fields='__all__'

class DireccionSerializer(serializers.ModelSerializer):

    class Meta:
        model= Direccion
        fields='__all__'

class ProvinciaSerializer(serializers.ModelSerializer):

    class Meta:
        model= Provincia
        fields='__all__'

class LocalidadSerializer(serializers.ModelSerializer):

    class Meta:
        model= Localidad
        fields='__all__'

class CarritoSerializer(serializers.ModelSerializer):

    class Meta:
        model= Carrito
        fields='__all__'

class ElementosCarritoSerializer(serializers.ModelSerializer):

    class Meta:
        model= ElementosCarrito
        fields='__all__'

class ArticuloSerializer(serializers.ModelSerializer):

    class Meta:
        model= Articulo
        fields='__all__'

class CategoriaSerializer(serializers.ModelSerializer):

    class Meta:
        model= Categoria
        fields='__all__'

class EstadoSerializer(serializers.ModelSerializer):

    class Meta:
        model= Estado
        fields='__all__'

class EnvioSerializer(serializers.ModelSerializer):

    class Meta:
        model= Envio
        fields='__all__'

"""class TipoUsuarioSerializer(serializers.ModelSerializer):

    class Meta:
        model= TipoUsuarios
        fields='__all__'
"""
class DetallePedidoSerializer(serializers.ModelSerializer):

    class Meta:
        model= DetallePedido
        fields=['cantidad', 'id_pedido', 'id_libro']

class PedidoSerializer(serializers.ModelSerializer):

    class Meta:
        model= Pedido
        fields = ['id_cliente', 'nro_tracking', 'id_orden']

class EstadoSerializer(serializers.ModelSerializer):

    class Meta:
        model= Estado
        fields='__all__'

class ModoPagoSerializer(serializers.ModelSerializer):

    class Meta:
        model= ModoPago
        fields = ['monto', 'detalle', 'id_orden']


#
# Serializador completo para recibir todos los datos de la compra /
# y poder distribuir en varios modelos a la vez
# 

class PagosSerializer(serializers.ModelSerializer):
        id_cliente = serializers.ReadOnlyField(source='context["request"].session.get("id_cliente")')

        class Meta:
            model = Pagos
            fields = ['id_cliente', 'code', 'dni', 'email', 'tarjeta', 'titular', 'vencimiento']


class ElementosSerializer(serializers.Serializer):
    Articulo = serializers.DictField()
    cantidad = serializers.IntegerField()

    def create(self, validated_data):
        articulo_data = validated_data['articulo']
        articulo_instance = Articulo.objects.get(id_articulo=articulo_data['id_articulo'])
        elemento = ElementosCarrito.objects.create(articulo=articulo_instance, cantidad=validated_data['cantidad'])
        return elemento


class OrdenSerializer(serializers.ModelSerializer):
    elementos = serializers.ListField(child=ElementosSerializer(), read_only=True)
    precioTotal = serializers.DecimalField(decimal_places=2, max_digits=7, write_only=True)
    id_cliente = serializers.PrimaryKeyRelatedField(read_only=True)
    id_estado = serializers.PrimaryKeyRelatedField(read_only=True)
    total = serializers.DecimalField(decimal_places=2, max_digits=7, read_only=True)

    class Meta:
        model = Orden
        fields = ['id_orden', 'fecha', 'total', 'id_cliente', 'id_estado', 'elementos', 'precioTotal']
        extra_kwargs = {
            'total': {'write_only': True},
        }