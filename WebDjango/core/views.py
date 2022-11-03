from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from datetime import datetime


# Importaciones de formulario y modelo de comentario
from .forms import ComentarioFormulario
from .models import Comentario


# Importaciones relacionadas con "forms"
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, UpdateView, CreateView


#Creación de vistas básicas de web

def home(request):
    return render(request, "inicio.html")

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
# >> Comentarios << #
#-----------------#


class ComentarioList(ListView):

    model = Comentario
    template_name = 'comentario/listarcomentario.html'
    context_object_name = "comentario"

class ComentarioDetail(DetailView):

    model = Comentario
    template_name = 'comentario/detallecomentario.html'
    context_object_name = "comentario"

class ComentarioCreate(CreateView):

    model = Comentario
    template_name = 'comentario/crearcomentario.html'
    fields = ["nombre", "descripcion"]
    success_url = '/core/listarcomentario/'

class ComentarioUpdate(UpdateView):

    model = Comentario = 'comentario/editarcomentario.html'
    fields = ["nombre", "descripcion"]
    success_url = '/core/listarcomentario/'

class ComentarioDelete(DeleteView):

    model = Comentario
    template_name = 'comentario/eliminarcomentario.html'
    success_url = '/core/listarcomentario/'
