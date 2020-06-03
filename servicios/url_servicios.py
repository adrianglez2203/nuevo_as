from django.urls import path

from servicios import views

urlpatterns = [
    path('servicios/bodas',views.boda_render,name='bodas'),
]

