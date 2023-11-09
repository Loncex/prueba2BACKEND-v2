from django.db import models

# Create your models here.
class Autor(models.Model):
    idAutor=models.AutoField(primary_key=True)
    nombreAutor=models.CharField(max_length = 20)
    apellidoAutor=models.CharField(max_length = 20)
    fechaNacimiento=models.CharField(max_length=30)
    Sexo=models.CharField(max_length = 20)
    telefonoAutor=models.CharField(max_length = 12)
    Email=models.CharField(max_length = 30)

    def __str__(self):
        fila = 'Autor:' + self.nombreAutor + '-' + 'Email:' + self.Email 
        return  fila
    
