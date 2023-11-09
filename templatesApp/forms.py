from django import forms
from templatesApp.models import Autor


class FormAutor(forms.ModelForm):
    class Meta:
        model=Autor
        fields='__all__'