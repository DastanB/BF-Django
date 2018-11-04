from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.urls import reverse_lazy
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Categories'


class PostManager(models.Manager):
    def for_user(self, user):
        return self.filter(user=user)

class CommentManager(models.Manager):
    def for_user(self, user):
        return self.filter(user=user)

class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.CharField(max_length=30000)
    published = models.DateTimeField(default = datetime.now(), null=True)
    user = models.ForeignKey(User, on_delete = models.CASCADE, related_name='posts')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='posts_of_category')
    image = models.ImageField(upload_to='static/images/posts', blank=True)

    objects = PostManager()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse_lazy('index')

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments_of_user')
    published = models.DateTimeField(default = datetime.now())
    message = models.CharField(max_length=30000)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')


    objects = CommentManager()

    def __str__(self):
        return self.message 

    def get_absolute_url(self):
        return reverse_lazy('index')