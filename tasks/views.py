from django.shortcuts import render, get_object_or_404, redirect
from .models import Session, Weekend, Task
from django.contrib.auth.decorators import login_required
from accounts.models import User
from .forms import TaskForm


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
    tasks = user.task_set.all()
    context = {
        'sessions': sessions,
        'user': user,
        'tasks': tasks,
        'count': tasks.count()
    }
    return render(request, 'tasks/profile.html', context)


@login_required
def weekend_detail(request, pk):
    sessions = Session.objects.all()
    weekend = get_object_or_404(Weekend, pk=pk)

    if request.user.profile.position == 'STUDENT':
        tasks = Task.objects.filter(user=request.user, weekend=weekend)
        form = TaskForm()

        if request.method == 'POST':
            form = TaskForm(request.POST, request.FILES)
            if form.is_valid():
                form = form.save(commit=False)
                form.user = request.user
                form.weekend = weekend
                form.save()
                return redirect('weekend_detail', weekend.pk)

        context = {
            'sessions': sessions,
            'weekend': weekend,
            'form': form,
            'tasks': tasks
        }
        return render(request, 'tasks/task.html', context)

    else:
        tasks = Task.objects.filter(weekend=weekend)
        context = {
            'sessions': sessions,
            'weekend': weekend,
            'tasks': tasks,
        }
        return render(request, 'tasks/task.html', context)



@login_required
def create_task(request):
    sessions = Session.objects.all()

    context = {
        'sessions': sessions
    }
    return render(request, 'tasks/task.html', context)
