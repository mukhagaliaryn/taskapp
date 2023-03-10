from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('user/<username>/', views.user_detail, name='user_detail'),
    path('week/<pk>/', views.weekend_detail, name='weekend_detail'),
    path('task/', views.create_task, name='create_task'),
]
