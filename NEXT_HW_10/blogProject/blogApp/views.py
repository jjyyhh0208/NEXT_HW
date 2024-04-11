from django.shortcuts import render, redirect, get_object_or_404
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
    comments = articles.comments.filter(parent__isnull=True)
    
    if request.method == 'POST':
        content = request.POST['content']
        parent_id = request.POST.get('parent_id')
        
        if parent_id:
            parent_comment = get_object_or_404(ArticleComment, id=parent_id)
            ArticleComment.objects.create(content=content, article=articles, parent=parent_comment)
        else:
            ArticleComment.objects.create(content=content, article=articles)
            
        return redirect('detail', article_id)
    
    ctx = {
        'articles': articles,
        'comments': comments,
    }
    
    return render(request, 'detail.html', ctx)