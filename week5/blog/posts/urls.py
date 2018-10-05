from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('<int:pk>/', views.post_details),
    path('add_post/', views.add_post),
    path('<int:fk>/add_comment', views.add_comment)
]
