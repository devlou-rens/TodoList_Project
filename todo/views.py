from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Todo

# Home page
def home(request):
    if not request.user.is_authenticated:
        return redirect('login')
    todos = Todo.objects.filter(user=request.user)
    return render(request, 'todo/home.html', {'todos': todos})
def toggle_todo(request, id):
    todo = Todo.objects.get(id=id, user=request.user)
    todo.completed = not todo.completed
    todo.save()
    return redirect('home')

# Register
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists!")
            return redirect('register')
        user = User.objects.create_user(username=username, password=password)
        user.save()
        messages.success(request, "Account created successfully")
        return redirect('login')
    return render(request, 'todo/register.html')

# Login
def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Incorrect Email or Password Please Try Again!")
            messages.error(request, "Or Account doesn't Exist! Please Create one.")
            return redirect('login')
    return render(request, 'todo/login.html')

# Logout
def logout_user(request):
    logout(request)
    return redirect('login')

# Add Todo
def add_todo(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        Todo.objects.create(user=request.user, title=title, description=description)
        return redirect('home')
    return render(request, 'todo/add_todo.html')

# Update Todo
def update_todo(request, id):
    todo = get_object_or_404(Todo, id=id, user=request.user)
    if request.method == 'POST':
        todo.title = request.POST['title']
        todo.description = request.POST['description']
        todo.completed = 'completed' in request.POST
        todo.save()
        return redirect('home')
    return render(request, 'todo/update_todo.html', {'todo': todo})

# Delete Todo
def delete_todo(request, id):
    todo = get_object_or_404(Todo, id=id, user=request.user)
    todo.delete()
    return redirect('home')


# Create your views here.
