from django.db import forms
from Models.post.models import post
# Register your models here.
class Posted(forms.ModelForm):
    class Meta: 
        model= Posts