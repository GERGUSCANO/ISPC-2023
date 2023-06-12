from django.db import models


class ROL (models.Model):
    idrol= models.AutoField(primary_key=True)
    rol= models.CharField(max_length=20, blank=False)

    class meta:
        db_table = "ROL"
        verbase_name = "rol"
        verbase_name_plural= "roles"
    
    def __str__(self):
        return self.rol

class USUARIOS(models.Model):
    id_usuario = models.AutoField (primary_key=True)
    nombre = models.CharField(max_length=20, blank=False)
    apellido = models.CharField(max_length=20, blank=False)
    email = models.CharField(max_length=50, blank=False)
    contraseña = models.IntegerField(blank=False)
    idrol = models.ForeignKey (ROL, to_field= 'idrol', on_delete=models.CASCADE)

    class meta:
        db_table = "USUARIOS"
        verbase_name = "usuario"
        verbase_name_plural= "usuarios"
    
    def __str__(self):
        return self.nombre
    

class Categoria(models.Model):
    idcategoria = models.IntegerField(primary_key=True, blank=False)
    nombrecategoria = models.CharField(max_length=50, blank=False)

    class meta:
        db_table="CATEGORIAS"
        verbase_name= "categoria"
        verbase_name_plural="categorias"

    def __str__(self):
        return self.nombrecategoria
    
class Producto(models.Model):
    idproducto= models.IntegerField(primary_key=True, blank=False)
    nombreProducto= models.CharField(max_length=50, blank=False)
    descripcion= models.TextField(max_length=100)
    precio= models.DecimalField(max_digits=10, blank=False, decimal_places=2, max_length=10)
    stock= models.IntegerField(blank=False, default=0)
    imagen= models.CharField(max_length=200)
    idcategoria=models.ForeignKey(Categoria, to_field="idcategoria", on_delete=models.CASCADE)

    class meta:
        db_table="Productos"
        verbase_name= "producto"
        verbase_name_plural="productos"

    def __str__(self):
        return self.nombreProducto 
    
class metadoPago (models.Model):
    idmetodoPago=models.IntegerField(primary_key=True, blank=False)
    metodopago=models.CharField(max_length=50, blank=False)

    class meta:
        db_table="metodopago"
        verbase_name= "metodopago"
        verbase_name_plural="metodospagos"

    def __str__(self):
        return self.metodopago
    

class estados (models.Model):
    idestados=models.IntegerField(primary_key=True, blank=False)
    descripcion=models.CharField(max_length=20, blank=False)
# Aca se agregaran los diferentes estados de todas las tablas 1. enviado, 2. pendiente, 3. cancelado, 4. alta, 5. baja
    class meta:
        db_table="estados"
        verbase_name= "estado"
        verbase_name_plural="estados"

    def __str__(self):
        return self.idestados + self.descripcion


class Pagos(models.Model):
    idpago=models.IntegerField(primary_key=True, blank=False)
    idmetodoPago=models.ForeignKey(metadoPago,to_field="idmetodoPago", on_delete=models.CASCADE)
    fechaPedido= models.DateField(auto_created=True)
    idestados= models.ForeignKey(estados, to_field="idestados", on_delete=models.CASCADE)

    class meta:
        db_table="pagos"
        verbase_name= "pago"
        verbase_name_plural="pagos"

    def __str__(self):
        return self.idpago + self.idestados + self.fechaPedido
    
class cliente(models.Model):
    idcliente=models.IntegerField(primary_key=True, blank=False)
    idusuario= models.ForeignKey(USUARIOS, to_field="id_usuario", on_delete=models.CASCADE)

    class meta:
        db_table="cliente"
        verbase_name= "cliente"
        verbase_name_plural="clientes"

    def __str__(self):
        return self.idusuario.nombre + self.idusuario.apellido 

class direccion (models.Model):
    iddireccion= models.IntegerField(primary_key=True, blank=False)
    idcliente=models.ForeignKey(cliente, to_field="idcliente", on_delete=models.CASCADE)
    calle=models.TextField()
    numero=models.IntegerField()
    barrio=models.TextField()
    localidad=models.CharField()
    
    class meta:
        db_table="direccion"
        verbase_name= "direccion"
        verbase_name_plural="direccion"

    def __str__(self):
        return self.idcliente 