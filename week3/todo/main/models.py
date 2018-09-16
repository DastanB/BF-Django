from django.db import models

# Create your models here.
class Task(models.Model):
    
    name = models.CharField(max_length = 255)
    created = models.DateTimeField()
    due_on = models.DateTimeField()
    owner = models.CharField(max_length = 255)
    mark = models.BooleanField(default = False)