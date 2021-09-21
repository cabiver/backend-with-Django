from django.db import models

class Student(models.Model):
    nombre = models.CharField(max_length=150)
    apellidos = models.CharField(max_length=150)
    edad = models.IntegerField()
    email = models.EmailField()
# Create your models here.
