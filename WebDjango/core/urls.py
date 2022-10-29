from django.contrib import admin
from django.urls import path
from .views import inicio, sobre, servicios, contacto, blog

urlpatterns = [
    path('', inicio),
    path('about/', sobre, name="sobre"),
    path('services/', servicios, name="servicios"),
    path('contacto/', contacto, name="contacto"),
    path('blog/', blog, name="blog"),
    path('admin/', admin.site.urls),
]
