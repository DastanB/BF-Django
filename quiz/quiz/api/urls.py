from django.urls import path, include
from .views import AdvertGenDetail, AdvertGenList, AdvertGenDelete, AdvertGenUpdate, AdvertGenCreate
from . import views
urlpatterns = [
    path('login/', views.login),
    path('register/', views.register),
    path('ads/', views.adverList),
    path('ads/', AdvertGenList.as_view()),
    # path('ads/create/', views.advertCreate),
    path('ads/create/', AdvertGenCreate.as_view()),
    # path('ads/<int:pk>/',views.advertDetails),
    path('ads/<int:pk>/',AdvertGenDetail.as_view()),
    # path('ads/delete/<int:pk>/', views.advertDelete),
    path('ads/delete/<int:pk>/', AdvertGenDelete.as_view()),
    # path('ads/update/<int:pk>/', views.advertUpdate),
    path('ads/update/<int:pk>/', AdvertGenUpdate.as_view()),
]