from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from rest_framework import status, generics, viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser, AllowAny, IsAuthenticated
from .serializer import *
from .models import *
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

class SignupView(generics.CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = UserSerializer

class LoginView(APIView):
    permission_classes = [AllowAny]
    def post(self, request): #def post(request): usa HTTP POST
        # Recuperamos las credenciales y autenticamos al usuario
        email = request.data.get('email', None)
        password = request.data.get('password', None)
        # user guarda un objeto User con las credenciales validas
        user = authenticate(request, email=email, password=password) #se le agrego REQUEST. Si no funciona, borrar!

        # Si es correcto aniadimos a la request la informacion de sesion
        if user:
            login(request, user)
            
            # Verificar si el usuario ya tiene un carrito asociado
            if not user.id_carrito:
                # Si no tiene un carrito, crear uno nuevo y asociarlo al usuario
                carrito = Carrito.objects.create()
                user.id_carrito = carrito
                user.save()
                
            return Response(
                UserSerializer(user).data,
                status=status.HTTP_200_OK)
        
        # Si no es correcto devolvemos un error en la peticion
        return Response(
            status=status.HTTP_404_NOT_FOUND)

class LogoutView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        # Borramos de la request la informacion de sesion
        logout(request)

        # Devolvemos la respuesta al cliente
        return Response(status=status.HTTP_200_OK)
    
class CustomUserViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    def list(self, request):
        queryset = self.get_queryset()
        serializer = UserSerializer(queryset, many=True)
        if self.request.user.is_authenticated:
            return Response(serializer.data)

#Perfil de usuarios
class ProfileView(generics.RetrieveUpdateAPIView):
    permission_classes = [IsAuthenticated] #Solo usuario logueado puede ver.
    serializer_class = UserSerializer
    http_method_names = ['get', 'patch']
    def get_object(self):
        if self.request.user.is_authenticated:
            return self.request.user

#endopoint para gestionar la venta

class PagosView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = PagosSerializer(data=request.data)

        if serializer.is_valid():
            pagos = serializer.save(id_cliente=request.user)
            return Response(PagosSerializer(pagos).data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ComprarView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        elementos_data = request.data.pop('elementos', [])
        precio_total = request.data['precioTotal']
        total = float(precio_total)
        user = request.user
        estado_por_defecto = Estado.objects.get(id_estado=3)
        
        serializer = OrdenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        if user.is_authenticated:
            carrito = user.id_carrito

            Orden.objects.create(
                id_cliente=user,
                total=total,
                id_estado=estado_por_defecto
            )

            for elemento_data in elementos_data:
                articulo_data = elemento_data['articulo']
                cantidad = elemento_data['cantidad']

                try:
                    Articulo_instance = Articulo.objects.get(id_articulo=articulo_data['id_articulo'])
                    ElementosCarrito.objects.create(
                        id_carrito=carrito,
                        id_cliente=user,
                        id_articulo=Articulo_instance,
                        cantidad=cantidad
                    )
                except Articulo.DoesNotExist:
                    raise ValidationError(f"El articulo con ID {articulo_data['id_articulo']} no existe")

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({"detail": "El usuario no está autenticado"}, status=status.HTTP_401_UNAUTHORIZED)
########################################################################

class DireccionViewSet(viewsets.ModelViewSet):  #direccion editable por usuario logueado
    permission_classes = [IsAuthenticated]
    queryset = Direccion.objects.all()
    serializer_class = DireccionSerializer

class DireccionAdmin(viewsets.ModelViewSet):    #direccion editable
    permission_classes = [IsAdminUser]
    queryset = Direccion.objects.all()
    serializer_class = DireccionSerializer
   
class ProvinciaViewSet(viewsets.ReadOnlyModelViewSet):  #provincia solo vista. Llenar antes de opciones.
    permission_classes = [AllowAny]
    queryset = Provincia.objects.all()
    serializer_class = ProvinciaSerializer

class ProvinciaAdmin(viewsets.ModelViewSet):    #provincia editable
    permission_classes = [IsAdminUser]
    queryset = Provincia.objects.all()
    serializer_class = ProvinciaSerializer

class LocalidadViewSet(viewsets.ReadOnlyModelViewSet):  #localidad solo vista. Llenar antes de opciones.
    permission_classes = [AllowAny]
    queryset = Localidad.objects.all()
    serializer_class = LocalidadSerializer

class LocalidadAdmin(viewsets.ModelViewSet):    #localidad editable
    permission_classes = [IsAdminUser]
    queryset = Localidad.objects.all()
    serializer_class = LocalidadSerializer

class EnvioViewSet(viewsets.ReadOnlyModelViewSet):  #envio solo vista. Llenar antes de opciones.
    permission_classes = [AllowAny]
    queryset = Envio.objects.all()
    serializer_class = EnvioSerializer

class EnvioView(viewsets.ModelViewSet): #envio editable
    permission_classes = [IsAdminUser]
    queryset = Envio.objects.all()
    serializer_class = EnvioSerializer

#####################################################################
class CarritoViewSet(viewsets.ModelViewSet):    #carrito editable por usuario logueado
    permission_classes = [IsAuthenticated]
    queryset = Carrito.objects.all()
    serializer_class = CarritoSerializer

class CarritoAdmin(viewsets.ModelViewSet): #carrito editable
    permission_classes = [IsAdminUser]
    queryset = Carrito.objects.all()
    serializer_class = CarritoSerializer

class ElementosCarritoViewSet(viewsets.ModelViewSet):   #elementos carrito editable por usuario logueado
    permission_classes = [IsAuthenticated]
    queryset = ElementosCarrito.objects.all()
    serializer_class = ElementosCarritoSerializer

class ElementosCarritoAdmin(viewsets.ModelViewSet): #elementos carrito editable
    permission_classes = [IsAdminUser]
    queryset = ElementosCarrito.objects.all()
    serializer_class = ElementosCarritoSerializer

class ArticuloViewSet(viewsets.ReadOnlyModelViewSet):  #libro solo vista
    permission_classes = [AllowAny]
    queryset = Articulo.objects.all()
    serializer_class = ArticuloSerializer

class ArticuloAdmin(viewsets.ModelViewSet):    #libro editable
    permission_classes = [IsAdminUser]
    queryset = Articulo.objects.all()
    serializer_class = ArticuloSerializer

class CategoriaViewSet(viewsets.ReadOnlyModelViewSet):  #categoria solo vista
    permission_classes = [AllowAny]
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class CategoriaAdmin(viewsets.ModelViewSet):    #categoria editable
    permission_classes = [IsAdminUser]
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class DetallePedidoAdmin(viewsets.ModelViewSet):  #detalle editable
    permission_classes = [IsAdminUser]
    queryset = DetallePedido.objects.all()
    serializer_class = DetallePedidoSerializer

class DetallePedidoView(APIView):  #detalle editable por usuario logueado
    permission_classes = [IsAuthenticated]
    def post(self, request):
        detalles = request.data.get('detalles')
        serializer = DetallePedidoSerializer(data=detalles, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class PedidoAdmin(viewsets.ModelViewSet): #pedido editable
    permission_classes = [IsAdminUser]
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer

class PedidoViewSet(viewsets.ModelViewSet): #pedido editable por usuario logueado
    permission_classes = [IsAuthenticated]
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer

class OrdenAdmin(viewsets.ModelViewSet):    #orden editable
    permission_classes = [IsAdminUser]
    queryset = Orden.objects.all()
    serializer_class = OrdenSerializer

class OrdenViewSet(viewsets.ModelViewSet):  #orden editable por usuario logueado  
    permission_classes = [IsAuthenticated]
    queryset = Orden.objects.all()
    serializer_class = OrdenSerializer

class EstadoViewSet(viewsets.ReadOnlyModelViewSet): #estado solo vista. Llenar los estados antes
    permission_classes = [IsAuthenticated]
    queryset = Estado.objects.all()
    serializer_class = EstadoSerializer

class EstadoAdmin(viewsets.ModelViewSet):   #estado editable
    permission_classes = [IsAdminUser]
    queryset = Estado.objects.all()
    serializer_class = EstadoSerializer

class ModoPagoAdmin(viewsets.ModelViewSet): #modopago editable por usuario logueado
    permission_classes = [IsAdminUser]
    queryset = ModoPago.objects.all()
    serializer_class = ModoPagoSerializer

class ModoPagoViewSet(viewsets.ModelViewSet):   #modopago editable
    permission_classes = [IsAuthenticated]
    queryset = ModoPago.objects.all()
    serializer_class = ModoPagoSerializer

