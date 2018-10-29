from django.contrib import admin
from django.urls import path, include
from . import views
from .views import IndexView, RestaurantView, AddRestView, DelRestView, DishesView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('<int:pk>/', RestaurantView.as_view()),
    path('addrest/', login_required(AddRestView.as_view()), name="add_rest"),
    path('<int:fk>/delete/<int:pk>/', login_required(DelRestView.as_view())),
    path('<int:fk>/dishes/<int:pk>/', DishesView.as_view()),
]