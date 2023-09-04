from django.db import models
from datetime import datetime as dt
from cloudinary.models import CloudinaryField


# Create your models here.
class Images(models.Model):
    nombre = models.CharField(max_length=255, unique=True, default=str(dt.now()))
    path = CloudinaryField('image')

    # Function to return the name of the Image
    def __str__(self):
        return self.nombre
    # Class to change super Class attributes

    class Meta:
        # Change verbose names to spanish language
        verbose_name = "Slide de Imágen"
        verbose_name_plural = "Slides de Imágenes"


# Table Video
# Create a model to save the video of the index
class Video(models.Model):
    # Declare variables for table Video
    url = models.CharField(max_length=255, unique=True, null=False)

    # Return the title of the announcement
    def __str__(self):
        return self.url

    # Class to change super Class attributes
    class Meta:
        # Change verbose names to spanish language
        verbose_name = "Video"
        verbose_name_plural = "Videos"


class AboutUs(models.Model):
    # Declare variables for table AboutUs
    nombre = models.CharField(max_length=255, unique=True, default=str(dt.now()))
    textoA = models.CharField(max_length=255, unique=True)
    imagenA = CloudinaryField('imageA')
    textoB = models.CharField(max_length=255, unique=True)
    imagenB = CloudinaryField('imageB')
    textoC = models.CharField(max_length=255, unique=True)
    imagenC = CloudinaryField('imageC')

    # Return the title of the announcement
    def __str__(self):
        return self.nombre

    # Class to change super Class attributes
    class Meta:
        # Change verbose names to spanish language
        verbose_name ="Sobre Nosotros"
        verbose_name_plural = "Sobre Nosotros"


class Patrons(models.Model):
    nombre = models.CharField(max_length=255)
    imagen = CloudinaryField('patron')
    titulo = models.CharField(max_length=255)
    puesto = models.CharField(max_length=255)

    # Return the title of the announcement
    def __str__(self):
        return self.nombre

    # Class to change super Class attributes
    class Meta:
        # Change verbose names to spanish language
        verbose_name = "Patronato"
        verbose_name_plural = "Patrones"


class Directors(models.Model):
    nombre = models.CharField(max_length=255)
    imagen = CloudinaryField('patron')
    titulo = models.CharField(max_length=255)
    puesto = models.CharField(max_length=255)

    # Return the title of the announcement
    def __str__(self):
        return self.nombre

    # Class to change super Class attributes
    class Meta:
        # Change verbose names to spanish language
        verbose_name = "Director"
        verbose_name_plural = "Directores"


class Mision(models.Model):
    nombre = models.CharField(max_length=255, unique=True, default=str(dt.now()))
    mision = models.CharField(max_length=1000, unique=True)

    # Function to return the name of the Image
    def __str__(self):
        return self.nombre

    # Class to change super Class attributes
    class Meta:
        # Change verbose names to spanish language
        verbose_name = "Misión"
        verbose_name_plural = "Misión"


class Vision(models.Model):
    nombre = models.CharField(max_length=255, unique=True, default=str(dt.now()))
    vision = models.CharField(max_length=1000, unique=True)

    # Function to return the name of the Image
    def __str__(self):
        return self.nombre

    # Class to change super Class attributes
    class Meta:
        # Change verbose names to spanish language
        verbose_name = "Visión"
        verbose_name_plural = "Visión"


class Values(models.Model):
    nombre = models.CharField(max_length=255, unique=True, default=str(dt.now()))
    valor = models.CharField(max_length=255, unique=True)

    # Function to return the name of the Image
    def __str__(self):
        return self.nombre

    # Class to change super Class attributes
    class Meta:
        # Change verbose names to spanish language
        verbose_name ="Valor"
        verbose_name_plural = "Valores"
