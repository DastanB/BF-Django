from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('lists/', views.list_list, name='lists'),
    path('lists/<int:pk>', views.list_detail, name='lists_detail'),
    path('tasks/', views.task_list, name='tasks'),
    path('tasks/<int:pk>', views.task_detail, name='tasks_detail'),
]