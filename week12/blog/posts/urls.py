from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>/', views.post_details),
    path('<int:pk>/update', views.update_post),
    path('<int:pk>/delete', views.delete_post),
    path('add_post/', views.add_post),
    path('<int:fk>/add_comment', views.add_comment),
    path('<int:fk>/update_comment/<int:pk>', views.update_comment),
    path('<int:fk>/delete_comment/<int:pk>', views.delete_comment),
]
