from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.urls import reverse_lazy
# Create your models here.
class ListManager(models.Manager):
    def for_list(self, List):
        return self.filter(id=List.id)

class TaskManager(models.Manager):
    def for_user(self, owner):
        return self.filter(owner=owner)

class List(models.Model):
    name = models.CharField(max_length=255)

    objects = ListManager()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse_lazy('index')

class Task(models.Model):
    name = models.CharField(max_length = 255)
    created = models.DateTimeField(default=datetime.now())
    due_on = models.DateTimeField(default=None)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    mark = models.BooleanField(default = False)
    list_id = models.ForeignKey(List, on_delete=models.CASCADE, default=None, related_name='tasks')

    objects = TaskManager()

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse_lazy('index')