from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
# Create your models here.
class List(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
        }

    def __str__(self):
        return self.name


class Task(models.Model):
    name = models.CharField(max_length = 255)
    created = models.DateTimeField(default=datetime.now())
    due_on = models.DateTimeField(default=None)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mark = models.BooleanField(default = False)
    list = models.ForeignKey(List, on_delete=models.CASCADE, default=None, related_name='tasks')

    def __str__(self):
        return self.name
    
    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'created': self.created,
            'due_on': self.due_on,
            'owner': self.owner,
            'mark': self.mark,
            'list_id': self.list_id
        }