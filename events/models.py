from django.db import models
from datetime import datetime as dt
from cloudinary.models import CloudinaryField


# Create your models here.
class Event(models.Model):
    nombre = models.CharField(max_length=255, unique=True, default=str(dt.now()))
    fecha = models.DateField(default=dt.now())
    imagen = CloudinaryField('event')
    rotar_imagen = models.BooleanField(default=False)
    descripcion = models.CharField(max_length=1000, unique=True)
    lugar = models.CharField(max_length=255, null=True)

    # Return the title of the announcement
    def __str__(self):
        return self.nombre

    # Class to change super Class attributes
    class Meta:
        # Change verbose names to spanish language
        verbose_name = "Evento"
        verbose_name_plural = "Eventos"


# Create your models here.
class Notice(models.Model):
    nombre = models.CharField(max_length=255, unique=True, default=str(dt.now()))
    fecha = models.DateField(default=dt.now())
    imagen = CloudinaryField('notice')
    rotar_imagen = models.BooleanField(default=False)
    descripcion = models.CharField(max_length=1000, unique=True)
    lugar = models.CharField(max_length=255, null=True)

    # Return the title of the announcement
    def __str__(self):
        return self.nombre

    # Class to change super Class attributes
    class Meta:
        # Change verbose names to spanish language
        verbose_name = "Noticia"
        verbose_name_plural = "Noticias"


class Site(models.Model):
    nombre = models.CharField(max_length=255, unique=True, default=str(dt.now()))
    descripcion = models.CharField(max_length=1000, unique=True, default="Noticias y eventos de la institución.")
    imagen = CloudinaryField('site')

    def __str__(self):
        return self.nombre

    # Class to change super Class attributes
    class Meta:
        # Change verbose names to spanish language
        verbose_name= "Sitio"
        verbose_name_plural = "Sitio"
