from django.shortcuts import render
from inicio import models as model_inicio
from galeria import models
# Create your views here.



def cargar_fotos(request):
    fotos = model_inicio.Album_fotos_variadas.objects.all()
    contexto={
        'fotos':fotos
    }
    return render(request,'galeria/galeria.html',contexto)
