from django.utils.timezone import now
from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.


Status = (
    (0, "Borrador"),
    (1, "Publicado")
)


class Categoria(models.Model):
    name = models.CharField(max_length=100, verbose_name='Nombre')
    creado = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creacion')
    update = models.DateTimeField(auto_now=True, verbose_name='Fecha de ultima Edicion')

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = "Categorias"
        ordering = ['-creado']

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name='Titulo', unique=True)
    slug = models.SlugField(max_length=200, unique=True, default=None)
    content = RichTextField(verbose_name='Contenido')
    published = models.DateTimeField(verbose_name='Fecha de Publicacion', default=now())
    image = models.ImageField(verbose_name='Image', upload_to='blog', null=True, blank=True)
    author = models.CharField(max_length=100, verbose_name='Autor')
    categories = models.ManyToManyField(Categoria, verbose_name='Categoria')
    creado = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de Creacion')
    update = models.DateTimeField(auto_now=True, verbose_name='Fecha de ultima Edicion')
    status = models.IntegerField(choices=Status, default=0)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = "Posts"
        ordering = ['-creado']

    def __str__(self):
        return self.title


class Image(models.Model):
    post = models.ForeignKey(Post, related_name='images', on_delete=models.CASCADE)
    file = models.ImageField()
    position = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ['position']

    def __str__(self):
        return '%s - %s' % (self.post, self.file)
