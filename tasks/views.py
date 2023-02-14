from django.shortcuts import render


def index(request):
    return render(request, 'tasks/index.html', {})


def create_task(request):
    return render(request, 'tasks/task.html', {})
