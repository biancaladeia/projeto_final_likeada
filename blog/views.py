#blog/views.py

from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm, SearchForm, CommentForm
from django.contrib.auth import login as auth_login, logout as auth_logout
from .forms import CustomLoginForm, RegistrationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib import messages

def home(request):
    search_form = SearchForm()
    posts = Post.objects.all().order_by('-created_at')  
    # Verifica se o usuário está autenticado
    is_authenticated = request.user.is_authenticated

    return render(request, 'home.html', {'posts': posts, 'search_form': search_form, 'is_authenticated': is_authenticated})

def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'post_detail.html', {'post': post})

def edit_post(request, id):
    post = get_object_or_404(Post, id=id)

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail', id=id)
    else:
        form = PostForm(instance=post)

    return render(request, 'edit_post.html', {'form': form})

def delete_post(request, id):
    post = get_object_or_404(Post, id=id)

    if request.method == 'POST':
        post.delete()
        return redirect('home')

    return render(request, 'delete_post.html', {'post': post})

def search(request):
    query = request.GET.get('q')
    if query:
        results = Post.objects.filter(title__icontains=query)
    else:
        results = Post.objects.all()

    return render(request, 'search_results.html', {'results': results, 'query': query})

def add_comment_to_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)

    if not request.user.is_authenticated:
        return redirect('login')

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('post_detail', id=post.id)
    else:
        form = CommentForm()

    return render(request, 'add_comment_to_post.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        # Verifica se o usuário já está autenticado
        if request.user.is_authenticated:
            return redirect('home')  # Redireciona para a página principal se já estiver autenticado
        form = RegistrationForm()

    return render(request, 'registration.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = CustomLoginForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)  # Verifica se o usuário existe
        if user is not None:
            auth_login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Usuário ou senha inválidos')
    else:
        form = CustomLoginForm()
    return render(request, 'login.html', {'form': form})

@login_required
def user_logout(request):
    auth_logout(request)
    return redirect('home')

'''
@login_required
def post_new(request):
    if not request.user.is_authenticated:
        return redirect('login')

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', id=post.id)
    else:
        form = PostForm()

    return render(request, 'post_new.html', {'form': form})
    '''
    
'''
@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            # Altera a senha do usuário
            user = form.save()
            # Atualiza a sessão do usuário
            update_session_auth_hash(request, user)
            return redirect('home')
    else:
        form = PasswordChangeForm(request.user)

    return render(request, 'change_password.html', {'form': form})
'''