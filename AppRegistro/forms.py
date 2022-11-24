from django import forms
from django.forms import ModelForm
from blog.models import Post, Comment
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django.views.generic import (CreateView)
from django.db import models


class UserCreateForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Enter you email...'  , 'class': 'form-control'}))
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Enter you first name...'  , 'class': 'form-control'}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Enter you last name...'  , 'class': 'form-control'}))

    class Meta:
        fields = ("username", "first_name", "last_name", "email", "password1", "password2")
        model = get_user_model()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].label = "Display name"
        self.fields["email"].label = "Email address"


class EditProfileForm(UserChangeForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Ingresa tu correo electrónico...'  , 'class': 'form-control'}))
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Ingresa tu nombre...'  , 'class': 'form-control'}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Ingresa tu apellido...'  , 'class': 'form-control'}))
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Ingresa tu nombre de usuario...'  , 'class': 'form-control'}))
    #last_login = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Enter you last name...'  , 'class': 'form-control'}))
    #is_superuser = forms.CharField(max_length=100, widget=forms.checkboxInput(attrs={'placeholder': 'Es superusuario...'  , 'class': 'form-check'}))
    #is_staff = forms.CharField(max_length=100, widget=forms.checkboxInput(attrs={'placeholder': 'Es staff...'  , 'class': 'form-check'}))
    #is_active = forms.CharField(max_length=100, widget=forms.checkboxInput(attrs={'placeholder': 'Es activo...'  , 'class': 'form-check'}))
    #date_joined = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Fecha de registro...'  , 'class': 'form-control'}))


    class Meta:
        fields = ("username", "first_name", "last_name", "email", "password" )
        model = get_user_model()

    class Meta:
        fields = ("username", "first_name", "last_name", "email", "password" )
        model = get_user_model()



