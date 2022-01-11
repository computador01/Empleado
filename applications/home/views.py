from django.shortcuts import render

from django.views.generic import(
     TemplateView,
     ListView,
     CreateView
)

# import models
from . models import prueba

from.forms import PruebaForm

# Create your views here.

class pruebaView(TemplateView):
    template_name='home/prueba.html'



class ResumenFoundationView(TemplateView):
    template_name='home/resume_foundation.html'
    
    
class pruebaListaView(ListView):
    template_name = "home/lista.html"
    context_object_name ='listaNumeros'
    queryset = ['0','10','20','30']


class ListarPrueba(ListView):
    template_name = "home/lista_prueba.html"
    model = prueba
    context_object_name ='lista'

class pruebacreateView(CreateView):
    template_name = "home/add.html"
    model = prueba
    form_class = PruebaForm
    success_url = '/'



    