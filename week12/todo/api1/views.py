from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User

from main.models import Task, List
# Create your views here.
@csrf_exempt
def list_list(request):
    if request.method == 'GET':
        lists = List.objects.all()
        for l in lists:
            l.to_json()
        return JsonResponse(lists, safe=False)
    elif request.method == 'POST':
        data = json.loads(request.body)
        the_list = List(name=data['name'])
        the_list.save()
        return JsonResponse(the_list.to_json())

@csrf_exempt
def list_detail(request, pk):
    try:
        the_list = List.objects.get(id=pk)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=404)

    if request.method == 'GET':
        return JsonResponse(the_list.to_json())
    elif request.method == 'PUT':
        data = json.loads(request.body)
        the_list.name = data.get('name', the_list.name)
        the_list.save()
        return JsonResponse(the_list.to_json())
    elif request.method == 'DELETE':
        the_list.delete()
        return JsonResponse({'deleted': True}, status=204)

@csrf_exempt
def task_list(request):
    if request.method == 'GET':
        tasks = Task.objects.all()
        for task in tasks:
            task.to_json()
        return JsonResponse(Task.objects.first().to_json(), safe=False)
    elif request.method == 'POST':
        data = json.loads(request.body)
        the_list = Task(
            name=data['name'], 
            created=data['created'], 
            due_on=data['due_on'], 
            owner=data['due_on'], 
            mark=data['mark'], 
            list_id=data['list_id']
        )
        the_list.save()
        return JsonResponse(the_list.to_json())

@csrf_exempt
def task_detail(request, pk):
    try:
        task = Task.objects.get(id=pk)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=404)

    if request.method == 'GET':
        return JsonResponse(task.to_json(), safe=False)
    elif request.method == 'PUT':
        data = json.loads(request.body)
        task.name = data.get('name', task.name)
        task.due_on = data.get('due_on', task.due_on)
        task.save()
        return JsonResponse(task.to_json())
    elif request.method == 'DELETE':
        task.delete()
        return JsonResponse({'deleted': True}, status=204)