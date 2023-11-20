from django.contrib import admin
from django.urls import path
from templatesApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('autor/', views.ListadoAutor),
    path('libros/', views.ListadoLibros),
    path('editorial/', views.ListadoEditorial),
    path('agregarAutor/', views.agregarAutor),
    path('eliminarAutor/<idAutor>',views.eliminarAutor),
    path('actualizarAutor/<idAutor>',views.actualizarAutor),
    path('agregarLibros/', views.agregarLibro),
    path('eliminarLibro/<idLibro>',views.eliminarLibro),
    path('actualizarLibro/<idLibro>',views.actualizarLibro),
    path('agregarEditorial/', views.agregarEditorial),
    path('eliminarEditorial/<idEditorial>',views.eliminarEditorial),
    path('actualizarEditorial/<idEditorial>',views.actualizarEditorial)
]
