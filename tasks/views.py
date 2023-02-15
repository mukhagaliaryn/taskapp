from django.shortcuts import render, get_object_or_404
from .models import Session, Weekend, Task
from django.contrib.auth.decorators import login_required
from accounts.models import User


@login_required
def index(request):
    sessions = Session.objects.all()
    users = User.objects.filter(profile__position='STUDENT')
    context = {
        'sessions': sessions,
        'users': users
    }
    return render(request, 'tasks/index.html', context)


@login_required
def user_detail(request, username):
    sessions = Session.objects.all()
    user = get_object_or_404(User, username=username)
    context = {
        'sessions': sessions,
        'user': user
    }
    return render(request, 'accounts/profile.html', context)


@login_required
def create_task(request):
    sessions = Session.objects.all()

    context = {
        'sessions': sessions
    }
    return render(request, 'tasks/task.html', context)
