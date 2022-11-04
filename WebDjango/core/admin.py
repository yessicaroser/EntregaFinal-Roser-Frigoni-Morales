from django.contrib import admin
from . import models

admin.site.register(models.Profile)
admin.site.register(models.Post)
admin.site.register(models.Categoria)
admin.site.register(models.Publicacion)
admin.site.register(models.Comentario)
