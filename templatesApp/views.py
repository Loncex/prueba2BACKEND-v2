from django.shortcuts import render
from templatesApp.models import Autor
from templatesApp.forms import FormAutor
from django.shortcuts import redirect

# Create your views here.
def index(request):
    return render(request,'index.html')

def ListadoAutor(request):
    autor=Autor.objects.all()
    data ={'autor':autor}
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
