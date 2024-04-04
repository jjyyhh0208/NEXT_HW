from django.shortcuts import render, redirect
from .models import *

# Create your views here.
def new(request):
    if request.method == "POST":
        print(request.POST)
        
        new_article = Article.objects.create(
            title = request.POST['title'],
            content = request.POST['content'],
        )
        
        return redirect('detail', article_id = new_article.pk)
    return render(request, 'new.html')

def list(request):
    articles = Article.objects.all()
    ctx = {
        'articles': articles,
    }
    
    return render(request, 'list.html', ctx)

def detail(request, article_id):
    articles = Article.objects.get(pk = article_id)
    
    ctx = {
        'articles': articles
    }
    
    return render(request, 'detail.html', ctx)