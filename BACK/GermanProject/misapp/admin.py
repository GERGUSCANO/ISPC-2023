from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model



@admin.register(get_user_model())
class CustomUserAdmin(UserAdmin):
    pass


class ROLADMIN(admin.ModelAdmin):
    list_display=["idrol","detalle"]

class CategoriaADMIN(admin.ModelAdmin):
    list_display=('idcategoria','nombre','descripcion')

class ArticulosADMIN(admin.ModelAdmin):
    list_display=('idarticulo', 'nombre', 'descripcion', 'precio', 'stock', 'imagen','precio','idcategoria')

class EstadosADMIN(admin.ModelAdmin):
    list_display=('idestados', 'detalle')

class ProveedoresADMIN(admin.ModelAdmin):
    list_display=('idproveedor', 'nombre')

class IngresosADMIN(admin.ModelAdmin):
    list_display=('idingreso', 'idproveedor', 'tipoComprobante', 'serieComprobante','numeroComprobante', 'fecha', 'total', 'estado')

class OrdenADMIN(admin.ModelAdmin):
    list_display=('idorden', 'usuario')

class EnvioADMIN(admin.ModelAdmin):
    list_display=('idenvio','descripcion','direccion_envio', 'fecha', 'cod_seguimiento', 'orden','estado')

class DetalleVentaADMIN(admin.ModelAdmin):
    list_display=('iddetalle','cantidad','precio', 'descuento', 'articulo', 'orden')    

class DetalleIngresoADMIN(admin.ModelAdmin):
    list_display=('iddetalle','cantidad', 'descripcion')    


admin.site.register(ROL, ROLADMIN)
admin.site.register(Categoria, CategoriaADMIN)
admin.site.register(Articulos, ArticulosADMIN)
admin.site.register(Estados, EstadosADMIN)
admin.site.register(Proveedores, ProveedoresADMIN)
admin.site.register(Ingreso, IngresosADMIN)
admin.site.register(Orden, OrdenADMIN)
admin.site.register(Envio, EnvioADMIN)
admin.site.register(DetalleIngreso, DetalleIngresoADMIN)
admin.site.register(DetalleVenta, DetalleVentaADMIN)

