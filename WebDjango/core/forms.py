from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *



class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
        

class PostForm(forms.ModelForm):
	content = forms.CharField(label='', widget=forms.Textarea(attrs={'rows':2, 'placeholder': '¿Qué está pasando?'}), required=True)

	class Meta:
		model = Post
		fields = ['content']
