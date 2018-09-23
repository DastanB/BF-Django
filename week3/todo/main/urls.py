from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.to_do_list),
    path('donelist', views.done_list),
]
