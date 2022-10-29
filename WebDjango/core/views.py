from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect

#Creación de vistas básicas de web

def inicio(request):
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

def login(request):
    return render(request, "login.html")
    return HttpResponse("Login")

def perfil(request):
    return render(request, "perfil.html")
    return HttpResponse("Perfil")
    
    
def registro(request):
    return render(request, "registro.html")
    return HttpResponse("Registro")
