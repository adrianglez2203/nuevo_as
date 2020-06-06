from django.db import models
from django.shortcuts import render
from wagtail.contrib.routable_page.models import RoutablePageMixin, route
from django import forms
from modelcluster.fields import ParentalKey
from modelcluster.contrib.taggit import ClusterTaggableManager
from taggit.models import TaggedItemBase
from wagtail.contrib.routable_page.models import RoutablePageMixin, route
from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, MultiFieldPanel, StreamFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.images.blocks import ImageChooserBlock
from wagtail.search import index
from wagtail.snippets.models import register_snippet
from modelcluster.fields import ParentalKey, ParentalManyToManyField
from django.contrib.auth.models import User
from wagtail.core.fields import StreamField
from wagtail.core import blocks
import six

class HomePage(Page):
    body = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
    ]
@register_snippet
class BlogCategory(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length=80)

    panels = [
        FieldPanel('name'),
        FieldPanel('slug'),
    ]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
class BlogIndexPage(RoutablePageMixin,Page):
    intro = RichTextField(blank=True)

    def get_context(self, request):
        # Update context to include only published posts, ordered by reverse-chron
        context = super().get_context(request)
        blogpages = self.get_children().live().order_by('-first_published_at')
        context['blogpages'] = blogpages
        return context
    content_panels = Page.content_panels + [
        FieldPanel('intro', classname="full")
    ]
    @route(r'^$')
    def index(self,request):
        contexto = super().get_context(request)
        blogpages = self.get_children().live().order_by('-first_published_at')
        contexto['blogpages'] = blogpages

        return render(request, 'blogs/blog_index_page.html',contexto)


class BlogPageTag(TaggedItemBase):
    content_object = ParentalKey(
        'BlogPage',
        related_name='tagged_items',
        on_delete=models.CASCADE
    )

class BlogPage(RoutablePageMixin,Page):
    date = models.DateField("Post date")
    intro = models.CharField(max_length=250)
    template = 'blogs/blog_page.html'
    ajax_template = "blogs/blog_page_ajax.html"
    # body = RichTextField(features=['h1','h2', 'h3','h4','h5','h6', 'bold', 'italic', 'link','ol','ul','hr','document-link','image','embed','code','superscript','subscript','blockquote'])
    body = StreamField([
        ('heading', blocks.CharBlock(classname="full title")),
        ('paragraph', blocks.RichTextBlock()),
        ('image', ImageChooserBlock()),
        ('list', blocks.ListBlock(blocks.CharBlock(label=""))),
        ('document', blocks.BlockQuoteBlock()),
    ])

    tags = ClusterTaggableManager(through=BlogPageTag, blank=True)
    author = models.CharField(max_length=255,default='Adrian')
    categories = ParentalManyToManyField('BlogCategory', blank=True)
    def main_image(self):
        gallery_item = self.gallery_images.first()
        if gallery_item:
            return gallery_item.image
        else:
            return None

    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        index.SearchField('body'),
    ]

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('date'),
            FieldPanel('tags'),
        ], heading="Blog information"),
        FieldPanel('intro'),
        FieldPanel('author'),
        # FieldPanel('body'),
        StreamFieldPanel('body'),
        InlinePanel('gallery_images', label="Gallery images"),
        FieldPanel('categories', widget=forms.CheckboxSelectMultiple),
    ]
    def get_context(self, request):
        context = super().get_context(request)
        raw_url = context['request'].get_raw_uri()
        parse_result = six.moves.urllib.parse.urlparse(raw_url)
        lista = parse_result.path.split('/')
        slug = lista[4]
        print(slug)
        comment1 = Comment.objects.filter(post__slug = slug)
        # comment2 = Comment.objects.filter(post__slug = 'post-1')
        # print(comment)
        post = BlogPage.objects.all()
        context['comments'] = comment1
        return context





class BlogPageGalleryImage(Orderable):
    page = ParentalKey(BlogPage, on_delete=models.CASCADE, related_name='gallery_images')
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
    )
    caption = models.CharField(blank=True, max_length=250)

    panels = [
        ImageChooserPanel('image'),
        FieldPanel('caption'),
    ]
class BlogTagIndexPage(Page):

    def get_context(self, request):

        # Filter by tag
        tag = request.GET.get('tag')
        blogpages = BlogPage.objects.filter(tags__name=tag)

        # Update template context
        context = super().get_context(request)
        context['blogpages'] = blogpages
        return context

class Comment(models.Model):
    author = models.ForeignKey(User,  on_delete=models.CASCADE)
    fecha_creado= models.DateTimeField(auto_now_add=True, editable=False)
    fecha_editado = models.DateTimeField(auto_now=True)
    comentario = models.TextField()
    post = models.ForeignKey(BlogPage, on_delete=models.SET_NULL, null=True, blank=False, editable=True)
    def __str__(self):
        return self.comentario
    class Meta:
        ordering= ['-fecha_creado']
        verbose_name='Comentario'
        verbose_name_plural='Comentarios'