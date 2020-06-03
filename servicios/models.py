from django.db import models

# Create your models here.
class Servicio_Boda(models.Model):
    Titulo = models.CharField(max_length=60,null=False,blank=False)
    Descripcion = models.TextField(max_length=2000,null=False,blank=False)

    def __str__(self):
        return self.Titulo