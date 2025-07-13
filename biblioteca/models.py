from django.db import models
from .validators import validar_isbn, validar_fecha_publicacion, validar_estado, validar_fecha_devolucion, validar_fecha_prestamo
from django.core.exceptions import ValidationError
from datetime import datetime

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    nacionalidad = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    isbn = models.CharField(max_length=13, unique=True, validators=[validar_isbn])
    fecha_publicacion = models.DateField(null=True, blank=True, validators=[validar_fecha_publicacion])
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    estado = models.BooleanField(default=True, validators=[validar_estado])
    
    def __str__(self):
        return self.titulo


class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    nacionalidad = models.CharField(max_length=100, blank=True)
    estado = models.BooleanField(default=True, validators=[validar_estado])
    
    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Prestamo(models.Model):
    fecha_prestamo = models.DateField(validators=[validar_fecha_prestamo])
    fecha_devolucion = models.DateField(null=True, blank=True, validators=[validar_fecha_devolucion])
    estado = models.BooleanField(default=True, validators=[validar_estado])
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.libro} - {self.usuario} - {self.fecha_prestamo} - {self.fecha_devolucion} - {self.estado}"

    
    
