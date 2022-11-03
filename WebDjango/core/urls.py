
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('blog/', views.blog, name="blog"),
    path('pages/', views.pages, name="paginas"),
    path('about/', views.about, name="acerca de mi"),
    path('login/', views.login, name="login"),
    path('profile/', views.profile, name="perfil"),
    path('singup/', views.singup, name="registrarme"),


   
# URL para el modelo Comentario
      
    path('listarcomentario/', views.ComentarioList.as_view(), name="listarcomentario"),
    path('crearcomentario/', views.ComentarioCreate.as_view(), name="crearcomentario"),
    path('detallecomentario/<int:pk>', views.ComentarioDetail.as_view(), name="detallecomentario"),
    path('editarcomentario/<int:pk>', views.ComentarioUpdate.as_view(), name="editarcomentario"),
    path('eliminarcomentario/<int:pk>', views.ComentarioDelete.as_view(), name="eliminarcomentario"),


]
