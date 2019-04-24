from django.core.exceptions import ValidationError
from django.db import models


# Create your models here.


class Boda(models.Model):
    fecha_realizacion = models.DateField(max_length=20, blank=False)
    nombre_novia = models.CharField(max_length=50)
    nombre_novio = models.CharField(max_length=50)
    localizacion = models.CharField(max_length=30)

    def __str__(self):
        return "Boda de " + self.nombre_novia +" y "+ self.nombre_novio

    class Meta:
        ordering = ('fecha_realizacion',)
        verbose_name_plural='Bodas'


class Fotos(models.Model):
    fotografia = models.ImageField(upload_to='',blank=True, null=True)
    boda = models.ForeignKey(Boda, on_delete=models.CASCADE)
    def __str__(self):
        return self.boda.nombre_novia
    class Meta:
        verbose_name_plural='Fotos'

class Album_fotos_variadas(models.Model):
    nombre = models.CharField(max_length=25,blank=True, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    foto1 = models.ImageField(upload_to='',blank=True, null=True)


class Foto_carrusel(models.Model):
    foto = models.ImageField(upload_to='')
    descripcion = models.CharField(max_length=25,blank=True,null=True)

    def __str__(self):
        return self.foto.url

def validar_calificacion(value):
    if value < 1 and value > 5:
        raise ValidationError(
            ('%(value)s no es un numero entre 1 y 5'),
            params={'value':value},
        )
class Testimonio(models.Model):
    nombre = models.CharField(max_length=50,null=False,blank=False)
    testimonio = models.TextField(max_length=150, null=False, blank=False)
    foto = models.ImageField(upload_to='')
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    profesion = models.CharField(max_length=20,null=True,blank=True,default='')
    estrellas = models.IntegerField(validators=[validar_calificacion],default=5)

    def __str__(self):
        return self.nombre
    class Meta:
        ordering= ['fecha_creacion']
        verbose_name_plural='Testimonios'

