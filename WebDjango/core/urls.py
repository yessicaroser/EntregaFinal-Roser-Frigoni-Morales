
from django.urls import path
from . import views
#from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [

    path('', views.home, name='home'),
    
    # Vistas de Cmorales
    path('profile/', views.profile, name='profile'),
    path('about/', views.about, name="Acerca de mi"),
    path('register/', views.register, name='register'),
    path('post/', views.post, name='post'),
    path('login/', LoginView.as_view(template_name='cmorales/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='cmorales/logout.html'), name='logout'),

    # Vistas Originales
    path('blog/', views.blog, name="Blog"),
    path('pages/', views.pages, name="Páginas"),
    path('about/', views.about, name="Acerca de mi"),
    path('login/', views.login, name="Login"),
    path('profile/', views.profile, name="Perfil"),
    path('singup/', views.singup, name="Registrarme"),

    # URL para el modelo Categoria
    path('listarcategoria/', views.CategoriaList.as_view(), name="listarcategoria"),
    path('crearcategoria/', views.CategoriaCreate.as_view(), name="crearcategoria"),
    path('detallecategoria/<int:pk>', views.CategoriaDetail.as_view(), name="detallecategoria"),
    path('editarcategoria/<int:pk>', views.CategoriaUpdate.as_view(), name="editarcategoria"),
    path('eliminarcategoria/<int:pk>', views.CategoriaDelete.as_view(), name="eliminarcategoria"),

    # URL para el modelo Publicacion
    path('listarpublicacion/', views.listarpublicacion, name="listarpublicacion"),
    path('crearpublicacion/', views.crearpublicacion, name="crearpublicacion"),
    path('editarpublicacion/<int:id>', views.editarpublicacion, name="editarpublicacion"),
    path('eliminarpublicacion/<int:id>', views.eliminarpublicacion, name="eliminarpublicacion"),

    # URL para el modelo Comentario
    path('listarcomentario/', views.ComentarioList.as_view(), name="listarcomentario"),
    path('crearcomentario/', views.ComentarioCreate.as_view(), name="crearcomentario"),
    path('detallecomentario/<int:pk>', views.ComentarioDetail.as_view(), name="detallecomentario"),
    path('editarcomentario/<int:pk>', views.ComentarioUpdate.as_view(), name="editarcomentario"),
    path('eliminarcomentario/<int:pk>', views.ComentarioDelete.as_view(), name="eliminarcomentario"),

]
