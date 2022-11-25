from django import forms
#from django.forms import ModelForm
#from blog.models import Post, Comment
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
#from django.contrib.auth.models import User
#from django.views.generic import (CreateView)
#from django.db import models

class UserCreateForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput())
    first_name = forms.CharField(max_length=100, widget=forms.TextInput())
    last_name = forms.CharField(max_length=100, widget=forms.TextInput())

    class Meta:
        fields = ("username", "first_name", "last_name", "email", "password1", "password2")
        model = get_user_model()

class EditProfileForm(UserChangeForm):
    email = forms.EmailField(widget=forms.EmailInput())
    first_name = forms.CharField(max_length=100, widget=forms.TextInput())
    last_name = forms.CharField(max_length=100, widget=forms.TextInput())
    username = forms.CharField(max_length=100, widget=forms.TextInput())
    #last_login = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Enter you last name...'  , 'class': 'form-control'}))
    #is_superuser = forms.CharField(max_length=100, widget=forms.checkboxInput(attrs={'placeholder': 'Es superusuario...'  , 'class': 'form-check'}))
    #is_staff = forms.CharField(max_length=100, widget=forms.checkboxInput(attrs={'placeholder': 'Es staff...'  , 'class': 'form-check'}))
    #is_active = forms.CharField(max_length=100, widget=forms.checkboxInput(attrs={'placeholder': 'Es activo...'  , 'class': 'form-check'}))
    #date_joined = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Fecha de registro...'  , 'class': 'form-control'}))

    class Meta:
        fields = ("username", "first_name", "last_name", "email", "password" )
        model = get_user_model()



class PasswordChangingForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'type':'password'}))
    new_password1 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control', 'type':'password'}))
    new_password2 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class': 'form-control', 'type':'password'}))

    class Meta:
        fields = ("old_password", "new_password1", "new_password2")
        model = get_user_model()

