from django.shortcuts import render, redirect
from .models import *
from django.utils import timezone

# Create your views here.
def programming(request):
    programmings = Programming.objects.all()
    ctx = {
        'programmings': programmings,
    }
    
    return render(request, 'programming.html', ctx)

def programmingDetail(request, pk):
    programming = Programming.objects.get(pk = pk)
    ctx = {
        'programming': programming, 
        'pk': pk,
    }
    return render(request, 'programmingDetail.html', ctx)

def createProgramming(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        content = request.POST.get('content')
        createDate = timezone.now()
        
        newProgramming = Programming.objects.create(name=name, content=content, createDate=createDate)
        newProgramming.save()
        return redirect('programmingDetail', pk=newProgramming.pk)

    return render(request, 'programmingCreate.html')