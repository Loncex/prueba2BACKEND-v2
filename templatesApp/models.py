from django.db import models

# Create your models here.
class Autor(models.Model):
    idAutor=models.AutoField(primary_key=True)
    nombreAutor=models.CharField(max_length = 200)
    apellidoAutor=models.CharField(max_length = 200)
    fechaNacimiento=models.DateField()
    SEXO_CHOICES = [
        ('Hombre', 'Hombre'),
        ('Mujer', 'Mujer'),
        ('Otro', 'Otro'),
    ]
    sexo=models.CharField(max_length=20, choices=SEXO_CHOICES)
    telefonoAutor=models.CharField(max_length = 30)
    Email=models.EmailField(max_length = 200)

    def __str__(self):
        fila = 'Autor:' + self.nombreAutor + '-' + 'Email:' + self.Email 
        return  fila
    
class Editorial(models.Model):
    idEditorial=models.AutoField(primary_key=True)
    nombreEditorial=models.CharField(max_length = 200, )
    direccionEditorial=models.CharField(max_length = 200)
    ciudadEditorial=models.CharField(max_length = 200)
    numeroEditorial=models.CharField(max_length = 40)
    telefonoEditorial=models.CharField(max_length = 40)
    faxEditorial=models.CharField(max_length = 40,blank=True, null=True)

    def __str__(self):
        fila = 'Editorial:' + self.nombreEditorial + '-' + 'Direccion:' + self.direccionEditorial
        return  fila   

class Libros(models.Model):
    idLibro=models.AutoField(primary_key=True)
    tituloLibro=models.CharField(max_length = 200)
    generoLibro=models.CharField(max_length = 200)
    anoPublicacion=models.DateField()
    idiomaLibro=models.CharField(max_length = 40)
    paginasLibro=models.CharField(max_length = 40)
    precioLibro=models.CharField(max_length = 40)

    # Relación muchos a muchos con Autor
    autores = models.ManyToManyField(Autor)

    # Relación uno a muchos con Editorial
    editorial = models.ForeignKey(Editorial, on_delete=models.CASCADE)

    def __str__(self):
        fila = 'Libro:' + self.tituloLibro + '-' + 'Precio:' + self.precioLibro
        return  fila   
