from django.shortcuts import render, redirect
from django.utils import timezone
from .models import *

# Create your views here.
def food(request):
    foods = Food.objects.all()
    ctx = {
        'foods': foods,
    }
    
    return render(request, 'food.html', ctx)

def foodDetail(request, pk):
    food = Food.objects.get(pk = pk)
    ctx = {
        'food': food, 
        'pk': pk,
    }
    return render(request, 'foodDetail.html', ctx)

def createFood(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        content = request.POST.get('content')
        createDate = timezone.now()
        
        newFood = Food.objects.create(name=name, content=content, createDate=createDate)
        newFood.save()
        return redirect('foodDetail', pk=newFood.pk)

    return render(request, 'foodCreate.html')