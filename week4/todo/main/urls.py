from django.contrib import admin
from django.urls import path, include, re_path
from . import views

urlpatterns = [
    path('', views.show_lists),
    path('<int:fk>/todolist', views.to_do_list),
    path('<int:fk>/donelist', views.done_list),
]
