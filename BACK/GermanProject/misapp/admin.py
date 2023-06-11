from django.contrib import admin
from .models import USUARIOS
from .models import ROL



class ROLADMIN(admin.ModelAdmin):
    list_display=('rol')

class USUARIOADMIN(admin.ModelAdmin):
    list_display=('nombre','idrol')


admin.site.register(ROL, ROLADMIN)
admin.site.register(USUARIOS, USUARIOADMIN)
