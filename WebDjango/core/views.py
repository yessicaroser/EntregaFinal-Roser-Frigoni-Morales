from django.shortcuts import render, HttpResponse

#Creación de vistas básicas de web

def home(request):
    return HttpResponse("Inicio")

def about(request):
    return HttpResponse("Historia")

def services(request):
    return HttpResponse("Servicios")

def contact(request):
    return HttpResponse("Contacto")

def blog(request):
    return HttpResponse("Blog")
