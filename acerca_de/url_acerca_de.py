from django.urls import path

from acerca_de import views

urlpatterns = [
    path('acerca',views.vista , name='acerca_de'),
]