from django.shortcuts import render, redirect
from .models import Task , Registro

# exibir informaçoes para o front
def task_list(request):
    tasks = Task.objects.all()
    registro = Registro.objects.all()
    return render(request,'tasks/tasks_list.html', {'tasks': tasks , 'registro': registro})

def cadastro(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        telefone = request.POST.get('telefone')
        
        Registro.objects.create(nome=nome, telefone=telefone)
        return redirect('add_task')
    return render(request,'tasks/cadastro_task.html')


def add_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        completed = request.POST.get('completed')
        if completed :
            completed = True
        else :
            completed = False

        
        if title:
            Task.objects.create(title=title, completed=completed)
        return redirect('task_list')
    return render(request,'tasks/add_task.html')



