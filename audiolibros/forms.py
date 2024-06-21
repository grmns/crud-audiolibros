# audiolibros/forms.py

from django import forms
from .models import Audiolibro

class AudiolibroForm(forms.ModelForm):
    fecha_publicacion = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))

    class Meta:
        model = Audiolibro
        fields = ['titulo', 'autor', 'descripcion', 'audio', 'tipo', 'fecha_publicacion']
