from django.shortcuts import render
from servicios import  models
# Create your views here.
def boda_render(request):
    bodas = models.Servicio_Boda.objects.all()
    contexto = {
        'bodas':bodas
    }
    return render(request,'Servicios/bodas.html',contexto)