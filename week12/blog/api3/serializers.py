from rest_framework import serializers
from posts.models import Post, Comment
from django.contrib.auth.models import User

class UserModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']

class PostModelSerializer(serializers.ModelSerializer):
    user = UserModelSerializer(read_only=True)
    class Meta:
        model = Post
        fields = ['id', 'title', 'body', 'published', 'user']

class CommentModelSerializer(serializers.ModelSerializer):
    post = PostModelSerializer(read_only=True)
    user = UserModelSerializer(read_only=True)
    class Meta:
        model = Comment
        fields = ['id', 'user', 'published', 'message', 'post']