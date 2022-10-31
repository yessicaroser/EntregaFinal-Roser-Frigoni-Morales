from django.db import models
from datetime import datetime


# Create your models here.

class Comentario(models.Model):
    nombre_usuario = models.CharField(max_length=50)
    fecha_comentario = models.DateField(default = None)
    ingreso_comentario = models.TextField(max_length=1000)