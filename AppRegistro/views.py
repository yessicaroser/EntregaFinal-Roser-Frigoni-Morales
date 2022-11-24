from django.urls import reverse_lazy
from . import forms
from django.views.generic import (CreateView, UpdateView)
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.decorators import login_required
from .forms import EditProfileForm

class UserRegisterView(CreateView):
    form_class = forms.UserCreateForm #ver
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

class UserEditView(UpdateView):
    form_class = EditProfileForm
    success_url = reverse_lazy('about')
    template_name = 'profiles/edit_profile.html'

    def get_object(self):
        return self.request.user

