#django imports
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
#rest framework import
from rest_framework import response
from rest_framework import authentication, generics, permissions
from rest_framework.settings import api_settings
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.permissions import IsAdminUser, IsAuthenticated
#knox import
from knox.views import Loginview as KnoxLoginView
from knox.auth import TokenAuthentication

#local import
from .serializer import *
from .models import *

#local apps import
from core.serializers import UserSerializer, AuthSerializer

from rest_framework.authentication import SessionAuthentication

# Create your views here.

permissions_classes = [IsAdminUser]

def home(request):
    return render(request, 'main-page.component.html')

class CreateUserView(generics.CreateAPIView):
    # Create user API view
    serializer_class = UserSerializer

class Signup(generics.GenericAPIView):
    serializer_class= RegisterSerializer
    def post(self,request,*args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]
        })

class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)
    
class ManageUserView(generics.RetrieveUpdateAPIView):
    'Gestionar el usuario autenticado'
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self):
        'Recuperar y devolver el usuario autenticado'
        return self.request.user

class LogoutView(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def post(self, request, format=None):
        request._auth.delete()
        user_logged_out.send(
            sender=request.user.__class__,
            request=request, user=request.user
        )
        return response(
            None, 
            status=status.HTTP_204_NO_CONTENT
        )


class LogoutAllView(APIView):
    '''
    Log the user out of all sessions
    I.E. deletes all auth tokens for the user
    '''
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def post(self, request, format=None):
        request.user.auth_token_set.all().delete()
        user_logged_out.send(sender=request.user.__class__,
                             request=request, user=request.user)
        return response(None, status=status.HTTP_204_NO_CONTENT)


class ProfileView(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated] #Solo usuarios logueados pueden ver.
    serializer_class = UserSerializer
    http_method_names = ['get', 'patch']
    def get_object(self):
        if self.request.user.is_authenticated:
            return self.request.user
    def patch_object(self,request):
        serializer = UserSerializer(data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return response(serializer.data, status=status.HTTP_201_CREATED)
        return response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UsersList(generics.ListCreateAPIView):
    queryset = UserSerializer.objects.all()
    serializer_class = UserSerializer
    http_method_names = ['get']
    permission_classes = [IsAdminUser]
    def list(self, request):
        queryset = self.get_queryset()
        serializer = UserSerializer(queryset, many=True)
        if self.request.user.is_authenticated:
            return response(serializer.data)
        

class RolViewSet(viewsets.ModelViewSet):
    queryset=ROL.objects.all()
    serializer_class=RolSerializer

class EstadoViewSet(viewsets.ModelViewSet):
    queryset=Estados.objects.all()
    serializer_class=EstadosSerializer

class ProveedoresViewSet(viewsets.ModelViewSet):
    queryset=Proveedores.objects.all()
    serializer_class=ProveedoresSerializer

class IngresoViewSet(viewsets.ModelViewSet):
    queryset=Ingreso.objects.all()
    serializer_class=IngresoSerializer

class OrdenViewSet(viewsets.ModelViewSet):
    queryset=Orden.objects.all()
    serializer_class=OrdenSerializer

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset=Categoria.objects.all()
    serializer_class=CategoriaSerializer

class EnvioViewSet(viewsets.ModelViewSet):
    queryset=Envio.objects.all()
    serializer_class=EnvioSerializer

class ArticulosViewSet(viewsets.ModelViewSet):
    queryset=Articulos.objects.all()
    serializer_class=ArticulosSerializer

class DetalleVentaViewSet(viewsets.ModelViewSet):
    queryset=DetalleVenta.objects.all()
    serializer_class=DetalleVentaSerializer

class DetalleIngresoViewSet(viewsets.ModelViewSet):
    queryset=DetalleIngreso.objects.all()
    serializer_class=DetalleIngresosSerializer
        

