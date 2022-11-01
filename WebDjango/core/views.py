from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from datetime import datetime

# Importaciones relacionadas con "forms"
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, UpdateView, CreateView

# Importaciones de formulario y modelo de categoria
from .forms import CategoriaFormulario, PublicacionFormulario
from .models import Categoria, Publicacion

#Creación de vistas básicas de web

def home(request):
    return render(request, "inicio.html")

def formulario(request):
    return render(request, "formulario.html")

def blog(request):
    return HttpResponse("Blog")
    return render(request, "blog.html")

def pages(request):
    return HttpResponse("Páginas")
    return render(request, "pages.html")

def about(request):
    return HttpResponse("Acerca de mi")
    return render(request, "about.html")

def login(request):
    return HttpResponse("Login")
    return render(request, "login.html")

def profile(request):
    return HttpResponse("Perfil")
    return render(request, "perfil.html")

def singup(request):
    return HttpResponse("Registrarme")
    return render(request, "registro.html")

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