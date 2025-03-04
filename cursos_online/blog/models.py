from django.db import models

# Create your models here.
from django.db import models

# Modelo para el curso
class Curso(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha_publicacion = models.DateField()

    def __str__(self):
        return self.nombre

# Modelo para el instructor
class Instructor(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField()

    def __str__(self):
        return self.nombre

# Modelo para la categoría del curso
class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre