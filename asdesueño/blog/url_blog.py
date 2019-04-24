from django.urls import path

from blog import views

urlpatterns = [
    path('acerca',views.vista , name='acerca_de'),
]