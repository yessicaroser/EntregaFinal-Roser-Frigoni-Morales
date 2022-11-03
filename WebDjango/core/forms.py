from django import forms

class ComentarioFormulario(forms.Form):
    # Campos
    user = forms.CharField(max_length=50)
    ingreso_comentario = forms.CharField(max_length=200)

