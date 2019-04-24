from django.shortcuts import render

# Create your views here.

from inicio import models
def inicio(request):

    testimonio = models.Testimonio.objects.all()
    fotos_carrusel= models.Foto_carrusel.objects.all()
    primera_foto = fotos_carrusel[0]

    contexto={
        'fotos': fotos_carrusel,
        'primera': primera_foto,
        'testimonios':testimonio,
    }
    return render(request,'index.html',contexto)

def cargar_fotos(request):
    fotos = models.Album_fotos_variadas.objects.all()
    contexto={
        'fotos':fotos
    }
    return render(request,'galeria/galeria.html',contexto)


def bodas(request):
    return render(request,'Servicios/bodas.html')