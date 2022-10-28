from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('services/', views.services, name="services"),
    path('contact/', views.contact, name="contact"),
    path('blog/', views.blog, name="blog"),
    path('admin/', admin.site.urls),
]
