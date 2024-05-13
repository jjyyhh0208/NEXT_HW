from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from .models import Comment, Post
from django.utils.decorators import method_decorator
from django.utils import timezone
from functools import wraps

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        exist_user = User.objects.filter(username=username)
        if exist_user:
            error = "이미 존재하는 유저입니다."
            return render(request, 'registration/signup.html', {"error": error})

        new_user = User.objects.create_user(username=username, password=password)
        auth.login(request, new_user)

        return redirect('home')

    return render(request, 'registration/signup.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user, backend="django.contrib.auth.backends.ModelBackend")
            return redirect(request.GET.get('next', '/'))
        error = "아이디 또는 비밀번호가 틀립니다"
        return render(request, 'registration/login.html', {"error": error})

    return render(request, 'registration/login.html')

def home(request):
    posts = Post.objects.all()
    return render(request, 'home.html', {'posts': posts})

def logout(request):
    auth.logout(request)
    return redirect('home')

@login_required(login_url="/registration/login/")
def new(request):
    if request.method == "POST":
        title = request.POST['title']
        content = request.POST['content']
        new_post = Post.objects.create(
            title=title,
            content=content,
            author=request.user
        )
        return redirect('detail', new_post.pk)

    return render(request, 'new.html')

def track_last_viewed(func):
    @wraps(func)
    def wrapper(request, *args, **kwargs):
        response = func(request, *args, **kwargs)
        if request.user.is_authenticated:
            post_pk = kwargs.get('post_pk', None)
            if post_pk:
                post = Post.objects.get(pk=post_pk)
                post.last_viewer = request.user
                post.last_viewed = timezone.now()
                post.save(update_fields=['last_viewer', 'last_viewed'])
        return response
    return wrapper

@login_required(login_url="/registration/login/")
@track_last_viewed
def detail(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    if request.method == 'POST':
        content = request.POST['content']
        if 'delete_comment' in request.POST:
            comment_id = request.POST['delete_comment_id']
            comment = Comment.objects.get(pk=comment_id, author=request.user)
            comment.delete()
        else:
            Comment.objects.create(post=post, content=content, author=request.user)
    comments = post.comments.all()
    return render(request, 'detail.html', {'post': post, 'comments': comments})


def edit(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        Post.objects.filter(pk=post_pk).update(
            title=title,
            content=content
        )
        return redirect('detail', post_pk)

    return render(request, 'edit.html', {'post': post})

def delete(request, post_pk):
    post = Post.objects.get(pk=post_pk)
    if post.author == request.user:
        post.delete()
    return redirect('home')

def delete_comment(request, post_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk, author=request.user)
    if comment:
        comment.delete()
    return redirect('detail', post_pk)
