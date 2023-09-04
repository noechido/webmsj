from django.db import models
from datetime import datetime as dt
from cloudinary.models import CloudinaryField


# Create your models here.
class Report(models.Model):
    nombre = models.CharField(max_length=255, unique=True, default=str(dt.now()))
    reporte_url = models.CharField(max_length=1000, unique=True, default=None)

    # Return the title of the announcement
    def __str__(self):
        return self.nombre

    # Class to change super Class attributes
    class Meta:
        # Change verbose names to spanish language
        verbose_name = "Reporte"
        verbose_name_plural = "Reportes"


class Certification(models.Model):
    nombre = models.CharField(
        max_length=255, unique=True, default=str(dt.now()))
    nombre_certificacion = models.CharField(
        max_length=255, unique=True, default=str(dt.now()))
    imagen = CloudinaryField('certificacion', default=None, null=True)

    # Return the title of the announcement
    def __str__(self):
        return self.nombre

    # Class to change super Class attributes
    class Meta:
        # Change verbose names to spanish language
        verbose_name = "Certificación"
        verbose_name_plural = "Certificaciones"


class Other(models.Model):
    nombre = models.CharField(
        max_length=255, unique=True, default=str(dt.now()))
    nombre_otro = models.CharField(
        max_length=255, unique=True, default=str(dt.now()))
    imagen = CloudinaryField('other', default=None, null=True)

    # Return the title of the announcement
    def __str__(self):
        return self.nombre

    # Class to change super Class attributes
    class Meta:
        # Change verbose names to spanish language
        verbose_name = "Otro"
        verbose_name_plural = "Otros"

class Site(models.Model):
    nombre = models.CharField(max_length=255, unique=True, default=str(dt.now()))
    descripcion = models.CharField(max_length=1000, unique=True, default="Reportes de la institución.")
    imagen = CloudinaryField('site')

    def __str__(self):
        return self.nombre

    # Class to change super Class attributes
    class Meta:
        # Change verbose names to spanish language
        verbose_name= "Sitio"
        verbose_name_plural = "Sitio"

