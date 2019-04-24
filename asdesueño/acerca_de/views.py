from django.shortcuts import render
from inicio import models
# Create your views here.
def vista(request):

    foto1 = models.Foto_carrusel.objects.all()
    contexto = {
        'foto1':foto1
    }
    return render(request,'acerca.html',contexto)