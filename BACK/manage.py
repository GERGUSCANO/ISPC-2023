#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'abm_ispc.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()

from django.db import models

class Marca(models.Model):
    id_marca = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)

class Producto(models.Model):
    id_producto = models.IntegerField(primary_key=True)
    id_marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)

class Categoria(models.Model):
    id_categoria = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)

class ProductoCategoria(models.Model):
    id_productoCategoria = models.IntegerField(primary_key=True)
    id_producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    id_categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

class EstadoEnvio(models.Model):
    id_estadoEnvio = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)
    codigo_rastreo = models.CharField(max_length=20)

class Envio(models.Model):
    id_envio = models.IntegerField(primary_key=True)
    id_estadoenvio = models.ForeignKey(EstadoEnvio, on_delete=models.CASCADE)
    direccion_envio = models.CharField(max_length=255)
    ciudad_envio = models.CharField(max_length=255)
    fecha_envio = models.DateField()

class Pago(models.Model):
    id_pago = models.IntegerField(primary_key=True)
    metodo_pago = models.CharField(max_length=255)
    estado_pago = models.CharField(max_length=255)
    fecha_pago = models.DateField()

class Usuario(models.Model):
    id_usuario = models.IntegerField(primary_key=True)
    correo = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

class Cliente(models.Model):
    id_cliente = models.IntegerField(primary_key=True)
    id_usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    direccion = models.CharField(max_length=255)
    telefono = models.CharField(max_length=15)
    fecha_nacimiento = models.DateField()

class Pedido(models.Model):
    id_pedido = models.IntegerField(primary_key=True)
    id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    id_pago = models.ForeignKey(Pago, on_delete=models.CASCADE)
    id_envio = models.ForeignKey(Envio, on_delete=models.CASCADE)
    estado = models.CharField(max_length=255)
    fecha = models.DateField()
    total = models.DecimalField(max_digits=10, decimal_places=2)

class ProductoPedido(models.Model):
    id_productoPedido = models.IntegerField(primary_key=True)
    id_pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    id_producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    descripcion = models.CharField(max_length=100)

class Carrito(models.Model):
    id_carrito = models.IntegerField(primary_key=True)
    id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    fecha_creacion = models.DateField()

class CarritoProducto(models.Model):
    id_carritoProducto = models.IntegerField(primary_key=True)
    id_carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE)
    id_producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    descripcion = models.CharField(max_length=100)

class Comentario(models.Model):
    id_comentario = models.IntegerField(primary_key=True)
    id_cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    comentario = models.TextField
