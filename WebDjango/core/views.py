from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect

# Importaciones relacionadas con "forms"
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, UpdateView, CreateView

# Importaciones de formulario y modelo de categoria
from .forms import CategoriaFormulario
from .models import Categoria

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