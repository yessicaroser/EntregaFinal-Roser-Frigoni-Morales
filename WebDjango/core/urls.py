
from django.urls import path
from .views import home, blog, pages, about, login, profile, singup

urlpatterns = [
    path('', home),
    path('blog/', blog, name="Blog"),
    path('pages/', pages, name="Páginas"),
    path('about/', about, name="Acerca de mi"),
    path('login/', login, name="Login"),
    path('profile/', profile, name="Perfil"),
    path('singup/', singup, name="Registrarme"),

   
]
