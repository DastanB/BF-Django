from django.shortcuts import render
from .models import Task

# Create your views here.
def ToDoList(request):
    tasks = list()

    task1 = Task()
    task1.name = 'Task1'
    task1.created = '10.09.2018'
    task1.due_on = '12.09.2018'
    task1.owner = 'admin'
    
    task2 = Task()
    task2.name = 'Task1'
    task2.created = '10.09.2018'
    task2.due_on = '12.09.2018'
    task2.owner = 'admin'
    
    task3 = Task()
    task3.name = 'Task1'
    task3.created = '10.09.2018'
    task3.due_on = '12.09.2018'
    task3.owner = 'admin'
    
    task4 = Task()
    task4.name = 'Task1'
    task4.created = '10.09.2018'
    task4.due_on = '12.09.2018'
    task4.owner = 'admin'
    
    tasks.append(task1)
    tasks.append(task2)
    tasks.append(task3)
    tasks.append(task4)
    
    context = {
        'tasks': tasks,
    }

    return render(request, 'main/todo_list.html', context)

def DoneList(request):
    
    tasks = list()

    task0 = Task()
    task0.name = 'Task0'
    task0.created = '10.09.2018'
    task0.due_on = '12.09.2018'
    task0.owner = 'admin'
    task0.mark = True

    tasks.append(task0)

    context = {
        'tasks': tasks,    
    }

    return render(request, 'main/completed_todo_list.html', context)
