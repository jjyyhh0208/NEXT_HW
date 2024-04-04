from django.shortcuts import render, redirect
from .models import *
from django.utils import timezone

# Create your views here.
def hobby(request):
    hobbys = Hobby.objects.all()
    ctx = {
        'hobbys': hobbys,
    }
    
    return render(request, 'hobby.html', ctx)

def hobbyDetail(request, pk):
    hobby = Hobby.objects.get(pk = pk)
    ctx = {
        'hobby': hobby, 
        'pk': pk,
    }
    return render(request, 'hobbyDetail.html', ctx)

def createHobby(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        content = request.POST.get('content')
        createDate = timezone.now()
        
        newHobby = Hobby.objects.create(name=name, content=content, createDate=createDate)
        newHobby.save()
        return redirect('hobbyDetail', pk=newHobby.pk)

    return render(request, 'hobbyCreate.html')