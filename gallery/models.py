from django.db import models
from datetime import datetime as dt
from cloudinary.models import CloudinaryField


# Create your models here.
class Images(models.Model):
    nombre = models.CharField(
        max_length=255, unique=True, default=str(dt.now()))
    path = CloudinaryField('image')

    # Function to return the name of the Image
    def __str__(self):
        return self.nombre
    # Class to change super Class attributes

    class Meta:
        # Change verbose names to spanish language
        verbose_name = "Imagen"
        verbose_name_plural = "Imagenes"


class Category(models.Model):
    nombre = models.CharField(
        max_length=255, unique=True, default=str(dt.now()))
    nombre_categoria = models.CharField(
        max_length=255, unique=True, default=str(dt.now()))

    # Function to return the name of the Image
    def __str__(self):
        return self.nombre
    # Class to change super Class attributes

    class Meta:
        # Change verbose names to spanish language
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"


class Year(models.Model):
    anio = models.CharField(
        max_length=255, unique=True, default="2020")
    imagen_tarjeta = CloudinaryField('tarjeta', default=None)
    categorias = models.ManyToManyField(Category)
    imagenes = models.ManyToManyField(Images)
    # Function to return the name of the Image

    def __str__(self):
        return self.anio
    # Class to change super Class attributes

    class Meta:
        # Change verbose names to spanish language
        verbose_name = "Año"
        verbose_name_plural = "Años"


class Site(models.Model):
    nombre = models.CharField(max_length=255, unique=True, default=str(dt.now()))
    descripcion = models.CharField(max_length=1000, unique=True, default="Galería de imagenes de la institución.")
    imagen = CloudinaryField('image')

    def __str__(self):
        return self.nombre

    # Class to change super Class attributes
    class Meta:
        # Change verbose names to spanish language
        verbose_name = "Sitio"
        verbose_name_plural = "Sitio"
