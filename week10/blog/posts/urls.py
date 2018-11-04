from django.contrib import admin
from django.urls import path, include
from . import views
from .views import ( 
    PostListView, 
    PostDetailView, 
    PostCreateView, 
    PostUpdateView, 
    PostDeleteView, 
    PostDetView, 
    CommentCreateView, 
    CommentUpdateView,
    CommentDeleteView
    )

urlpatterns = [
    path('', PostListView.as_view(), name='index'),
    path('<int:pk>/', PostDetView.as_view(), name='post_detail'),
    path('<int:pk>/update', PostUpdateView.as_view(), name= 'post_update'),
    path('<int:pk>/delete', PostDeleteView.as_view(), name='post_delete'),
    path('add_post/', PostCreateView.as_view(), name='post_create'),
    path('<int:fk>/add_comment', CommentCreateView.as_view()),
    path('<int:fk>/update_comment/<int:pk>', CommentUpdateView.as_view()),
    path('<int:fk>/delete_comment/<int:pk>', views.CommentDeleteView.as_view()),
]
