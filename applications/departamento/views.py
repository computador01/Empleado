from django.shortcuts import render
from django.views.generic.edit import FormView
from django.views.generic import ListView

from applications.persona.models import Empleado
from.models import Departamento

from .forms import NewDepartamentoForm

# Create your views here.

class DepartamentoListView(ListView):
    template_name = "departamento/lista.html"
    model = Departamento
    context_object_name ='departamentos'
   



class NewDepartamentoView(FormView):
    template_name = 'departamento/new_departamento.html'
    form_class = NewDepartamentoForm
    success_url = '/'
    
    def form_valid(self, form):
        print('****Estamos en el form valid***********')
        
        depa = Departamento(
            name=form.cleaned_data['departamento'],
            shor_name=form.cleaned_data['shorname']  
        )
        depa.save()
        
        nombre = form.cleaned_data['nombre']
        apelido = form.cleaned_data['apellidos']
        Empleado.objects.create(
            first_name=nombre,
            last_name=apelido,
            job='1',
            departamento=depa
    
        )
        return super(NewDepartamentoView, self).form_valid(form)
        
    



