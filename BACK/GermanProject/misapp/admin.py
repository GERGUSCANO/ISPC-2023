from django.contrib import admin
from .models import USUARIOS
from .models import ROL
from .models import Producto
from .models import Categoria
from .models import estados
from .models import metadoPago
from .models import Pagos
from .models import cliente
from .models import direccion




class ROLADMIN(admin.ModelAdmin):
    list_display=["idrol","rol"]

class USUARIOADMIN(admin.ModelAdmin):
    list_display=('nombre','idrol')

class CategoriaADMIN(admin.ModelAdmin):
    list_display=('nombrecategoria','idcategoria')

class ProductoADMIN(admin.ModelAdmin):
    list_display=('idproducto', 'nombreProducto', 'descripcion', 'precio', 'stock', 'imagen','idcategoria')

class estadosADMIN(admin.ModelAdmin):
    list_display=('idestados', 'descripcion')

class metodoPagoADMIN(admin.ModelAdmin):
    list_display=('idmetodoPago', 'metodoPago')

class Pagos(admin.ModelAdmin):
    list_display=('idpago', 'idestados')

class clientes(admin.ModelAdmin):
    list_display=('idcliente', 'idestados')

class direccion(admin.ModelAdmin):
    list_display=('idpago', 'idestados')

admin.site.register(ROL, ROLADMIN)
admin.site.register(USUARIOS, USUARIOADMIN)
