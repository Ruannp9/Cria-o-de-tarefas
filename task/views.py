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
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        print(nome)
        print(email)
        if nome:
            Aluno.objects.create(nome=nome,email=email)
            
            return redirect('cadastro_escola')
    return render(request, 'escola/cadastro_adicionar.html')

def delete_cadastro(request, Aluno_id):
    cadastro = Aluno.objects.get(id=Aluno_id)
    cadastro.delete()
    return redirect('cadastro_escola')
            
from django.shortcuts import get_object_or_404
def atualizar_cadastro(request, Aluno_id):
    
    i = get_object_or_404(Aluno, id=Aluno_id)
    
    if request.method == 'POST':
        
     i.nome = request.POST.get('nome')
     i.email = request.POST.get('email')
     
     
     i.save()
     
     return redirect('cadastro_escola')
    return render(request, 'escola/cadastro_editar.html', {'Cadastro':i})