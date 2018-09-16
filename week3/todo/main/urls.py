from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.ToDoList),
    path('donelist', views.DoneList),
]
