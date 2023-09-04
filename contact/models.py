from django.db import models
from datetime import datetime as dt
from cloudinary.models import CloudinaryField

# Table Contacto
class Contact(models.Model):
    # Declare variables for table Contacto
    telefono = models.CharField(max_length=255, null=False)
    horario = models.CharField(max_length=255, null=False)
    mail = models.EmailField(null=False, unique=True)

    # Class to change super Class attributes
    class Meta:
        # Change verbose names to spanish language
        verbose_name = "Informacion de Contacto"
        verbose_name_plural = "Informacion de Contacto"


# Table Mensaje
class Message(models.Model):
    # Declare variables for table Mensaje
    nombre = models.CharField(max_length=255, null=False)
    correo = models.EmailField(null=False)
    mensaje = models.TextField(max_length=255, null=False)

    # Declare function to return the name of the user sending the message
    def __str__(self):
        return self.nombre

    # Class to change super Class attributes
    class Meta:
        # Change verbose names to spanish language
        verbose_name = "Mensaje"
        verbose_name_plural = "Mensajes"


class Site(models.Model):
    nombre = models.CharField(max_length=255, unique=True, default=str(dt.now()))
    descripcion = models.CharField(max_length=1000, unique=True, default="Contacto de la institución.")
    imagen = CloudinaryField('contact')

    def __str__(self):
        return self.nombre

    # Class to change super Class attributes
    class Meta:
        # Change verbose names to spanish language
        verbose_name = "Sitio"
        verbose_name_plural = "Sitio"
