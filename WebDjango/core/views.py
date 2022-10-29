from http.client import HTTPResponse
from django.http import HttpResponse
from django.shortcuts import render

#Creación de vistas básicas de web

def inicio(request):

    return HttpResponse("Inicio")
    return render(request, "inicio.html")

def sobre(request):
    return HttpResponse("Acerca de")
    return render(request, "sobre.html")

def servicios(request):
    return HttpResponse("Servicios")
    return render(request, "servicios.html")

def contacto(request):
    return HttpResponse("Contacto")
    return render(request, "contacto.html")

def blog(request):
    return HttpResponse("Blog")
    return render(request, "blog.html")
