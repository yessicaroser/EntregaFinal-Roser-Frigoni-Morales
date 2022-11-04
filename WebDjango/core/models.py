from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.conf import settings

category =[
    [0, "Python"],
    [1, "Javascript"],
    [2, "Ruby"]
] 

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	image = models.ImageField(default='coderhouse.jpg')

	def __str__(self):
		return f'Perfil de {self.user.username}'

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    timestamp = models.DateTimeField(default=timezone.now)
    content = models.TextField()
    categories = models.IntegerField(choices= category)
    #category = models.ForeignKey(Category, on_delete =models.PROTECT)
    class Meta:
        ordering = ['-timestamp']
    def __str__(self):
        return f'{self.user.username}: {self.content}'

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
