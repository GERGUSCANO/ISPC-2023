from django.db import models

from django.conf import settings
from django.utils.translation import gettext_lazy as _
from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime

class CustomUser(AbstractUser):

    email = models.EmailField(
        max_length=150,
        unique=True
    )   
    dni = models.CharField(
        max_length=8,
        help_text='Maximo 8 caracteres',
        null=True
        )
    fecha_nac = models.DateField(
        null=True
        )
    telefono = models.CharField(
        max_length=12,
        help_text='Maximo 12 caracteres',
        null=True
        )
    id_direccion = models.ForeignKey(
        'Direccion',
        to_field='id_direccion',
        on_delete=models.CASCADE,
        null=True
        )
    id_carrito = models.ForeignKey(
        'Carrito',
        on_delete=models.SET_NULL,
        null=True,
        related_name='customuser'
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'password']

class Provincia(models.Model):

    class Provincias(models.TextChoices):
        BUENOS_AIRES = 'BA',
        CATAMARCA = 'CT',
        CHACO = 'CH',
        CHUBUT = 'CB',
        CORDOBA = 'CD',
        CORRIENTES = 'CR',
        ENTRE_RIOS = 'ER',
        FORMOSA = 'FO',
        JUJUY = 'JY',
        LA_PAMPA = 'LP',
        LA_RIOJA = 'LR',
        MENDOZA = 'MZ',
        MISIONES = 'MN',
        NEUQUEN = 'NQ',
        RIO_NEGRO = 'RN',
        SALTA = 'SA',
        SAN_JUAN = 'SJ',
        SAN_LUIS = 'SL',
        SANTA_CRUZ = 'SC',
        SANTA_FE = 'SF',
        SANTIAGO_DEL_ESTERO = 'SE',
        TIERRA_DEL_FUEGO = 'TF',
        TUCUMAN = 'TM'

    id_provincia = models.AutoField(
        primary_key=True,
        unique=True,
        db_index=True
        )
    nombre = models.CharField(
        max_length=2,
        choices=Provincias.choices,
        default=Provincias.BUENOS_AIRES
        )

    class Meta:
        db_table = 'Provincia'
        verbose_name = ('Nombre de Provincia')
        verbose_name_plural = ('Nombres de Provincias')

    def __unicode__(self):
        return self.id_provincia
    
    def __str__(self):
        return self.nombre

class Localidad(models.Model):

    id_localidad = models.AutoField(
        primary_key=True,
        db_index=True
        )
    nombre = models.CharField(
        max_length=100,
        help_text='Maximo 100 caracteres'
        )
    codigo_postal = models.CharField(
        max_length=8,
        help_text='Codigo postal'
        )
    
    class Meta:
        db_table = 'Localidad'
        verbose_name = ('Nombre de Localidad')
        verbose_name_plural = ('Nombres de Localidades')

    def __unicode__(self):
        return self.id_localidad
    
    def __str__(self):
        return self.nombre

class Direccion(models.Model):

    id_direccion = models.AutoField(
        primary_key=True,
        db_index=True
        )
    calle= models.CharField(
        max_length=100,
        help_text='Calle')
    numero= models.CharField(
        max_length=100, 
        help_text='Numero')
    departamento= models.CharField(
        max_length=10, 
        help_text='Ingrese numero departamento')
    piso=models.CharField(
        max_length=10, 
        help_text='Ingrese el piso')
    barrio=models.CharField(
        max_length= 100, 
        help_text='Ingrese el barrio donde vive')
    id_provincia = models.ForeignKey(
        'Provincia',
        to_field='id_provincia', 
        null=False, 
        on_delete=models.CASCADE)
    id_localidad = models.ForeignKey(
        'Localidad', 
        to_field='id_localidad', 
        null=False, 
        on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'Direccion'
        verbose_name = ('Detalle Direccion')
        verbose_name_plural = ('Detalles de Direcciones')

    def __str__(self):
        return f' CALLE {self.calle} \
            numero {self.numero} \
            piso {self.piso}\
            departamento {self.departamento}\
            barrio {self.barrio}\
            '
    
    
class Estado(models.Model):
    class Estados(models.TextChoices):
        activo='1',
        desactivo='2',
        pendiente='3',
        aprobado='4',
        desaprobado='5',
        en_proceso='6',

    id_estado=models.AutoField(primary_key=True)
    detalle = models.CharField(max_length=2, choices=Estados.choices, default=Estados.activo)    

    class Meta:
        db_table = 'Estado'
        verbose_name = ('Estado')
        verbose_name_plural = ('Estados')

        def __unicode__(self):
           return self.id_estado
    
        def __str__(self):
           return f' Estado {self.get_estado_display()}'
        
class Envio(models.Model):
    id_envio=models.AutoField(primary_key=True)
    estado =models.ForeignKey(Estado, to_field='id_estado', on_delete=models.CASCADE)
    direccion = models.ForeignKey(Direccion, to_field='id_direccion', on_delete=models.CASCADE)
    fecha = models.DateTimeField(default=datetime.now)
    total = models.DecimalField(max_length=10, max_digits=10, decimal_places=2, help_text='Ingrese el valor del envio')
    class Meta:
        db_table = 'Envio'
        verbose_name = ('Envio')
        verbose_name_plural = ('Envios')

    def __str__(self):
        return f'ENVIO{self.id_envio} , ESTADO {self.estado}, FECHA{self.fecha}, TOTAL{self.total}'

"""class TipoUsuarios(models.Model):
    class Tipos(models.TextChoices):
        superadmin='Super Administrador',
        admin='Administrador',
        user='Usuarios',
    
    id_tipo=models.AutoField(primary_key=True)
    detalle = models.CharField(max_length=20, choices=Tipos.choices, default=Tipos.user)

    class Meta:
        db_table = 'tiposUsuarios'
        verbose_name = ('Tipo de Usuario')
        verbose_name_plural = ('Tipos de Usuarios')

    def __str__(self):
        return self.id_tipo, self.detalle
"""

"""class Cliente(models.Model):
    dni=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=50, help_text='Nombre completo', blank=False)
    apellido=models.CharField(max_length=20, help_text='Apellido', blank=False)
    tipo_dni=models.CharField(max_length=10, help_text='Ingrese tipo de identificacion')
    email= models.EmailField(max_length=100, help_text='Correo Electronico', blank=False)
    fecha_nac= models.DateField()
    telefono=  models.IntegerField(max_length=15, help_text='Telefono', blank=True) 
    tipo=models.ForeignKey(TipoUsuarios, to_field='id_tipo', on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'clientes'
        verbose_name = ('Cliente')
        verbose_name_plural = ('Clientes')

    def __str__(self):
        return self.dni, self.email
"""
class ModoPago(models.Model):
    class tiposPago(models.TextChoices):
        efectivo='EF',
        transferencia='TF',
        tarjeta='TJ',
        deposito='DP',
        class Electronico(models.TextChoices):
            mercadopago='MP',
            modo='MO',
            paypal='PY',
        pagoeletronico= models.CharField(choices=Electronico.choices, default=Electronico.mercadopago)

    id_mp=models.AutoField(primary_key=True)
    tipos=models.CharField(choices=tiposPago.choices, default=tiposPago.efectivo, max_length=100)
    detalle=models.TextField(max_length=200, help_text='Detalle', blank=True)
    fecha=models.DateField()
    monto=models.DecimalField(
        max_length=99999,
        decimal_places=2,
        max_digits=7)


    class Meta:
        db_table = 'modoPago'
        verbose_name = ('Modo de pago')
        verbose_name_plural = ('Modos de pagos')

    def __unicode__(self):
        return self.id_mp
    
    def __str__(self):
        return f'registrado {self.fecha} \
        monto {self.monto} \
        info {self.detalle}'

class Orden(models.Model):
    id_orden=models.AutoField(
        primary_key=True)
    pago=models.ForeignKey(
        ModoPago, 
        to_field='id_mp', 
        on_delete=models.CASCADE)
    estado=models.ForeignKey(
        Estado, 
        to_field='id_estado', 
        on_delete=models.CASCADE)
    id_cliente = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        to_field='id',
        on_delete=models.CASCADE)    
    fecha=models.DateField(
        auto_now=True)
    tipo_comprobante=models.CharField(
        max_length=20, 
        help_text='tipo comprobante')
    detalle_comprobante=models.CharField(
        max_length=30, 
        help_text='Numero de Comprobante')
    total = models.DecimalField(
        max_length=99999,
        decimal_places=2,
        max_digits=7
        )

    class Meta:
        db_table = 'orden'
        verbose_name = ('Orden')
        verbose_name_plural = ('Ordenes')

    def __unicode__(self):
        return self.id_orden
    
    def __str__(self):
        return f'nro de orden {self.id_orden} \
            estado {self.estado} \
            total {self.total}'
   
class Carrito(models.Model):

    id_carrito = models.AutoField(
        primary_key=True,
        unique=True,
        db_index=True
        )
    fecha_creacion = models.DateTimeField(
        auto_now=True,
        db_comment= 'The field is only automatically updated when calling Model.save()'
        )


    class Meta:
        db_table = 'carrito'
        verbose_name = ('Id del Carrito')
        verbose_name_plural = ('Ids de los Carritos')

    def __unicode__(self):
        return self.id_carrito
    
    def __str__(self):
        return self.id_carrito


class Categoria(models.Model):
    id_categoria: models.AutoField(
        primary_key=True,
        unique=True,
        db_index=True
        ) 
    nombre=models.CharField(max_length=100, help_text="Nombre del la categoria", blank=False)
    detalle=models.TextField(max_length=200, blank=True)

class Articulo(models.Model):

    id_articulo = models.AutoField(
        primary_key=True,
        unique=True,
        db_index=True
        )
    categoria=models.ForeignKey(Categoria, to_field='id', on_delete=models.CASCADE)
    nombre = models.CharField(
        max_length=200,
        help_text='Maximo 200 caracteres'
        )
    tipo_presentacion = models.CharField(
        max_length=200,
        help_text='Maximo 200 caracteres'
        )
    descripcion= models.CharField(
        max_length=1000,
        help_text='Maximo 1000 caracteres'
        )
    precio = models.DecimalField(
        max_digits=7,
        decimal_places=2
        )
    stock = models.PositiveSmallIntegerField(
        )
    img_url = models.URLField(
        max_length = 200,
        default='https://www.bayertecuida.es/sites/g/files/vrxlpx43471/files/2020-07/aspirina500mg-comprimidos_0.jpg'
    )
    
    class Meta:
        db_table = 'articulo'
        verbose_name = ('Articulo')
        verbose_name_plural = ('Articulos')

    def __unicode__(self):
        return self.id_articulo
    
    def __str__(self):
        return f'{self.nombre} \
            formato {self.tipo_presentacion} \
            descripcion {self.descripcion} \
            precio {self.precio} \
            stock {self.stock}'


class ElementosCarrito(models.Model):

    id_elementos_carrito = models.AutoField(
        primary_key=True,
        unique=True,
        db_index=True
        )
    id_carrito = models.ForeignKey(
        'Carrito',
        to_field='id_carrito',
        on_delete=models.CASCADE
        )
    id_cliente = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        to_field='id',
        on_delete=models.CASCADE
        )
    
    id_articulo= models.ForeignKey(
        Articulo, 
        to_field='id_articulo', 
        on_delete=models.CASCADE )
    
    cantidad = models.PositiveSmallIntegerField(
        )
   
    class Meta:
        db_table = 'elementos_carrito'
        verbose_name = ('Elemento del Carrito')
        verbose_name_plural = ('Elementos de los Carritos')

    def __unicode__(self):
        return self.id_elementos_carrito
    
    def __str__(self):
        return f'{self.cantidad} de \
            {self.id_articulo} perteneciente a \
            {self.id_carrito} de usuario \
            {self.id_cliente}'
    

class DetallePedido(models.Model):

    id_detalle_pedido = models.AutoField(
        primary_key=True,
        unique=True,
        db_index=True
        )
    cantidad = models.PositiveSmallIntegerField(
        )
    id_pedido = models.ForeignKey(
        'Pedido',
        to_field='id_pedido',
        on_delete=models.CASCADE
        )
    
    id_articulo = models.ForeignKey(
        'Articulo',
        to_field='id_articulo',
        on_delete=models.CASCADE
        )
    
    class Meta:
        db_table = 'detalle_pedido'
        verbose_name = ('Detalle del Pedido')
        verbose_name_plural = ('Detalles de los Pedidos')

    def __unicode__(self):
        return self.id_detalle_pedido
    
    def __str__(self):
        return f'nro de pedido {self.id_pedido} \
            contiene {self.cantidad} \
            de producto {self.id_articulo}'

class Pedido(models.Model):

    class Seguimientos(models.TextChoices):
            EN_CAMINO = 'CC',
            ARMANDO_PEDIDO = 'AA',
            ENTREGADO = 'EE',
            DEVOLUCION = 'DV'
            
    id_pedido = models.AutoField(
        primary_key=True,
        unique=True,
        db_index=True
        )
    seguimiento = models.CharField(
        max_length=2,
        choices=Seguimientos.choices,
        default=Seguimientos.ARMANDO_PEDIDO
        )
    id_cliente = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        to_field='id',
        on_delete=models.CASCADE
        )
    fecha = models.DateTimeField(
        #Create date of Invoice
        auto_now_add=True,
        db_comment= 'The field is only automatically updated when calling Model.save()'
        )
    id_orden = models.ForeignKey(
        'Orden',
        to_field='id_orden',
        on_delete=models.CASCADE
        )
    nro_tracking = models.CharField(
        max_length=40,
        help_text='Maximo 40 caracteres'
        )
    
    class Meta:
        db_table = 'pedido'
        verbose_name = ('Pedido')
        verbose_name_plural = ('Pedidos')

    def __unicode__(self):
        return self.id_pedido
    
    def __str__(self):
        return f'nro de pedido {self.id_pedido} \
            estado {self.seguimiento} \
            tracking {self.nro_tracking}'

"""class Orden(models.Model):

    id_orden = models.AutoField(
        primary_key=True,
        unique=True,
        db_index=True
        )
    fecha_creacion = models.DateTimeField(
        #Create date of Quote
        auto_now_add=True,
        db_comment= 'The field is only automatically updated when calling Model.save()'
        )
    total = models.DecimalField(
        max_length=99999,
        decimal_places=2,
        max_digits=7
        )
    id_cliente = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        to_field='id',
        on_delete=models.CASCADE
        )
    id_estado = models.ForeignKey(
        'Estado',
        to_field='id_estado',
        on_delete=models.CASCADE
        )
    
    class Meta:
        db_table = 'orden'
        verbose_name = ('Orden')
        verbose_name_plural = ('Ordenes')

    def __unicode__(self):
        return self.id_orden
    
    def __str__(self):
        return f'nro de orden {self.id_orden} \
            estado {self.id_estado} \
            total {self.total}'
"""    

"""class Estado(models.Model):

    class Estados(models.TextChoices):
            PAGADO = 'PP',
            RECHAZADO = 'RR',
            ESPERANDO_AUTORIZACION = 'AA'            
    
    id_estado = models.AutoField(
        primary_key=True,
        unique=True,
        db_index=True
        )
    estado = models.CharField(
        max_length=2,
        choices=Estados.choices,
        default=Estados.ESPERANDO_AUTORIZACION
        )
    
    class Meta:
        db_table = 'estado'
        verbose_name = ('Estado')
        verbose_name_plural = ('Estados')

    def __unicode__(self):
        return self.id_estado
    
    def __str__(self):
        return self.get_estado_display()

"""
"""class Pago(models.Model):

    id_pago = models.AutoField(
        primary_key=True,
        unique=True,
        db_index=True
        )
    
    fecha_pago = models.DateTimeField(
        #Create date of payment
        auto_now_add=True,
        db_comment= 'The field is only automatically updated when calling Model.save()'
        )
    monto = models.DecimalField(
        max_length=99999,
        decimal_places=2,
        max_digits=7
        )
        #Save last 4 digits of credit card, etc
    info_adicional = models.CharField(
        max_length=200,
        help_text='Maximo 200 caracteres'
        )
    
    id_orden = models.ForeignKey(
        'Orden',
        to_field='id_orden',
        on_delete=models.CASCADE
        )
    
    class Meta:
        db_table = 'pago'
        verbose_name = ('Pago')
        verbose_name_plural = ('Pagos')

    def __unicode__(self):
        return self.id_pago
    
    def __str__(self):
        return f'registrado {self.fecha_pago} \
        monto {self.monto} \
        info {self.info_adicional}'
    
"""
class Pagos(models.Model):

    id_pagos = models.AutoField(
        primary_key=True,
        unique=True,
        db_index=True
        )
    
    id_cliente = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        to_field='id',
        on_delete=models.CASCADE
        )
    
    fecha_pago = models.DateTimeField(
        #Create date of payment
        auto_now_add=True,
        db_comment= 'The field is only automatically updated when calling Model.save()'
        )
    
    code = models.CharField(
        max_length=200,
        help_text='Maximo 200 caracteres'
        )
    
    dni = models.CharField(
        max_length=200,
        help_text='Maximo 200 caracteres'
        )
    
    email = models.CharField(
        max_length=200,
        help_text='Maximo 200 caracteres'
        )
    
    tarjeta = models.CharField(
        max_length=200,
        help_text='Maximo 200 caracteres'
        )
    
    titular = models.CharField(
        max_length=200,
        help_text='Maximo 200 caracteres'
        )
    
    vencimiento = models.CharField(
        max_length=200,
        help_text='Maximo 200 caracteres'
        )

    class Meta:
        db_table = 'pagos'
        verbose_name = ('Pagos')
        verbose_name_plural = ('Datos generales de Pagos')

    def __unicode__(self):
        return self.id_pagos