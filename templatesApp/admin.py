from django.contrib import admin
from templatesApp.models import Autor
from templatesApp.models import Libros
from templatesApp.models import Editorial

# Register your models here.
admin.site.register(Autor)
admin.site.register(Libros)
admin.site.register(Editorial)
