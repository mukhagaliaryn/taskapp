from django.shortcuts import render
from .models import Session, Weekend, Task


def index(request):
    sessions = Session.objects.all()

    context = {
        'sessions': sessions
    }
    return render(request, 'tasks/index.html', context)


def create_task(request):
    sessions = Session.objects.all()

    context = {
        'sessions': sessions
    }
    return render(request, 'tasks/task.html', context)
