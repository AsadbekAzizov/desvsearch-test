from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from . import models
from . import forms
from .utils.filter_projects import filter_projects
from .utils.pagination import pagination


def projects(request):
    projects = filter_projects(request)
    search_query = request.GET.get('project', "")

    projects, custom_range = pagination(request=request, queryset=projects)

    context = {
        'page_range': custom_range,
        'projects': projects,
        'search_query': search_query,
    }
    return render(request, 'app_main/projects.html', context)


def project_detail(request, pk):
    project = models.Project.objects.get(id=pk)
    comments = project.comment_set.all().order_by('created')  # fresh comments - older comments
    tags = project.tags.all()

    context = {
        'project': project,
        'comments': comments,
        'tags': tags,
    }
    return render(request, 'app_main/project_detail.html', context)


@login_required(login_url='signin')
def create_project(request):

    if request.method == 'POST':
        form = forms.ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = request.user.profile
            project.save()
            # success message
            return redirect('account')
        else:
            # error message
            return redirect('create_project')

    form = forms.ProjectForm()

    context = {
        'form': form,
    }
    return render(request, 'form-template.html', context)


@login_required(login_url='signin')
def edit_project(request, pk):
    project = models.Project.objects.get(id=pk)

    if not project.owner == request.user.profile:
        # error message
        return redirect('account')

    if request.method == 'POST':
        form = forms.ProjectForm(request.POST, request.FILES, instance=project)
        if form.is_valid():
            form.save()
            # success message
            return redirect('account')
        else:
            # error message
            return redirect('edit_project', pk=pk)

    form = forms.ProjectForm(instance=project)
    context = {
        'form': form,
    }
    return render(request, 'form-template.html', context)
