from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('task/', views.create_task, name='create_task'),
]
