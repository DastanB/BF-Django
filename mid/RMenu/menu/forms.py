from django import forms
from .models import City, Restaurant, Dish, Review, RestaurantReview, DishReview

class RestForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = ('name', 'telephone', 'city', 'user')

class UpdateRestForm(forms.Form):
    name = forms.CharField(max_length=255)
    telephone = forms.CharField(max_length=255)