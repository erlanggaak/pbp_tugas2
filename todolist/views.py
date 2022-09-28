import datetime
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from todolist.models import Task

@login_required(login_url='/todolist/login/')
def show_todolist(request):
    task_list = Task.objects.all().filter(user = request.user)
    context = {
        'task_list': task_list,
        'task_count': task_list.count
    }
    return render(request, "todolist.html", context)

@login_required(login_url='/todolist/login/')
def add_task(request):
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        Task.objects.create(
            user = request.user,
            title = title,
            description = description,
        )
        return HttpResponseRedirect(reverse("todolist:show_todolist"))
    return render(request, "addtask.html")

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) # melakukan login terlebih dahulu
            response = HttpResponseRedirect(reverse("todolist:show_todolist")) # membuat response
            response.set_cookie('last_login', str(datetime.datetime.now())) # membuat cookie last_login dan menambahkannya ke dalam response
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return response

@login_required(login_url='/todolist/login/')
def change_status(request, id):
    task = Task.objects.get(pk=id)
    if task.is_finished:
        task.is_finished = False
    else:
        task.is_finished = True
    task.save()
    return HttpResponseRedirect(reverse('todolist:show_todolist'))

@login_required(login_url='/todolist/login/')
def delete(request, id):
    task = Task.objects.get(pk=id)
    task.delete()
    return HttpResponseRedirect(reverse('todolist:show_todolist'))