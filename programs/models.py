from django.db import models
from datetime import datetime as dt
from cloudinary.models import CloudinaryField


# Create your models here.
class Data(models.Model):
    nombre = models.CharField(
        max_length=255, unique=True, default=str(dt.now()))
    nombre_dato = models.CharField(max_length=255, default=str(dt.now()))
    numero = models.IntegerField()

    def __str__(self):
        return self.nombre

    # Class to change super Class attributes
    class Meta:
        # Change verbose names to spanish language
        verbose_name= "Dato"
        verbose_name_plural = "Datos"

class DataCollection(models.Model):
    nombre = models.CharField(
        max_length=255, unique=True, default=str(dt.now()))
    titulo_datos = models.CharField(max_length=255, null=True, blank=True, default= None)
    datos = models.ManyToManyField(Data)

    def __str__(self):
        return self.nombre

    # Class to change super Class attributes
    class Meta:
        # Change verbose names to spanish language
        verbose_name= "Colección Datos"
        verbose_name_plural = "Colección Datos"



class Program(models.Model):
    nombre = models.CharField(max_length=255, unique=True)
    imagen = CloudinaryField('program')
    subtitulo = models.CharField(max_length=255, unique=True, null=True)
    descripcion = models.CharField(max_length=650, unique=True, null=True)
    colecciones_datos = models.ManyToManyField(DataCollection)

    def __str__(self):
        return self.nombre

    # Class to change super Class attributes
    class Meta:
        # Change verbose names to spanish language
        verbose_name: "Programa"
        verbose_name_plural = "Programas"


class Site(models.Model):
    nombre = models.CharField(max_length=255, unique=True, default=str(dt.now()))
    descripcion = models.CharField(max_length=1000, unique=True, default="Programas de la Institución.")
    imagen = CloudinaryField('site')

    def __str__(self):
        return self.nombre

    # Class to change super Class attributes
    class Meta:
        # Change verbose names to spanish language
        verbose_name= "Sitio"
        verbose_name_plural = "Sitio"





