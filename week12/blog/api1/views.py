from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User

from posts.models import Post, Comment
# Create your views here.
@csrf_exempt
def post_list(request):
    if request.method == 'GET':
        posts = Post.objects.all()
        for p in posts:
            p.to_json()
        return JsonResponse(posts, safe=False)
    elif request.method == 'POST':
        data = json.loads(request.body)
        post = Post(
            title=data['title'],
            body=data['body'],
            published=data['published'],
            user=data['user'],
        )
        post.save()
        return JsonResponse(post.to_json())

@csrf_exempt
def post_detail(request, pk):
    try:
        post = Post.objects.get(id=pk)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=404)

    if request.method == 'GET':
        return JsonResponse(post.to_json())
    elif request.method == 'PUT':
        data = json.loads(request.body)
        post.title = data.get('title', post.title)
        post.body = data.get('body', post.body)
        post.save()
        return JsonResponse(post.to_json())
    elif request.method == 'DELETE':
        post.delete()
        return JsonResponse({'deleted': True}, status=204)

@csrf_exempt
def comment_list(request):
    if request.method == 'GET':
        comments = Comment.objects.all()
        for comment in comments:
            comment.to_json()
        return JsonResponse(Comment.objects.first().to_json(), safe=False)
    elif request.method == 'POST':
        data = json.loads(request.body)
        comment = Comment(
            name=data['name'], 
            created=data['created'], 
            due_on=data['due_on'], 
            owner=data['due_on'], 
            mark=data['mark'], 
            list_id=data['list_id']
        )
        comment.save()
        return JsonResponse(comment.to_json())

@csrf_exempt
def comment_detail(request, pk):
    try:
        comment = Comment.objects.get(id=pk)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=404)

    if request.method == 'GET':
        return JsonResponse(comment.to_json(), safe=False)
    elif request.method == 'PUT':
        data = json.loads(request.body)
        comment.name = data.get('name', comment.name)
        comment.due_on = data.get('due_on', comment.due_on)
        comment.save()
        return JsonResponse(comment.to_json())
    elif request.method == 'DELETE':
        comment.delete()
        return JsonResponse({'deleted': True}, status=204)