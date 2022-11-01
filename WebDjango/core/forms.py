from django import forms
from .models import Categoria

class CategoriaFormulario(forms.Form):
    nombre = forms.CharField(max_length=200)
    descripcion = forms.CharField(max_length=200)

class PublicacionFormulario(forms.Form):
    titulo = forms.CharField(max_length=200)
    descripcion = forms.CharField(max_length=200)
    contenido = forms.CharField(max_length=200)
    #fecha_publicacion = forms.DateField()
    hashtag = forms.CharField(max_length=200)
    autor = forms.CharField(max_length=200)
    categoria = forms.ModelMultipleChoiceField(queryset=Categoria.objects.all())