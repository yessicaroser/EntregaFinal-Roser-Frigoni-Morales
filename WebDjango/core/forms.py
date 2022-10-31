from django import forms

class CategoriaFormulario(forms.Form):
    nombre = forms.CharField(max_length=200)
    descripcion = forms.CharField(max_length=200)
