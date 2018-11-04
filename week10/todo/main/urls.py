from django.contrib import admin
from django.urls import path, include, re_path
from . import views
from .views import (
    ListListView, 
    ListCreateView, 
    ListUpdateView, 
    ListDeleteView,
    TodoView, 
    DoneView, 
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView
)
urlpatterns = [
    path('', ListListView.as_view(), name='index'),
    path('new_list', ListCreateView.as_view(), name='add_list'),
    path('<int:fk>/todolist', TodoView.as_view(), name = 'todo_list'),
    path('<int:fk>/donelist', DoneView.as_view(), name ='done_list'),
    path('<int:pk>/delete_list', ListDeleteView.as_view(), name='delete_list'),
    path('<int:pk>/update_list', ListUpdateView.as_view(), name='update_list'),
    path('<int:fk>/new_task', TaskCreateView.as_view(), name="add_task"),
    path('<int:fk>/updatetask/<int:pk>', views.make_done_task),
    path('<int:fk>/updatealltask/<int:pk>', TaskUpdateView.as_view(), name='update_task'),
    path('<int:fk>/tasknotdone/<int:pk>', views.make_notdone_task),
    path('<int:fk>/deletetask/<int:pk>', TaskDeleteView.as_view(), name="delete_task"),
]
