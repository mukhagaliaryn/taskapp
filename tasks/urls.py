from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('user/<username>/', views.user_detail, name='user_detail'),
    path('projects/', views.projects, name='projects'),
    path('solutions/', views.solutions, name='solutions'),
    # path('task/<pk>/', views.task_detail, name='task_detail'),
]
