from django.shortcuts import render, redirect
from .models import Task, List
from .forms import SearchListForm, TaskForm, ListForm
from django.contrib.auth.models import User
from django.db import models
from django.utils.dateparse import parse_datetime
from datetime import datetime
from django.contrib import messages
# Create your views here.
def to_do_list(request, fk):
    if request.method == 'GET':
        form = SearchListForm(request.GET) 
        if form.is_valid():
            search = form.cleaned_data['name']
            the_list = List.objects.get(id = fk)
            tasks = the_list.tasks.all()
            context = {
                'tasks': tasks.filter(name__contains = search),
                'form': form,
                'fk': fk,
            }
            return render(request, 'main/todo_list.html', context)
    
    if request.GET.get('order', '') != '':
        the_list = List.objects.get(id = fk)
        tasks = the_list.tasks.all()
        context = {
            'tasks': tasks.order_by("name"),
            'list': the_list,
            'fk': fk,
        }        
        return render(request, 'main/todo_list.html', context)
    
    the_list = List.objects.get(id = fk)
    tasks = the_list.tasks.all()
    context = {
        'tasks': tasks,
        'list': the_list,
        'fk': fk,
    }

    return render(request, 'main/todo_list.html', context)

def done_list(request, fk):
    
    if request.method == 'GET':
        form = SearchListForm(request.GET) 
        if form.is_valid():
            search = form.cleaned_data['name']
            the_list = List.objects.get(id = fk)
            tasks = the_list.tasks.all()
            context = {
                'tasks': tasks.filter(name__contains = search),
                'form': form,
                'fk': fk,
            }
            return render(request, 'main/todo_list.html', context)
    
    if request.GET.get('order', '') != '':
        the_list = List.objects.get(id = fk)
        tasks = the_list.tasks.all()
        context = {
            'tasks': tasks.order_by('name'),
            'list': the_list,
            'fk': fk,
        }        
        return render(request, 'main/completed_todo_list.html', context)
    
    the_list = List.objects.get(id = fk)
    tasks = the_list.tasks.all()
    context = {
        'tasks': tasks,
        'list': the_list,
        'fk': fk,
    }

    return render(request, 'main/completed_todo_list.html', context)

def show_lists(request):

    if request.method == 'GET':
        form = SearchListForm(request.GET or None) 
        print(form.errors)
        if form.is_valid():
           
            search = form.cleaned_data['name']
            
            context = {
                'lists': List.objects.filter(name__contains = search),
                'form': form
            }
            print('ctx', context)
            return render(request, 'index.html', context)
        
        if request.GET.get('order', '') != '':
            context = {
                'lists': List.objects.order_by('name')
            }
            return render(request, 'index.html', context)

    form = SearchListForm() 
    context = {
        'lists': List.objects.all(),    
    }
    return render(request, 'index.html', context)

def new_task(request, fk):
    if request.method == 'POST':
        form = TaskForm(request.POST or None)
        print(form.errors)
        if form.is_valid():
            print("ads")
            name = form.cleaned_data['name']
            due_on = form.cleaned_data['due_on']
            owner = form.cleaned_data['owner']
            created = models.DateTimeField()
            due_on = models.DateTimeField()
            task = Task()
            task.name = name 
            task.created = datetime.now()
            task.due_on = due_on
            task.owner = owner 
            task.mark = False 
            task.list_id = List.objects.get(pk=fk)
            task.save()
            return redirect('<fk>/todolist')
    

    form = TaskForm()
    context = {
        'form': form,
        'users': User.objects.all(),
        'fk': fk
    }
    return render(request, 'main/add_task.html', context)

def new_list(request):
    if request.method == 'POST':
        form = ListForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = ListForm()
    context = {
        'form': form
    }
    return render(request, 'main/add_list.html', context)

def make_done_task(request, fk, pk):
    task = Task.objects.get(pk= pk)
    task.mark = True
    task.save()
    messages.success(request, ('Task has been done!'))
    return redirect('../todolist')

def make_notdone_task(request, fk, pk):
    task = Task.objects.get(pk= pk)
    task.mark = False
    task.save()
    messages.success(request, ('Task has not been done!'))
    return redirect('../todolist')

def delete_list(request, fk):
    the_list = List.objects.get(pk= fk)
    the_list.delete()
    return redirect('..')