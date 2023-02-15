from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from tasks.models import Session


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'accounts/register.html', {'form': form})


@login_required
def profile(request):
    sessions = Session.objects.all()
    tasks = request.user.task_set.all()
    context = {
        'sessions': sessions,
        'tasks': tasks,
        'count': tasks.count()
    }
    return render(request, 'accounts/profile.html', context)