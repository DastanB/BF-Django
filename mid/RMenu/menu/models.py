from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class City(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Restaurant(models.Model):
    name = models.CharField(max_length=255)
    telephone = models.CharField(max_length=12)
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='restaurants')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Dish(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    price = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='dishes')

    def __str__(self):
        return self.name

class Review(models.Model):
    rating = models.IntegerField()
    comment = models.CharField(max_length=1000)
    date = models.DateField()

    def __str__(self):
        return self.comment

class RestaurantReview(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='reviews')
    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name='rest_reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.restaurant.__str__()


class DishReview(models.Model):
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE, related_name='reviews')
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.dish.__str__()