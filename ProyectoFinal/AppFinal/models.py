from django.db import models

class Personal(models.Model):
    nombres=models.CharField(max_length=40)
    apellidos=models.CharField(max_length=40)
    edad=models.IntegerField()
    nacionalidad=models.CharField(max_length=40)
    correo=models.CharField(max_length=100)

class Estudios(models.Model):
    carrera=models.CharField(max_length=100)
    universidad=models.CharField(max_length=100)
    idiomas=models.CharField(max_length=40)
    correo=models.CharField(max_length=100)

class Experiencia(models.Model):
    trabajos_anteriores=models.CharField(max_length=2000)
    años_experiencia=models.IntegerField()
    correo=models.CharField(max_length=100)