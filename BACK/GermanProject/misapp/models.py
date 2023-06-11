from django.db import models



class ROL (models.Model):
    idrol= models.AutoField(primary_key=True)
    rol= models.CharField(max_length=20, blank=False)
    class Meta:
        db_table = "ROL"
        verbase_name = "rol"
        verbase_name_plural= "roles"
    def __unicode__(self):
        return self.rol
    def __str__(self):
        return self.rol

class USUARIOS(models.Model):
    id_usuario = models.AutoField (primary_key=True)
    nombre = models.CharField(max_length=20, blank=False)
    apellido = models.CharField(max_length=20, blank=False)
    email = models.CharField(max_length=50, blank=False)
    contraseña = models.IntegerField(max_length=6, blank=False)
    idrol = models.ForeignKey (ROL, to_field= 'idrol', on_delete=models.CASCADE)
    class Meta:
        db_table = "USUARIOS"
        verbase_name = "usuario"
        verbase_name_plural= "usuarios"
    def __unicode__(self):
        return self.nombre
    def __str__(self):
        return self.nombre
    


# Create your models here.
