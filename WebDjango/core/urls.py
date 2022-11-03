
from django.urls import path
#from .views import home, blog, pages, about, login, profile, search_coments, singup
from .views import home, blog, about, formulario


urlpatterns = [
    path('', home, name='home'),
    path('blog/', blog, name="Blog"),
    #path('pages/', pages, name="Páginas"),
    path('about/', about, name="Acerca de mi"),
    # path('login/', login, name="Login"),
    # path('profile/', profile, name="Perfil"),
    # path('singup/', singup, name="Registrarme"),
    #path('singup/', singup, name="Registrarme"),
    path('formulario/', formulario, name="Formulario"),

   
]
