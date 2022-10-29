
from django.urls import path
from .views import inicio, sobre, login, perfil, registro, contacto, blog

urlpatterns = [
    path('', inicio),
    path('sobre/', sobre, name="Sobre"),
    path('login/', login, name="Login"),
    path('perfil/', perfil, name="Perfil"),
    path('registro/', registro, name="Registro"),
    path('contacto/', contacto, name="Contacto"),
    path('blog/', blog, name="Blog"),
   
]
