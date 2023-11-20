from django.shortcuts import render
from templatesApp.models import Autor
from templatesApp.forms import FormAutor
from templatesApp.models import Libros
from templatesApp.forms import FormLibros
from templatesApp.models import Editorial
from templatesApp.forms import FormEditorial
from django.shortcuts import redirect

# Create your views here.
def index(request):
    return render(request,'index.html')

#Autor
def ListadoAutor(request):
    autor=Autor.objects.all()
    data ={'autor': autor}
    return render(request,'autor.html',data)

def agregarAutor(request):
    form =FormAutor()
    if request.method =='POST':
        form = FormAutor(request.POST)
        if form.is_valid():
            form.save()
        return ListadoAutor(request)
    data={'form':form}
    return render(request,'agregarAutor.html',data)

def eliminarAutor(request,idAutor):
    autor=Autor.objects.get(idAutor=idAutor)
    autor.delete()
    return redirect('/autor')

def actualizarAutor(request,idAutor):
     autor=Autor.objects.get(idAutor=idAutor)
     form=FormAutor(instance=autor)
     if request.method =='POST':
         form = FormAutor(request.POST,instance=autor)
         if form.is_valid():
             form.save()
         return ListadoAutor(request)
     data={'form':form}
     return render(request,'agregarAutor.html',data)

#Libros
def ListadoLibros(request):
    libros=Libros.objects.all()
    data ={'libros': libros}
    return render(request,'libros.html',data)

def agregarLibro(request):
    form =FormLibros()
    if request.method =='POST':
        form = FormLibros(request.POST)
        if form.is_valid():
            form.save()
        return ListadoLibros(request)
    
    else:
        form = FormLibros
        
    data={'form':form}
    return render(request,'agregarLibros.html',data)

def eliminarLibro(request,idLibro):
    libros=Libros.objects.get(idLibro=idLibro)
    libros.delete()
    return redirect('/libros')

def actualizarLibro(request,idLibro):
     libro=Libros.objects.get(idLibro=idLibro)
     form=FormLibros(instance=libro)
     if request.method =='POST':
         form = FormLibros(request.POST,instance=libro)
         if form.is_valid():
             form.save()
         return ListadoLibros(request)
     data={'form':form}
     return render(request,'agregarLibros.html',data)

#Editorial
def ListadoEditorial(request):
    editorial=Editorial.objects.all()
    data ={'editorial': editorial}
    return render(request,'editorial.html',data)

def agregarEditorial(request):
    form =FormEditorial()
    if request.method =='POST':
        form = FormEditorial(request.POST)
        if form.is_valid():
            form.save()
        return ListadoEditorial(request)
    data={'form':form}
    return render(request,'agregarEditorial.html',data)

def eliminarEditorial(request,idEditorial):
    editorial=Editorial.objects.get(idEditorial=idEditorial)
    editorial.delete()
    return redirect('/editorial')

def actualizarEditorial(request,idEditorial):
     editorial=Editorial.objects.get(idEditorial=idEditorial)
     form=FormEditorial(instance=editorial)
     if request.method =='POST':
         form = FormEditorial(request.POST,instance=editorial)
         if form.is_valid():
             form.save()
         return ListadoEditorial(request)
     data={'form':form}
     return render(request,'agregarEditorial.html',data)