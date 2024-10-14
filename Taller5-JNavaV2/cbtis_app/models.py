from django.db import models

# Create your models here.
class AlumnoT(models.Model):
    Apaterno=models.CharField(max_length=50,verbose_name="Apellido Paterno")
    Amaterno=models.CharField(max_length=50,verbose_name="Apellido Materno")
    Nombres=models.CharField(max_length=100,verbose_name="Nombre (s)")
    fecha_nacimiento=models.DateField(verbose_name="Fecha de nacimiento",null=False,blank=False)
    fecha_ingreso=models.DateField( verbose_name="Fecha ingreso",null=False,blank=False)