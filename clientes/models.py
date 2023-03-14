from django.db import models

# Create your models here.

class cliente(models.Model):
    nombre = models.CharField(max_length=30)
    direccion=models.CharField(max_length=50)
    email=models.EmailField(max_length=30)
    telefono=models.CharField(max_length=20)