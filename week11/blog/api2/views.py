from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from posts.models import Post, Comment
from .serializers import PostSerializer, PostModelSerializer, CommentSerializer, CommentModelSerializer
import json


@csrf_exempt
def post_list(request):
    if request.method == 'GET':
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = json.loads(request.body)
        serializer = PostModelSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse({'error': 'invalid data'})


@csrf_exempt
def post_detail(request, pk):
    try:
        post = Post.objects.get(id=pk)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=404)

    if request.method == 'GET':
        serializer = PostModelSerializer(post)
        return JsonResponse(serializer.data)
    elif request.method == 'PUT':
        data = json.loads(request.body)
        serializer = PostModelSerializer(instance=post, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse({'error': 'invalid data'})
    elif request.method == 'DELETE':
        post.delete()
        return JsonResponse({'deleted': True})

@csrf_exempt
def comment_list(request):
    if request.method == 'GET':
        comments = Comment.objects.all()
        serializer = CommentSerializer(comments, many=True)
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = json.loads(request.body)
        serializer = CommentModelSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse({'error': 'invalid data'})


@csrf_exempt
def comment_detail(request, pk):
    try:
        comment = Comment.objects.get(id=pk)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=404)

    if request.method == 'GET':
        serializer = CommentModelSerializer(comment)
        return JsonResponse(serializer.data)
    elif request.method == 'PUT':
        data = json.loads(request.body)
        serializer = CommentModelSerializer(instance=comment, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse({'error': 'invalid data'})
    elif request.method == 'DELETE':
        comment.delete()
        return JsonResponse({'deleted': True})
