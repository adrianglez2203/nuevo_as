from django.shortcuts import render, get_object_or_404

# Create your views here.
from blog import models


def blog(request):
    blogs = models.Post.objects.all().order_by('published').reverse()
    images = models.Image.objects.all()

    contexto = {
        'blogs': blogs,
        'images': images
    }
    return render(request, 'galeria/galeria.html', contexto)


def detalle_blog(request, pk):
    post = get_object_or_404(models.Post, id=pk)
    post1 = models.Post.objects.get(id=pk)
    images = post1.images.all()
    print(images)
    return render(request, 'galeria/post.html', {'post': post1, 'images': images})


def post_a_index(request):
    post = models.Post.objects.all().order_by('published').reverse()
    contexto = {
        'posts': post
    }
    return render(request, 'index.html', contexto)
