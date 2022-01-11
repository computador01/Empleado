from django.contrib import admin
from django.urls import path

from . import views

app_name = "persona_app"

urlpatterns = [
    
    path('', views.inicioView.as_view(),name='inicio'),

    path('listar-todo-empleados/', views.listAllEmpleados.as_view(),name='empleados_all'),
    
    path('lista-by-area/<shorname>/', views.listBYAreaEmpleados.as_view(),name='empleados_area'),
    
     
    path('lista-empleados-admin/', views.listaEmpleadosAdmin.as_view(),name='empleados_admin'),
    
    
    
    
    path('buscar-empleado/', views.listEmpleadosByKword.as_view()),
    path('listar-habilidades-empleado/', views.listHabilidadesEmpleados.as_view()),
    path('listar-empleado_Trabajo/<shorname>/', views.listarEmpleadosBYTrabajo.as_view()),
    path('ver-empleado/<pk>/', views.EmpleadoDetailView.as_view(),name='empleado_detail'),
    
    path('add-empleado/', views.EmpleadoCreateView.as_view(), name='empleado-add'),
    
    
    path('success/', 
         views.successView.as_view(),
         name='correcto'
    ),
    
    
    path('update-empleado/<pk>/', views.EmpleadoUpdateView.as_view(),name='modificar_empleado'),
    path('delete-empleado/<pk>/', views.EmpleadoDeleteView.as_view(),name='eliminar_empleado'),
]

