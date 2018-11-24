from rest_framework import serializers
from .models import List, Task
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']

class ListSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = List
        fields = ['id', 'name', 'user']

class TaskSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    list = ListSerializer(read_only=True)
    class Meta:
        model = Task
        fields = ['id', 'name', 'created', 'due_on', 'user', 'mark', 'list']