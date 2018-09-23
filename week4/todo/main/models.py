from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class List(models.Model):
    name = models.CharField(max_length=255)


class Task(models.Model):
    name = models.CharField(max_length = 255)
    created = models.DateTimeField()
    due_on = models.DateTimeField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    mark = models.BooleanField(default = False)
    list_id = models.ForeignKey(List, on_delete=models.CASCADE, default=None)