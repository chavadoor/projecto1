from django.db import models
from django_resized import ResizedImageField
from django.core.urlresolvers import reverse

# Create your models here.
class Sucursal(models.Model):
    sucursal = models.CharField(primary_key=True, max_length=100)

    def __str__(self):
        return self.sucursal

class Instructor (models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    sucursal = models.ForeignKey('Sucursal')
    telefono = models.CharField(max_length=10)
    correo = models.EmailField(max_length=100)
    foto = ResizedImageField(size=[450, 350], crop=['middle', 'center'], upload_to='media/img')


    def __str__(self):
        return self.nombre


class Sexo(models.Model):
    genero = models.CharField(max_length=20)

    def __str__(self):
        return self.genero

class Rutina (models.Model):
    nombre = models.CharField(max_length=100)
    instructor = models.ForeignKey('Instructor')
    sexo = models.ForeignKey('Sexo')
    tipo = models.CharField(max_length=20)
    descripcion = models.TextField()
    rutina = models.FileField(upload_to='files/pdf')

    def __str__(self):
        return self.nombre

