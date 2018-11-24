from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Advert(models.Model):
    title = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    description = models.CharField(max_length=10000)
    price = models.IntegerField()
    number_views = models.IntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name