from django.db import models
from datetime import datetime


class Comentario(models.Model):
    # Campos
    nombre_usuario = models.CharField(max_length=50)
    fecha_comentario = models.DateField(default = None)
    ingreso_comentario = models.TextField(max_length=2000, help_text="Puedes ingresar un comentario hasta 2000 caracteres")

    # Métodos
    def __str__(self):
        return f'{self.nombre_usuario} - {self.fecha_comentario} - {self.ingreso_comentario}'

class Categoria(models.Model):
    # Campos
    nombre_categoria = models.CharField(max_length=50)
    descripcion_categoria = models.CharField(max_length=100)

    # Métodos
    def __str__(self):
        return f'{self.nombre_categoria} - {self.descripcion_categoria}'
