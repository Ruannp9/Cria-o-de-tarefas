from django.urls import path
from . import views

urlpatterns = [
     path('task/', views.task_list, name='task_list'),
     path('add/', views.add_task, name='add_task' ),
     path('delete/<int:Aluno_id>/', views.delete_cadastro, name='delete_cadastro'),
     path('', views.cadastro_escola, name='cadastro_escola'),
     path('ad/', views.cadastro_adicionar, name='cadastro_adicionar' ),
     path('atualizar_cadastro/<int:Aluno_id>/', views.atualizar_cadastro, name='atualizar_cadastro'),
]
