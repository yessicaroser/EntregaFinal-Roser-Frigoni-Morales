from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

class UserRegisterForm(UserCreationForm):
    name = models.CharField(max_length = 200)
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirma Contraseña', widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']
        help_texts = {k:"" for k in fields }

class PostForm(forms.ModelForm):
	content = forms.CharField(label='', widget=forms.Textarea(attrs={'rows':2, 'placeholder': '¿Qué está pasando?'}), required=True)

	class Meta:
		model = Post
		fields = ['content', 'categories']

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

class ComentarioFormulario(forms.Form):
    # Campos
    user = forms.CharField(max_length=50)
    ingreso_comentario = forms.CharField(max_length=200)

