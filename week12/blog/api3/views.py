from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth import authenticate
from posts.models import Post, Comment
from .serializers import PostModelSerializer, CommentModelSerializer, UserModelSerializer
from django.http import Http404
from django.contrib.auth.models import User
# Create your views here.
class PostView(APIView):
    def get(self, request):
        posts = Post.objects.all()
        serializer = PostModelSerializer(posts, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PostModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

class PostDetailView(APIView):
    def get_object(self, pk):
        try:
            return Post.objects.get(id=pk)
        except Post.DoesNotExist:
            return Http404

    def get(self, request, pk):
        post = Post.objects.get(id=pk)
        serializer = PostModelSerializer(post)
        return Response(serializer.data)

    def put(self, request, pk):
        post = Post.objects.get(id=pk)
        serializer = PostModelSerializer(instance=post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        post = Post.objects.get(id=pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class PostGenView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostModelSerializer
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)

class PostDetailGenView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostModelSerializer

    def get_object(self):
        return Post.objects.get(id=self.kwargs['pk'])

class CommentView(APIView):
    def get(self, request, fk):
        comments = Comment.objects.filter(post_id=fk)
        serializer = CommentModelSerializer(comments, many=True)
        return Response(serializer.data)

    def post(self, request, fk):
        serializer = CommentModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(post=Post.objects.get(id=self.kwargs["fk"]), user=User.objects.first())
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

class CommentDetailView(APIView):
    def get_object(self, fk, pk):
        try:
            return Comment.objects.get(id=pk)
        except:
            return Http404

    def get(self, request, fk, pk):
        comment = Comment.objects.get(id=pk)
        serializer = CommentModelSerializer(comment)
        return Response(serializer.data)

    def put(self, request, fk, pk):
        comment = Comment.objects.get(id=pk)
        serializer = CommentModelSerializer(instance=comment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, fk, pk):
        comment = Comment.objects.get(id=pk)
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class CommentGenView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentModelSerializer

    def get_queryset(self):
        return Comment.objects.filter(post=self.kwargs["fk"])

    def perform_create(self, serializer):
        serializer.save(post=Post.objects.get(id=self.kwargs["fk"]), user=User.objects.first())

class CommentGenDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentModelSerializer

    def get_queryset(self):
        return Comment.objects.filter(post=self.kwargs["fk"])

@api_view(['POST'])
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(username=username, password=password)
    if user is None:
        return Response({'error': 'Invalid data'})
    token, created = Token.objects.get_or_create(user=user)
    return Response({'token': token.key})

@api_view(['GET'])
def logout(request):
    request.user.auth_token.delete()
    return Response(status=status.HTTP_200_OK)

@api_view(['POST'])
def register(request):
    serialized = UserModelSerializer(data=request.data)
    if serialized.is_valid():
        User.objects.create_user(
            request.data.get('username'),
            request.data.get('email'),
            request.data.get('password')
        )
        return Response(serialized.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serialized._errors, status=status.HTTP_400_BAD_REQUEST)