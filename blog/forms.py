from django import forms
from blog.models import Post, Comment
from django.contrib.auth import get_user_model


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('autor', 'titulo', 'contenido',)

        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'textinputclass'}),
            'contenido': forms.Textarea(attrs={'class': 'editable medium-editor-textarea postcontent'}),
        }




class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('autor', 'comentario',)

        widgets = {
            'autor': forms.TextInput(attrs={'class': 'textinputclass'}),
            'comentario': forms.Textarea(attrs={'class': 'editable medium-editor-textarea'}),
        }
