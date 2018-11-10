from rest_framework import serializers
from posts.models import Post, Comment
from django.contrib.auth.models import User


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(max_length=300)
    email = serializers.EmailField()
    is_staff = serializers.BooleanField()
    # class Meta:
    #     model = User
    #     fields = ('id', 'username', 'email', )


class PostSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=255)
    body = serializers.CharField(max_length=255)
    published = serializers.DateTimeField()
    user = UserSerializer(read_only=True)
    
    def create(self, validated_data):
        post = Post(**validated_data)
        post.save()
        return post

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.body = validated_data.get('body', instance.body)
        instance.save()
        return instance


class PostModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'title', 'body', 'published', 'user']

class CommentSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    user = UserSerializer(read_only=True)
    published = serializers.DateTimeField()
    message = serializers.CharField(max_length=30000)
    post = PostSerializer(read_only=True)
    
    def create(self, validated_data):
        task = Comment(**validated_data)
        task.save()
        return task

    def update(self, instance, validated_data):
        instance.message = validated_data.get('message', instance.message)
        instance.save()
        return instance


class CommentModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'user', 'published', 'message', 'post']