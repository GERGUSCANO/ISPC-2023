from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class ROL(models.Model):
    idrol = models.AutoField(primary_key=True)
    detalle = models.CharField(max_length=20, default="detalle", blank=False)

    class Meta:
        db_table = "Roles"
        verbose_name = "rol"
        verbose_name_plural = "roles"

    def __str__(self):
        return self.detalle


class Estado(models.Model):
    idestado = models.IntegerField(primary_key=True, blank=False)
    detalle = models.CharField(max_length=20, blank=False)

    class Meta:
        db_table = "Estados"
        verbose_name = "estado"
        verbose_name_plural = "estados"

    def __str__(self):
        return f"{self.idestado} - {self.detalle}"


class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True, blank=False)
    nombre = models.CharField(max_length=20, blank=False)
    tipo_dni = models.CharField(max_length=10, blank=False)
    numero_dni = models.IntegerField(blank=False)
    direccion = models.TextField(max_length=100, default="direccion", blank=False)
    telefono = models.IntegerField()
    email = models.CharField(max_length=50, blank=False)
    contraseña = models.IntegerField(blank=False)
    id_rol = models.ForeignKey(ROL, to_field='idrol', on_delete=models.CASCADE)
    id_estado = models.ForeignKey(Estado, to_field='idestado', on_delete=models.CASCADE)

    class Meta:
        db_table = "Usuarios"
        verbose_name = "usuario"
        verbose_name_plural = "usuarios"

    def __str__(self):
        return self.nombre


class Proveedor(models.Model):
    idproveedor = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=100, blank=False)
    tipo_dni = models.CharField(max_length=10)
    numero_dni = models.IntegerField(blank=False)
    direccion = models.TextField(max_length=100)
    telefono = models.IntegerField(blank=False)
    email = models.CharField(max_length=50, blank=False)

    class Meta:
        db_table = "Proveedores"
        verbose_name = "proveedor"
        verbose_name_plural = "proveedores"

    def __str__(self):
        return self.nombre


class Ingreso(models.Model):
    idingreso = models.IntegerField(primary_key=True, blank=False)
    idproveedor = models.ForeignKey(Proveedor, to_field="idproveedor", on_delete=models.CASCADE)
    tipoComprobante = models.CharField(max_length=20, blank=False)
    serieComprobante = models.CharField(max_length=10, blank=False)
    numeroComprobante = models.IntegerField(default=0)
    fecha = models.DateTimeField(default=timezone.now)
    total = models.DecimalField(max_digits=10, decimal_places=2, blank=False)
    estado = models.ForeignKey(Estado, to_field="idestado", on_delete=models.CASCADE)

    class Meta:
        db_table = "Ingresos"
        verbose_name = "ingreso"
        verbose_name_plural = "ingresos"

    def __str__(self):
        return f"{self.idingreso} - {self.total}"


class Orden(models.Model):
    idorden = models.IntegerField(primary_key=True, blank=False)
    usuario = models.ForeignKey(Usuario, to_field="id_usuario", on_delete=models.CASCADE)
    tipoComprobante = models.CharField(max_length=20, blank=False)
    serieComprobante = models.CharField(max_length=10, blank=False)
    numeroComprobante = models.IntegerField(default=0)
    fecha = models.DateTimeField(default=timezone.now)
    impuesto = models.DecimalField(max_digits=10, decimal_places=2, blank=False)
    total = models.DecimalField(max_digits=10, decimal_places=2, blank=False)
    estado = models.ForeignKey(Estado, to_field="idestado", on_delete=models.CASCADE)

    class Meta:
        db_table = "Orden"
        verbose_name = "orden"
        verbose_name_plural = "ordenes"

    def __str__(self):
        return str(self.idorden)


class Categoria(models.Model):
    idcategoria = models.IntegerField(primary_key=True, blank=False)
    nombre = models.CharField(max_length=50, blank=False)
    descripcion = models.TextField()

    class Meta:
        db_table = "Categoria"
        verbose_name = "categoria"
        verbose_name_plural = "categorias"

    def __str__(self):
        return self.nombre


class Envio(models.Model):
    idenvio = models.IntegerField(primary_key=True, blank=False)
    descripcion = models.TextField()
    direccion_envio = models.CharField(max_length=100, blank=False)
    fecha = models.DateTimeField(default=timezone.now)
    cod_seguimiento = models.IntegerField(default=0)
    orden = models.ForeignKey(Orden, to_field="idorden", on_delete=models.CASCADE)
    estado = models.ForeignKey(Estado, to_field="idestado", on_delete=models.CASCADE)

    class Meta:
        db_table = "Envio"
        verbose_name = "envio"
        verbose_name_plural = "envios"

    def __str__(self):
        return str(self.idenvio)


class Articulo(models.Model):
    idarticulo = models.IntegerField(primary_key=True, blank=False)
    nombre = models.CharField(max_length=50, blank=False)
    descripcion = models.TextField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2, blank=False)
    stock = models.IntegerField(default=0)
    imagen = models.CharField(max_length=200)
    categoria = models.ForeignKey(Categoria, to_field="idcategoria", on_delete=models.CASCADE)

    class Meta:
        db_table = "Articulos"
        verbose_name = "articulo"
        verbose_name_plural = "articulos"

    def __str__(self):
        return self.nombre


class ItemCarrito(models.Model):
    carrito = models.ForeignKey('Carrito', on_delete=models.CASCADE)
    articulo = models.ForeignKey(Articulo, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)

    class Meta:
        db_table = "ItemsCarrito"
        verbose_name = "item de carrito"
        verbose_name_plural = "items de carrito"

    def __str__(self):
        return f"Item de {self.articulo.nombre} en el carrito de {self.carrito.usuario.username}"


class Carrito(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    creado_en = models.DateTimeField(auto_now_add=True)
    actualizado_en = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "Carritos"
        verbose_name = "carrito"
        verbose_name_plural = "carritos"

    def __str__(self):
        return f"Carrito de {self.usuario.username}"

