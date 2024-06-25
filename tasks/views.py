from django.shortcuts import render, get_object_or_404, redirect

from .forms import SolutionForm
from .models import Project, Task, Solution
from django.contrib.auth.decorators import login_required
from accounts.models import User


@login_required
def index(request):
    context = {}
    if request.user.profile.position == 'STAFF':
        projects = Project.objects.all()[:5]
        solutions = Solution.objects.filter(user=request.user)[:5]
        context['projects'] = projects
        context['solutions'] = solutions

    elif request.user.profile.position == 'ADMIN':
        users = User.objects.exclude(is_superuser=True)[:5]
        projects = Project.objects.all()[:5]
        solutions = Solution.objects.all()[:5]

        context['users'] = users
        context['projects'] = projects
        context['solutions'] = solutions
    return render(request, 'tasks/index.html', context)


@login_required
def users(request):
    all_users = User.objects.all()
    context = {
        'users': all_users
    }
    return render(request, 'tasks/users.html', context)


@login_required
def user_detail(request, username):
    user = get_object_or_404(User, username=username)
    solutions = user.solution_set.all()
    context = {
        'user': user,
        'solutions': solutions,
        'count': solutions.count()
    }
    return render(request, 'tasks/profile.html', context)


@login_required
def projects(request):
    all_projects = Project.objects.all()
    context = {
        'projects': all_projects
    }
    return render(request, 'tasks/projects.html', context)


@login_required
def project_detail(request, id):
    project = get_object_or_404(Project, id=id)
    tasks = project.task_set.all()

    context = {
        'project': project,
        'tasks': tasks
    }
    return render(request, 'tasks/project.html', context)


@login_required
def solutions(request):
    all_solutions = Solution.objects.all()
    context = {
        'solutions': all_solutions
    }
    return render(request, 'tasks/solutions.html', context)


@login_required
def task_send(request):
    form = SolutionForm()
    context = {'form': form}
    return render(request, 'tasks/task.html', context)
