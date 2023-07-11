from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *
from django.contrib.auth import get_user_model

@admin.register(get_user_model())
class CustomUserAdmin(UserAdmin):
    pass

# Register your models here.

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('dni', 'nombre', 'apellido', \
                    'password', 'email', 'dni', 'fecha_nac', \
                    'telefono', 'id_direccion')

class DireccionAdmin(admin.ModelAdmin):
    list_display = ('id_direccion', 'calle','numero', 'departamento', 'piso', 'barrio', 'id_provincia', \
                    'id_localidad')
    
class ProvinciaAdmin(admin.ModelAdmin):
    list_display = ('id_provincia', 'nombre')

class LocalidadAdmin(admin.ModelAdmin):
    list_display = ('id_localidad', 'nombre', 'codigo_postal')

class CarritoAdmin(admin.ModelAdmin):
    list_display = ('id_carrito', 'fecha_creacion')

class ElementosCarritoAdmin(admin.ModelAdmin):
    list_display = ('id_elementos_carrito', 'id_carrito', 'id_articulo', \
                    'cantidad')
    
class ArticuloAdmin(admin.ModelAdmin):
    list_display = ('id_articulo', 'categoria', 'nombre', \
                    'tipo_presentacion', 'descripcion', 'precio', 'stock', \
                    'img_url')

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre','detalle')

class DetallePedidoAdmin(admin.ModelAdmin):
    list_display = ('cantidad', 'id_pedido', \
                    'id_articulo')
    
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('id_pedido', 'seguimiento', 'id_cliente', \
                    'fecha', 'id_orden', 'nro_tracking')

class OrdenAdmin(admin.ModelAdmin):
    list_display = ('id_orden', 'pago','fecha', 'total', \
                    'id_cliente', 'estado', 'tipo_comprobante', \
                    'detalle_comprobante')
    
class EstadoAdmin(admin.ModelAdmin):
    list_display = ('id_estado', 'detalle')

class ModoPagoAdmin(admin.ModelAdmin):
    list_display = ('id_mp', 'tipos', 'fecha', 'monto', \
                    'detalle')


admin.site.register(Direccion,DireccionAdmin)
admin.site.register(Provincia,ProvinciaAdmin)
admin.site.register(Localidad,LocalidadAdmin)
admin.site.register(Carrito,CarritoAdmin)
admin.site.register(ElementosCarrito,ElementosCarritoAdmin)
admin.site.register(Articulo,ArticuloAdmin)
admin.site.register(Categoria,CategoriaAdmin)
admin.site.register(DetallePedido,DetallePedidoAdmin)
admin.site.register(Pedido,PedidoAdmin)
admin.site.register(Orden,OrdenAdmin)
admin.site.register(Estado,EstadoAdmin)
admin.site.register(ModoPago,ModoPagoAdmin)