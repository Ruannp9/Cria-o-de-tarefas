from django.shortcuts import render, redirect
from .models import Task, Aluno

def task_list(request):
    tasks = Task.objects.all()
    return render (request, 'tasks/task_list.html', {'task': tasks})

def add_task(request):
    if request.method == 'POST':
        titulo = request.POST.get('litle')
        if titulo:
            Task.objects.create(title=titulo)
        return redirect('task_list')
    return render(request, 'task/add_task.html')

def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('task_list')
# Create your views here.

def cadastro_escola(request):
    escola = Aluno.objects.all()
    return render (request, 'escola/cadastro_escola.html', {'escola': escola})

def cadastro_adicionar(request):
    if request.method == 'POST':
        cadastrar = request.POST.get('cadastrar')
        if cadastrar:
            Aluno.objects.create(nome=cadastrar)
            return redirect('cadastro_escola')
    return render(request, 'escola/cadastro_adicionar.html')
            
            