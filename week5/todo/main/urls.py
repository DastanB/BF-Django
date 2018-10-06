from django.contrib import admin
from django.urls import path, include, re_path
from . import views

urlpatterns = [
    path('', views.show_lists, name='index'),
    path('new_list', views.new_list),
    path('<int:fk>/todolist', views.to_do_list),
    path('<int:fk>/donelist', views.done_list),
    path('<int:fk>/delete_list', views.delete_list),
    path('<int:pk>/update_list', views.update_list),
    path('<int:fk>/new_task', views.new_task, name="add_task"),
    path('<int:fk>/updatetask/<int:pk>', views.make_done_task),
    path('<int:fk>/updatealltask/<int:pk>', views.update_task),
    path('<int:fk>/tasknotdone/<int:pk>', views.make_notdone_task),
    path('<int:fk>/deletetask/<int:pk>', views.delete_task),
]
