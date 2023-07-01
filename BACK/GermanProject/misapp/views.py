from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from rest_framework import status, viewsets, generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny
from .serializer import *
from .models import *

# Create your views here.

permissions_classes = [IsAdminUser]

def home(request):
    return render(request, 'main-page.component.html')

class LoginView(APIView):
    def post(self, request):
        #recuperamos las credenciales y las autenticamos al user
        email= request.data.get('email', None)
        password= request.data.get('password', None)
        user= authenticate(email=email, password=password)

        #si es correcto añadimos a la request la info de la sesion
        if user:
            
            login(request,user)
            return Response(status=status.HTTP_200_OK)
        
        #si no es correcto devolvemos un codigo de error
        return Response(status=status.HTTP_404_NOT_FOUND)
    
class LogoutView(APIView):
    def post(self, request):
        #borramos de la request la informaicon de sesion
        logout(request)

        #devolvemos la respuesta al cliente
        return Response(status=status.HTTP_200_OK)
    
class SignupView(generics.CreateAPIView):
    serializer_class = UserSerializer  

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
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UsersList(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    http_method_names = ['get']
    permission_classes = [IsAdminUser]
    def list(self, request):
        queryset = self.get_queryset()
        serializer = UserSerializer(queryset, many=True)
        if self.request.user.is_authenticated:
            return Response(serializer.data)
        

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
        

