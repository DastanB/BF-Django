from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
# Create your models here.
class List(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Task(models.Model):
    name = models.CharField(max_length = 255)
    created = models.DateTimeField(default=datetime.now())
    due_on = models.DateTimeField(default=None)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    mark = models.BooleanField(default = False)
    list_id = models.ForeignKey(List, on_delete=models.CASCADE, default=None, related_name='tasks')

    def __str__(self):
        return self.name