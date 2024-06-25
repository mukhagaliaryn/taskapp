from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('user/<username>/', views.user_detail, name='user_detail'),
    path('projects/', views.projects, name='projects'),
    path('solutions/', views.solutions, name='solutions'),
    path('users/', views.users, name='users'),
    path('project/<id>/', views.project_detail, name='project_detail'),
    path('task/', views.task_send, name='task_send'),
]
