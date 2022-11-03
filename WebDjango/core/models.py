from django.db import models
from datetime import datetime


# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.nombre

class Publicacion(models.Model):

    titulo = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=200)
    contenido = models.CharField(max_length=200)
    fecha_publicacion = models.DateField()
    hashtag = models.CharField(max_length=200)
    autor = models.CharField(max_length=200)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.titulo


class Comentario(models.Model):
    # Campos
    users = models.CharField(max_length=50)
    publicacion_comentario = models.ForeignKey(Publicacion, on_delete=models.CASCADE)
    fecha_comentario = models.DateField()
    ingreso_comentario = models.CharField(max_length=200)

    # Métodos
    def __str__(self): 
        return f'{self.users} - {self.fecha_comentario} - {self.publicacion_comentario} - {self.ingreso_comentario}'

