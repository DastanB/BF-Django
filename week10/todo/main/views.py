from django.shortcuts import render, redirect
from .models import Task, List
from .forms import SearchListForm, TaskForm, ListForm, UpdateTaskForm
from django.contrib.auth.models import User
from django.db import models
from django.utils.dateparse import parse_datetime
from datetime import datetime
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.generic import (
    TemplateView,
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    View
)
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
# Create your views here.
class TodoView(View):
    def get(self, request, fk):
        if request.GET.get('order', '') != '':
            the_list = List.objects.get(id = fk)
            tasks = the_list.tasks.all()
            context = {
                'tasks': tasks.order_by("name"),
                'list': the_list,
                'fk': fk,
            }        
            
        else:
            the_list = List.objects.get(id = fk)
            tasks = the_list.tasks.all()
            context = {
                'tasks': tasks,
                'list': the_list,
                'fk': fk,
            }    
        
        return render(request, 'main/todo_list.html', context)

class DoneView(View):
    def get(self, request, fk):
        if request.GET.get('order', '') != '':
            the_list = List.objects.get(id = fk)
            tasks = the_list.tasks.all()
            context = {
                'tasks': tasks.order_by("name"),
                'list': the_list,
                'fk': fk,
            }        
            
        else:
            the_list = List.objects.get(id = fk)
            tasks = the_list.tasks.all()
            context = {
                'tasks': tasks,
                'list': the_list,
                'fk': fk,
            }    
        
        return render(request, 'main/completed_todo_list.html', context)

class ListListView(ListView):
    model = List
    context_object_name = 'lists'

class ListCreateView(CreateView):
    model = List
    fields = ['name',]
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class ListUpdateView(UpdateView):
    model = List
    fields = ['name',]
    success_url = reverse_lazy('index')

    def get_queryset(self):
        return List.objects.filter(pk=self.kwargs['pk'])

class ListDeleteView(LoginRequiredMixin, DeleteView):
    model = List
    success_url = reverse_lazy('index')

    def get_queryset(self):
        return List.objects.filter(pk=self.kwargs['pk'])

class TaskCreateView(CreateView, LoginRequiredMixin):
    model = Task
    fields = ['name', 'due_on', ]
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        form.instance.list_id = List.objects.get(pk=self.kwargs['fk'])
        form.save()
        return super().form_valid(form)

class TaskUpdateView(UpdateView, LoginRequiredMixin):
    model = Task
    fields = ['name', 'due_on', ]
    success_url = reverse_lazy('index')

    def get_queryset(self):
        return Task.objects.filter(pk=self.kwargs['pk'])

class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = List
    success_url = reverse_lazy('index')

    def get_queryset(self):
        return Task.objects.filter(pk=self.kwargs['pk'])
 
@login_required
def make_done_task(request, fk, pk):
    task = Task.objects.get(pk= pk)
    task.mark = True
    task.save()
    messages.success(request, ('Task has been done!'))
    return redirect('../todolist')

@login_required
def make_notdone_task(request, fk, pk):
    task = Task.objects.get(pk= pk)
    task.mark = False
    task.save()
    messages.success(request, ('Task has not been done!'))
    return redirect('../todolist')

@login_required
def delete_task(request, fk, pk):
    task = Task.objects.get(pk= pk)
    task.delete()
    messages.success(request, ('Task has been deleted!'))
    return redirect('../todolist')

@login_required
def update_task(request, fk, pk):
    if request.method == 'POST':
        form = UpdateTaskForm(request.POST or None)
        print(form.errors)
        if form.is_valid():
            name = form.cleaned_data['name']
            due_on = form.cleaned_data['due_on']
            
            task = Task.objects.get(pk=pk)
            task.name = name 
            task.due_on = due_on
            task.save()
            return redirect('../todolist')
    

    form = UpdateTaskForm()
    context = {
        'form': form,
        'fk': fk,
        'task': Task.objects.get(pk=pk)
    }
    return render(request, 'main/update_task.html', context)
