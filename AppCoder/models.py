from django.db import models

# Create your models here.


class Curso(models.Model):

    nombre = models.CharField(max_length=40)
    camada = models.IntegerField()

    def __str__(self):
        return f"Nombre: {self.nombre}    Camada: {self.camada}"
    

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

    
class Alumno(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    fecha_nacimiento = models.DateField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    
class Profesor(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    especialidad = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

    
class Entregable(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_de_entrega = models.DateField()
    entregado = models.BooleanField(default=False)

    def __str__(self):
        return self.titulo