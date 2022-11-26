from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib import auth
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField 


# Create your models here.
'''
class Users(auth.models.User, auth.models.PermissionsMixin):
    def __str__(self):
        return "@{}".format(self.username)
'''

class Post(models.Model):
    titulo = models.CharField(max_length=100)
    imagen_portada = models.ImageField(default='default.jpg', upload_to='images/', null=True, blank=True)
    contenido = RichTextField(blank=True, null=True)
    fecha_creacion = models.DateTimeField(default=timezone.now)
    fecha_publicacion = models.DateTimeField(blank=True, null=True)
    autor = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    avatar = models.ImageField(default='default.jpg', upload_to='avatars/', null=True)
    slug = models.CharField
    
    def publish(self):
        self.fecha_publicacion = timezone.now()
        self.save()

    def approve_comments(self):
        return self.comentario.filter(comentario_aprobado=True)

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={'pk': self.pk})

    def __str__(self):
        return self.titulo


class Comment(models.Model):
    post = models.ForeignKey('blog.Post', related_name='comentario', on_delete=models.CASCADE)
    autor = models.CharField(max_length=200)
    comentario = models.TextField()
    fecha_creacion = models.DateTimeField(default=timezone.now)
    comentario_aprobado = models.BooleanField(default=False)

    def approve(self):
        self.comentario_aprobado = True
        self.save()

    def get_absolute_url(self):
        return reverse("post_list")

    def __str__(self):
        return self.comentario
