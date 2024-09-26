
from django.db import models
from datetime import datetime

# Create your models here.
## con el comando python magane.py makemigrations creo el metodo de migracion

class Curso(models.Model):
    nombre=models.CharField(max_length=50)
    camada=models.IntegerField()
    
class Estudiante(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    email=models.EmailField (max_length=254)
    
    
class Profesor(models.Model):
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    email=models.EmailField()
    profesion=models.CharField(max_length=30)
    
class Entregable(models.Model):
    nombre=models.CharField(max_length=30)
    fechaDeEntrega=models.DateField()
    entregado=models.BooleanField()
    