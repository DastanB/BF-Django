from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('posts/', views.post_list, name='posts'),
    path('posts/<int:pk>/', views.post_detail, name='posts_detail'),
    path('comments/', views.comment_list, name='comments'),
    path('comments/<int:pk>/', views.comment_detail, name='comments_detail'),
    
]