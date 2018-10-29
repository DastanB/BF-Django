from django.contrib import admin
from .models import City, Restaurant, Dish, Review, RestaurantReview, DishReview

# Register your models here.
admin.site.register(City)
admin.site.register(Restaurant)
admin.site.register(Dish)
admin.site.register(Review)
admin.site.register(RestaurantReview)
admin.site.register(DishReview)