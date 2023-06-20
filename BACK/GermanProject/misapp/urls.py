from django import urls
from django.urls import path, include
from .views import  LoginView, LogoutView, signupView, profileView, ListarUsuarios, agregarArticulo, customJsonYBajarStock, retornarPagado, carritoComprasVista


urlpatterns = [
    # Auth views
    path('auth/login/',
         LoginView.as_view(), name='auth_login'),

    path('auth/logout/',
         LogoutView.as_view(), name='auth_logout'),
     path('auth/reset/',
         include('django_rest_passwordreset.urls',
                 namespace='password_reset')),
     path('auth/registro/',
         signupView.as_view(), name='auth_signup'),
     path('user/profile/',
         profileView.as_view(), name='user_profile'),
     path('usuarios/',
         ListarUsuarios.as_view(), name='listar_usuarios'),
     path('agregararticulo/',
         agregarArticulo.as_view(), name='agregar_producto'),
    path('retornarPagado/',
         retornarPagado.as_view(), name='retornarPagado'),
    path('actualizarstock/<int:pk>/<int:cantidad>',
          customJsonYBajarStock.as_view(), name='customjsonybajarstock'), #
    path('carrito/',
         carritoComprasVista.as_view(), name='carritodecompras'),
]