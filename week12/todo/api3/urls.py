from . import views
from django.urls import path

urlpatterns = [
    path('lists/', views.ListView.as_view()),
    path('login/', views.login),
    path('lists/<int:pk>/', views.ListDetailView.as_view()),
    path('lists/<int:fk>/tasks/', views.TaskView.as_view()),
]