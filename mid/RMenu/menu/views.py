from django.shortcuts import render, redirect
from .models import City, Restaurant, Dish, Review, RestaurantReview, DishReview
from .forms import RestForm, UpdateRestForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.views import View
# Create your views here.
class IndexView(View):
    def get(self, request):
        cities = City.objects.all()
        context = {
            'cities': cities,
        }
        return render(request, 'index.html', context)

class RestaurantView(View):
    def get(self, request, pk):
        city = City.objects.get(pk=pk)
        rests = Restaurant.objects.filter(city=pk)
        context = {
            'city': city, 
            'restaurants': rests,
        }
        return render(request, 'menu/restaurants.html', context)


class AddRestView(View):
    
    def get(self, request):
        form = RestForm()
        context = {
            'form': form,
            'users': User.objects.all(),
            'cities': City.objects.all()
        }
        return render(request, 'menu/add_rest.html', context)

    def post(self, request):
        form = RestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    
class DelRestView(View):
    def get(self, request, pk, fk):
        rest = Restaurant.objects.get(pk=pk)
        rest.delete()
        return redirect('index')

class DishesView(View):
    def get(self, request, pk, fk):
        rest = Restaurant.objects.get(pk=pk)
        dishes = rest.dishes.all()
        reviews = RestaurantReview.objects.filter(restaurant=pk)
        context = {
            'rest': rest,
            'dishes': dishes,
            'reviews': reviews
        }

        return render(request, 'menu/dishes.html', context)

