from django.contrib import admin
from django.urls import path
from templatesApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('autor/', views.ListadoAutor),
    path('agregarAutor/', views.agregarAutor),
    path('eliminarAutor/<idAutor>',views.eliminarAutor),
    path('actualizarAutor/<idAutor>',views.actualizarAutor),
]
