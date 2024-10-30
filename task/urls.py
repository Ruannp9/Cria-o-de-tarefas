from django.urls import path
from . import views

urlpatterns = [
     path('task/', views.task_list, name='task_list'),
     path('add/', views.add_task, name='add_task' ),
     path('delete/<int:task_id>/', views.delete_task, name='delete_task'),    
     path('', views.cadastro_escola, name='cadastro_escola'),
     path('ad/', views.cadastro_adicionar, name='cadastro_adicionar' ),
]
