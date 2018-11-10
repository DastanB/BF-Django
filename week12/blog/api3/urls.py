from django.urls import path, include
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('posts/', views.PostGenView.as_view()),
    path('posts/<int:pk>/', views.PostDetailGenView.as_view()),
    path('posts/<int:fk>/comments/', views.CommentView.as_view()),
    path('posts/<int:fk>/comments/<int:pk>/', views.CommentGenDetailView.as_view()),
    path('login/', views.login),
    path('logout/', views.logout),
    path('register/', views.register),
]

urlpatterns = format_suffix_patterns(urlpatterns)