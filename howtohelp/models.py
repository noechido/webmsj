from django.db import models
from datetime import datetime as dt
from cloudinary.models import CloudinaryField


# Create your models here.
class HelpMethod(models.Model):
    nombre = models.CharField(max_length=255, unique=True)
    imagen = CloudinaryField('method')

    # Return the title of the announcement
    def __str__(self):
        return self.nombre

    # Class to change super Class attributes
    class Meta:
        # Change verbose names to spanish language
        verbose_name = "Método de Ayuda"
        verbose_name_plural = "Métodos de Ayuda"


class MonetaryInfo(models.Model):
    nombre = models.CharField(max_length=255, unique=True)
    imagen = CloudinaryField('monetaryInfo')
    nombre_cuenta = models.CharField(max_length=500, unique=True)
    numero_cuenta = models.CharField(max_length=255, unique=True)
    clabe_cuenta = models.CharField(max_length=255, unique=True)
    sucursal_cuenta= models.CharField(max_length=255, unique=True)

    # Return the title of the announcement
    def __str__(self):
        return self.nombre

    # Class to change super Class attributes
    class Meta:
        # Change verbose names to spanish language
        verbose_name = "Información Monetaria"
        verbose_name_plural = "Información Monetaria"


class Site(models.Model):
    nombre = models.CharField(max_length=255, unique=True, default=str(dt.now()))
    descripcion = models.CharField(max_length=1000, unique=True, default="Formas de ayudar a la institución.")
    imagen = CloudinaryField('site')

    def __str__(self):
        return self.nombre

    # Class to change super Class attributes
    class Meta:
        # Change verbose names to spanish language
        verbose_name= "Sitio"
        verbose_name_plural = "Sitio"
