from django.db import models
from datetime import datetime
from django.utils import timezone
from django.contrib.auth.models import AbstractUser, BaseUserManager
now = timezone.now()

class CustomUserManager(BaseUserManager):
    """
    Gestor de modelos de usuario personalizado donde el correo electrónico es el identificador único
    para la autenticación en lugar de los nombres de usuario.
    """
    def create_user(self, email, password, **extra_fields):
        """
        Crear y guardar un usuario con el correo electrónico y la contraseña dados.
        """
        if not email:
            raise ValueError(_("The Email must be set"))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Crea y guarda un SuperUsuario con el email y contraseña dados.
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))
        return self.create_user(email, password, **extra_fields)
    

#realiza el handle del login e interactua con la DB
class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(("email address"), unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
    

class ROL (models.Model):
    idrol= models.AutoField(primary_key=True)
    detalle= models.CharField(max_length=20, default="detalle",blank=False)

    class meta:
        db_table = "Roles"
        verbase_name = "rol"
        verbase_name_plural= "roles"
    
    def __str__(self):
        return self.detalle

class estados (models.Model):
    idestados=models.AutoField(primary_key=True, blank=False)
    detalle=models.CharField(max_length=20, blank=False)
# Aca se agregaran los diferentes estados de todas las tablas 1. enviado, 2. pendiente, 3. cancelado, 4. alta, 5. baja
    class meta:
        db_table="Estados"
        verbase_name= "estado"
        verbase_name_plural="estados"

    def __str__(self):
        return self.idestados + self.detalle

class USUARIOS(models.Model):
    id_usuario = models.AutoField (primary_key=True, blank=False)
    nombre = models.CharField(max_length=20, blank=False)
    tipo_dni= models.CharField(max_length=10, blank=False)
    numero_dni= models.IntegerField(blank=False)
    direccion= models.TextField(max_length=100, default="direccion",blank=False)
    telefono= models.IntegerField(blank=False)
    email = models.CharField(max_length=50, blank=False)
    contraseña = models.IntegerField(blank=False)
    idrol = models.ForeignKey (ROL, to_field= 'idrol', on_delete=models.CASCADE)
    idestados=models.ForeignKey(estados, to_field="idestados", on_delete=models.CASCADE)
    class meta:
        db_table = "Usuarios"
        verbase_name = "usuario"
        verbase_name_plural= "usuarios"
    
    def __str__(self):
        return self.nombre

class Proveedores (models.Model):
    idproveedor=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=100, blank=False)
    tipodni=models.CharField(max_length=10)
    numerodni=models.IntegerField( blank=False)
    direccion=models.TextField(max_length=100)
    telefono=models.IntegerField(blank=False)
    email=models.CharField(max_length=50, blank=False)
    
    class meta:
        db_table = "Proveedores"
        verbase_name = "proveedor"
        verbase_name_plural= "proveedores"
    
    def __str__(self):
        return self.nombre
    
class Ingreso(models.Model):
    idingreso=models.AutoField(primary_key=True, blank=False)
    idproveedor=models.ForeignKey(Proveedores, to_field="idproveedor", on_delete=models.CASCADE)
    tipoComprobante= models.CharField(max_length=20, blank=False)
    serieComprobante= models.CharField(max_length=10, blank=False)
    numeroComprobante= models.IntegerField(blank=False, default=0)
    fecha = models.DateTimeField(default=timezone.now)
    total=models.DecimalField(max_digits=10, decimal_places=2, blank=False)
    estado=models.ForeignKey(estados, to_field="idestados", on_delete=models.CASCADE)

    class meta:
        db_table = "Ingresos"
        verbase_name = "Ingreso"
        verbase_name_plural= "ingresos"
    
    def __str__(self):
        return self.idingreso + self.total
     
class Orden(models.Model):
    idorden=models.AutoField(primary_key=True, blank=False)
    usuario=models.ForeignKey(USUARIOS, to_field="id_usuario", on_delete=models.CASCADE)
    tipoComprobante= models.CharField(max_length=20, blank=False)
    serieComprobante= models.CharField(max_length=10, blank=False)
    numeroComprobante= models.IntegerField(blank=False, default=0)
    fecha = models.DateTimeField(default=timezone.now)
    impuesto=models.DecimalField (max_digits=10, decimal_places=2, blank=False)
    total=models.DecimalField(max_digits=10, decimal_places=2, blank=False)
    estado= models.ForeignKey(estados, to_field="idestados", on_delete=models.CASCADE)

    class meta:
        db_table="Orden"
        verbase_name= "Orden"
        verbase_name_plural="Ordenes"

    def __str__(self):
        return self.nombre

class Categoria(models.Model):
    idcategoria = models.AutoField(primary_key=True, blank=False)
    nombre = models.CharField(max_length=50, blank=False)
    descripcion=models.TextField()
    
    class meta:
        db_table="Categoria"
        verbase_name= "categoria"
        verbase_name_plural="categorias"

    def __str__(self):
        return self.nombre

class Envio(models.Model):
    idenvio=models.AutoField(primary_key=True, blank=False)
    descripcion=models.TextField()
    direccion_envio=models.CharField(max_length=100, blank=False)
    fecha = models.DateTimeField(default=timezone.now)
    cod_seguimiento=models.IntegerField(default=0)
    orden=models.ForeignKey(Orden, to_field="idorden", on_delete=models.CASCADE)
    estado=models.ForeignKey(estados, to_field="idestados", on_delete=models.CASCADE)

    class meta:
        db_table="Envio"
        verbase_name= "envio"
        verbase_name_plural="envios"

    def __str__(self):
        return self.idenvio + self.orden

class Articulos(models.Model):
    idarticulo= models.AutoField(primary_key=True, blank=False)
    nombre= models.CharField(max_length=50, blank=False)
    descripcion= models.TextField(max_length=100)
    precio= models.DecimalField(max_digits=10, blank=False, decimal_places=2, max_length=10)
    stock= models.IntegerField(blank=False, default=0)
    imagen= models.CharField(max_length=200)
    precio= models.DecimalField(max_digits=10 ,decimal_places=2, blank=False )
    idcategoria=models.ForeignKey(Categoria, to_field="idcategoria", on_delete=models.CASCADE)

    class meta:
        db_table="Articulos"
        verbase_name= "Articulo"
        verbase_name_plural="Articulos"

    def __str__(self):
        return self.nombre

class detalleVenta(models.Model):
    iddetalle=models.AutoField(primary_key=True, blank=False)
    cantidad=models.IntegerField(blank=False)
    precio= models.DecimalField(max_digits=10, decimal_places=2, blank=False )
    descuento=models.DecimalField(max_digits=10, decimal_places=2, blank=False )
    articulo=models.ForeignKey(Articulos, to_field="idarticulo", on_delete=models.CASCADE)
    orden= models.ForeignKey(Orden, to_field="idorden", on_delete=models.CASCADE)

    class meta:
        db_table="DetallesVenta"
        verbase_name= "detalle_venta"
        verbase_name_plural="detalles_ventas"

    def __str__(self):
        return self.iddetalle
    
class detalleingreso(models.Model):
    iddetalle=models.AutoField(primary_key=True, blank=False)
    cantidad=models.IntegerField(max_length=20, blank=False)
    descripcion= models.TextField()
    
    class meta:
        db_table="DetalleIngresos"
        verbase_name= "Detalle_Ingreso"
        verbase_name_plural="DetallesdeIngresos"

    def __str__(self):
        return self.iddetalle

