from django.shortcuts import render
from blogs import models as modelo
from .form import CommentForm
# Create your views here.
# Create your views here.

from inicio import models
def inicio(request):
    pass
    testimonios = models.Testimonio.objects.all()
    fotos_carrusel= models.Foto_carrusel.objects.all()
    fotos= models.Fotos.objects.all()
    portafolio = models.fotos_portafolio.objects.all()


    contexto={
        'fotos': fotos_carrusel,
        'testimonios':testimonios,
        'fotos1':fotos,
        'portafolios':portafolio
    }
    return render(request,'index.html',contexto)

def cargar_fotos(request):
    fotos = models.Fotos.objects.all()
    contexto={
        'fotos':fotos
    }
    return render(request,'galeria/galeria.html',contexto)


def bodas(request):
    return render(request,'Servicios/bodas.html')





def post_comments(request):
    comment_form = CommentForm(request.POST)
    # if request.method == 'POST':
    #     form = request.POST
    #     if form.is_valid():
    #         user = request.user
    #         comentario = request.POST.get('comentario')
    #         comentario = models.Comment.objects.create(author=user, comentario=comentario, post_id=1)
    #     else:
    #         None
    contexto ={
        'form':comment_form
    }
    return render(request, 'index.html', contexto)