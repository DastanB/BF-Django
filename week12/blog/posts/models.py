from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.CharField(max_length=30000)
    published = models.DateTimeField(default = datetime.now(), null=True)
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name='posts')

    def __str__(self):
        return self.title
    
    def to_json(self):
        return {
            'title': self.title,
            'body': self.body,
            'published': self.published,
        }

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments_of_user')
    published = models.DateTimeField(default = datetime.now())
    message = models.CharField(max_length=30000)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')

    def __str__(self):
        return self.message
    
    def to_json(self):
        return {
            'published': self.published,
            'message': self.message,
        }