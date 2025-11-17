from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm

def index(request):
    tasks = Task.objects.all()
    return render(request, 'index.html', {'tasks': tasks})

def add_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = TaskForm()
    return render(request, 'add_task.html', {'form': form})

def edit_task(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = TaskForm(instance=task)
    return render(request, 'edit_task.html', {'form': form})

def completed_tasks(request):
    tasks = Task.objects.filter(status='completed')
    return render(request, 'completed.html', {'tasks': tasks})

def in_progress_tasks(request):
    tasks = Task.objects.filter(status='in-progress')
    return render(request, 'in_progress.html', {'tasks': tasks})
