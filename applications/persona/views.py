
#from django.db.models.query import QuerySet
from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    TemplateView,
    UpdateView,
    DeleteView
)
from django.views.generic.base import TemplateView
# models
from .models import Empleado

# forms
from.forms import EmpleadoForm

class inicioView(TemplateView):
    """ Vista que carga la pagina de inicio """
    template_name = 'inicio.html'



class listAllEmpleados(ListView):
    template_name = 'persona/list_all.html'
    paginate_by =4
    ordering = 'first_name'
    
    def get_queryset(self):
        Palabra_clave = self.request.GET.get("kword", '')
        lista = Empleado.objects.filter( 
              first_name__icontains=Palabra_clave
        )                                                 
        return lista
    
    
    
class listaEmpleadosAdmin(ListView):
    template_name = 'persona/lista_empleados.html'
    paginate_by =10
    ordering = 'first_name'
    context_object_name = 'empleados'
    model = Empleado
    
    
    
class listBYAreaEmpleados(ListView):
    """ Lista empleados de un area """
    template_name = 'persona/list_by_area.html'
    context_object_name = 'empleados'
    
    def get_queryset(self):
        # escribo el codigo que yo quiera
        area = self.kwargs['shorname']
        lista = Empleado.objects.filter( 
             departamento__shor_name= area
     )
        return lista
    
 
 
 
class listarEmpleadosBYTrabajo(ListView):
    """ Listar empleados por trabajo """
    template_name = 'persona/list_by_Trabajo.html'
    
    def get_queryset(self):
        # escribo el codigo que yo quiera
        trabajo = self.kwargs['shorname']
        lista = Empleado.objects.filter( 
            departamento__shor_name = trabajo
     )
        return lista
       
       
       
    
class listEmpleadosByKword(ListView):
    """ Lista empleados por palabra clave"""
    template_name ='persona/by_kword.html'
    context_object_name ='empleados'

    def get_queryset(self):
        Palabra_clave = self.request.GET.get("kword", '')
        lista = Empleado.objects.filter( 
              first_name=Palabra_clave
        )                                                 
        return lista




class listHabilidadesEmpleados(ListView):
    """ Lista empleados por habilidades"""
    template_name = 'persona/habilidades.html'
    context_object_name ='habilidades'
    
    
    def get_queryset(self):
        empleado = Empleado.objects.get(id=7)
        return empleado.habilidades.all()
    
    

class EmpleadoDetailView(DetailView):
    model = Empleado
    template_name = "persona/detail_empleado.html"
    
    def get_context_data(self, **kwargs):
        context = super(EmpleadoDetailView, self).get_context_data(**kwargs)
        context['titulo'] = 'Empleado del mes'
        return context
    
    
    
    

class successView(TemplateView):
    template_name = "persona/success.html"
    
    
    
class EmpleadoCreateView(CreateView):
    template_name = "persona/add.html"
    model = Empleado
    form_class = EmpleadoForm
    success_url = reverse_lazy('persona_app:empleados_admin')
    
    def form_valid(self, form):
        #logica del proceso
        empleado = form.save(commit=False)
        empleado.full_name = empleado.first_name + ' ' + empleado.last_name
        empleado.save()
        return super(EmpleadoCreateView, self).form_valid(form)
    
    
    
class EmpleadoUpdateView(UpdateView):
    template_name = "persona/update.html"
    model = Empleado
    fields = [
        'first_name',
        'last_name',
        'job',
        'departamento',
        'habilidades',
    ]
    success_url = reverse_lazy('persona_app:empleados_admin')


class EmpleadoDeleteView(DeleteView):
    template_name = "persona/delete.html"
    model = Empleado
    success_url = reverse_lazy('persona_app:empleados_admin')
        
        
        
     

    
    
