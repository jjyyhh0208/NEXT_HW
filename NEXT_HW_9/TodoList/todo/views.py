from django.shortcuts import render, redirect
from .models import *
from .forms import *
# Create your views here.
def home(request):
    lists = Todo.objects.all()
    ctx = {
        'lists': lists,
    }
    return render(request, 'home.html', ctx)

def create(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        
    else:
        form = TodoForm()
        
    ctx = {
        'form': form
    }
    
    return render(request, 'create.html', ctx)

def detail(request, pk):
    todoList = Todo.objects.get(pk=pk)
    ctx = {
        'list': todoList,
        'pk': pk,
    }
    return render(request, 'detail.html', ctx)

def update(request, pk):
    todoList = Todo.objects.get(pk=pk)
    
    if request.method == 'POST':
        form = TodoForm(request.POST, instance = todoList)
        if form.is_valid():
            form.save()
            return redirect('detail', pk = pk)
    else:
        form = TodoForm(instance=todoList)
        
    ctx = {
        'form': form,
        'list': todoList,
    }
    return render(request, 'update.html', ctx)

def delete(request, pk):
    todoList = Todo.objects.get(pk = pk)
    
    if request.method == 'POST':
        todoList.delete()
        return redirect('home')