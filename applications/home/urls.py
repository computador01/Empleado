from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('prueba/', views.pruebaView.as_view()),
    
    path('lista/', views.pruebaListaView.as_view()),
    
    path('lista-prueba/', views.ListarPrueba.as_view()),
    
    path('add/', views.pruebacreateView.as_view(), name='prueba_add'),
    
     path('resume-foundation/', views.ResumenFoundationView.as_view(), name='resume-foundation'),
    
]

