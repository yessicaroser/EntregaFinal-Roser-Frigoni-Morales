from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect

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

#prueba