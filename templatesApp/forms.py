from django import forms
from templatesApp.models import Autor
from templatesApp.models import Libros
from templatesApp.models import Editorial


class FormAutor(forms.ModelForm):
    class Meta:
        model=Autor
        fields='__all__'

class FormLibros(forms.ModelForm):
    class Meta:
        model=Libros
        fields='__all__'

class FormEditorial(forms.ModelForm):
    class Meta:
        model=Editorial
        fields='__all__'

def clean_email(self):
    inputEmail=self.cleaned_data['Email']
    if inputEmail.find('@')==-1:
        raise forms.ValidationError("El correo debe contener @")
    return inputEmail