
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('blog/', views.blog, name="Blog"),
    path('pages/', views.pages, name="Páginas"),
    path('about/', views.about, name="Acerca de mi"),
    path('login/', views.login, name="Login"),
    path('profile/', views.profile, name="Perfil"),
    path('singup/', views.singup, name="Registrarme"),

    # URL para el modelo Categoria
    path('crearcategoria/', views.CategoriaCreate.as_view(), name="crearcategoria"),
    path('editarcategoria/<int:pk>', views.CategoriaUpdate.as_view(), name="editarcategoria"),
    path('eliminarcategoria/<int:pk>', views.CategoriaDelete.as_view(), name="eliminarcategoria"),
    path('listarcategoria/', views.CategoriaList.as_view(), name="listarcategoria"),
    path('detallecategoria/<int:pk>', views.CategoriaDetail.as_view(), name="detallecategoria"),

    # URL para el modelo Publicacion
    path('crearpublicacion/', views.singup, name="crearpublicacion"),
    path('editarpublicacion/<int:id>', views.singup, name="editarpublicacion"),
    path('eliminarpublicacion/<int:id>', views.singup, name="eliminarpublicacion"),
    path('listarpublicacion/', views.singup, name="listarpublicacion"),
]
