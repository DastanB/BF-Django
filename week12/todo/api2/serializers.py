from rest_framework import serializers
from main.models import List, Task
from django.contrib.auth.models import User


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(max_length=300)
    email = serializers.EmailField()
    is_staff = serializers.BooleanField()
    # class Meta:
    #     model = User
    #     fields = ('id', 'username', 'email', )


class ListSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=200)
    
    def create(self, validated_data):
        the_list = List(**validated_data)
        the_list.save()
        return the_list

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance


class ListModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = List
        fields = ['id', 'name', ]

class TaskSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=200)
    created = serializers.DateTimeField()
    due_on = serializers.DateTimeField()
    owner = UserSerializer(read_only=True)
    mark = serializers.BooleanField()
    list_id = ListSerializer(read_only=True)
    
    def create(self, validated_data):
        task = Task(**validated_data)
        task.save()
        return task

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.due_on = validated_data.get('due_on', instance.due_on)
        instance.save()
        return instance


class TaskModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'name', 'created', 'due_on', 'owner', 'mark', 'list_id']