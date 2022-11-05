from django.http import HttpResponseRedirect
from datetime import datetime
from django.shortcuts import render, redirect, get_object_or_404


# Importaciones de formularios y modelos
from .forms import PostForm, PublicacionFormulario, Post, UserRegisterForm
from .models import Comentario, Categoria, Publicacion

# Importaciones relacionadas de vistas
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, UpdateView, CreateView

# Importaciones relacionadas de objetos varios
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
#from django.contrib.auth.forms import UserCreationForm

# Creación de vistas Cmorales
def home(request):
    posts = Post.objects.all()
    context = { 'posts': posts}
    return render(request, 'cmorales/home.html', context)

def about(request):
    return render(request, "cmorales/about.html")

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'Usuario {username} creado')
            return redirect('home')
    else:
        form = UserRegisterForm()
    context = { 'form' : form }
    return render(request, 'cmorales/register.html', context)

def formulario(request):
    return render(request, "formulario.html")

@login_required
def post(request):
	current_user = get_object_or_404(User, pk=request.user.pk)
	if request.method == 'POST':
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.user = current_user
			post.save()
			messages.success(request, 'Post enviado')
			return redirect('home')
	else:
		form = PostForm()
	return render(request, 'cmorales/post.html', {'form' : form })

def profile(request, username=None):
	current_user = request.user
	if username and username != current_user.username:
		user = User.objects.get(username=username)
		posts = user.posts.all()
	else:
		posts = current_user.posts.all()
		user = current_user
	return render(request, 'cmorales/profile.html', {'user':user, 'posts':posts})

# Creación de vistas Originales

def blog(request):
    #return HttpResponse("Blog")
    return render(request, "/originales/blog.html")

def pages(request):
    #return HttpResponse("Páginas")
    return render(request, "/originales/pages.html")

def login(request):
    #return HttpResponse("Login")
    return render(request, "/originales/login.html")

def singup(request):
    #return HttpResponse("Registrarme")
    return render(request, "/originales/registro.html")

#-----------------#
# >> Categoria << #
#-----------------#

class CategoriaList(ListView):

    model = Categoria
    template_name = 'categoria/listarcategoria.html'
    context_object_name = "categorias"

class CategoriaDetail(DetailView):

    model = Categoria
    template_name = 'categoria/detallecategoria.html'
    context_object_name = "categoria"

class CategoriaCreate(CreateView):

    model = Categoria
    template_name = 'categoria/crearcategoria.html'
    fields = ["nombre", "descripcion"]
    success_url = '/core/listarcategoria/'

class CategoriaUpdate(UpdateView):

    model = Categoria
    template_name = 'categoria/editarcategoria.html'
    fields = ["nombre", "descripcion"]
    success_url = '/core/listarcategoria/'

class CategoriaDelete(DeleteView):

    model = Categoria
    template_name = 'categoria/eliminarcategoria.html'
    success_url = '/core/listarcategoria/'

#-------------------#
# >> Publicacion << #
#-------------------#

def listarpublicacion(request):
    publicaciones = Publicacion.objects.all()
    return render(request, "publicacion/listarpublicacion.html", {"publicaciones": publicaciones})

def crearpublicacion(request):

    print('method:', request.method)
    print('post: ', request.POST)

    if request.method == 'POST':

        miFormulario = PublicacionFormulario(request.POST)

        if miFormulario.is_valid():

            data = miFormulario.cleaned_data

            publicacion = Publicacion(
                titulo = data['titulo'],
                descripcion = data['descripcion'],
                contenido = data['contenido'],
                fecha_publicacion = datetime.now(),
                hashtag = data['hashtag'],
                autor = data['autor'],
                categoria = data['categoria'][0]
            )
            
            publicacion.save()

            return HttpResponseRedirect('/core/listarpublicacion/')
    
    else:

        miFormulario = PublicacionFormulario()

        return render(request, "publicacion/crearpublicacion.html", {"miFormulario": miFormulario})

def editarpublicacion(request, id):

    print('method:', request.method)
    print('post: ', request.POST)

    publicacion = Publicacion.objects.get(id=id)

    if request.method == 'POST':

        miFormulario = PublicacionFormulario(request.POST)

        if miFormulario.is_valid():

            data = miFormulario.cleaned_data

            publicacion.titulo = data["titulo"]
            publicacion.descripcion = data["descripcion"]
            publicacion.contenido = data["contenido"]
            publicacion.hashtag = data["hashtag"]
            publicacion.autor = data["autor"]
            publicacion.categoria = data["categoria"][0]

            publicacion.save()

            return HttpResponseRedirect('/core/listarpublicacion/')
    
    else:

        miFormulario = PublicacionFormulario(initial={
            "titulo": publicacion.titulo,
            "descripcion": publicacion.descripcion,
            "contenido": publicacion.contenido,
            "hashtag": publicacion.hashtag,
            "autor": publicacion.autor,
            "categoria": publicacion.categoria,
        })

        return render(request, "publicacion/editarpublicacion.html", {"miFormulario": miFormulario, "id": publicacion.id})

def eliminarpublicacion(request, id):

    if request.method == 'POST':

        publicacion = Publicacion.objects.get(id=id)
        publicacion.delete()

        publicaciones = Publicacion.objects.all()
        return render(request, "publicacion/listarpublicacion.html", {"publicaciones": publicaciones})  

#-------------------#
# >> Comentarios << #
#-------------------#


class ComentarioList(ListView):

    model = Comentario
    template_name = 'comentario/listarcomentario.html'
    context_object_name = "comentarios"

class ComentarioDetail(DetailView):

    model = Comentario
    template_name = 'comentario/detallecomentario.html'
    context_object_name = "comentario"

class ComentarioCreate(CreateView):

    model = Comentario
    template_name = 'comentario/crearcomentario.html'
    fields = ["users", "publicacion_comentario", "ingreso_comentario"]
    success_url = '/core/listarcomentario/'

class ComentarioUpdate(UpdateView):

    model = Comentario 
    fields = ["users", "publicacion_comentario", "ingreso_comentario"]
    success_url = '/core/listarcomentario/'
    
class ComentarioDelete(DeleteView):

    model = Comentario
    template_name = 'comentario/eliminarcomentario.html'
    success_url = '/core/listarcomentario/'
