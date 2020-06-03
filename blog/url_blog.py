from django.urls import path

from blog import views

urlpatterns = [
    path('blogs', views.blog, name='blog'),
    path('blogs/post/<int:pk>', views.detalle_blog, name='post')
]
