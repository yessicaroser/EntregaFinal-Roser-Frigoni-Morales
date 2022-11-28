from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from . import forms
from django.views.generic import (CreateView, UpdateView, TemplateView)
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import EditProfileForm, PasswordChangingForm


class UserRegisterView(CreateView):
    form_class = forms.UserCreateForm 
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


class UserEditView(UpdateView):
    form_class = EditProfileForm
    success_url = reverse_lazy('panel') #cambiar a home
    template_name = 'profiles/edit_profile.html'

    def get_object(self):
        return self.request.user


class PasswordsChangeView(PasswordChangeView):
    from_class = PasswordChangingForm
    success_url = reverse_lazy('password_success') 

def password_success(request):
    return render(request, 'profiles/password_success.html', {})

@login_required
def panel(request):
    return render(request, 'profiles/base_admin.html', {})


class ProfileView(TemplateView):
    template_name = 'profiles/index.html'
