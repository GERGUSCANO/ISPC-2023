from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from  misapp import views


routers= routers.DefaultRouter()
# routers.register(r'ROL', views.RolViewSet, "rol")
# routers.register(r'Estados', views.EstadoViewSet, "estados")
routers.register(r'Proveedores', views.ProveedoresViewSet, "proveedores")
routers.register(r'Ingreso', views.IngresoViewSet, "ingreso")
routers.register(r'Orden', views.OrdenViewSet, "orden")
routers.register(r'Categoria', views.CategoriaViewSet, "categoria")
routers.register(r'Envio', views.EnvioViewSet, "envio")
routers.register(r'Articulos', views.ArticulosViewSet, "articulos")
routers.register(r'DetalleVenta', views.DetalleVentaViewSet, "detalleventa")
routers.register(r'DetalleIngreso', views.DetalleIngresoViewSet, "detalle")


urlpatterns = [
    #api routes
    path('api/', include(routers.urls)),
    path('admin/', admin.site.urls),
    path('api/v1/', include('misapp.urls')),
]
