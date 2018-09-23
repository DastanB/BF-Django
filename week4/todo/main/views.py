from django.shortcuts import render
from .models import Task, List
from .forms import SearchListForm

# Create your views here.
def to_do_list(request, fk):
    if request.method == 'GET':
        form = SearchListForm(request.GET) 
        if form.is_valid():
            search = form.cleaned_data['name']
            tasks = Task.objects.all().filter(list_id = fk)
            list_of = List.objects.get(id = fk)
            context = {
                'tasks': tasks.filter(name__contains = search),
                'form': form
            }
            return render(request, 'main/todo_list.html', context)
    
    if request.GET.get('order', '') != '':
        tasks = Task.objects.all().filter(list_id = fk)
        list_of = List.objects.get(id = fk)
        context = {
            'tasks': tasks.order_by("name"),
            'list': list_of,
        }        
        return render(request, 'main/todo_list.html', context)
    
    tasks = Task.objects.all().filter(list_id = fk)
    list_of = List.objects.get(id = fk)
    context = {
        'tasks': tasks,
        'list': list_of,
    }

    return render(request, 'main/todo_list.html', context)

def done_list(request, fk):
    
    if request.method == 'GET':
        form = SearchListForm(request.GET) 
        if form.is_valid():
            search = form.cleaned_data['name']
            tasks = Task.objects.all().filter(list_id = fk)
            list_of = List.objects.get(id = fk)
            context = {
                'tasks': tasks.filter(name__contains = search),
                'form': form
            }
            return render(request, 'main/todo_list.html', context)
    
    if request.GET.get('order', '') != '':
        tasks = Task.objects.all().filter(list_id = fk)
        list_of = List.objects.get(id = fk)
        context = {
            'tasks': tasks.order_by('name'),
            'list': list_of,
        }        
        return render(request, 'main/completed_todo_list.html', context)
    
    tasks = Task.objects.all().filter(list_id = fk)
    list_of = List.objects.get(id = fk)
    context = {
        'tasks': tasks,
        'list': list_of,
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