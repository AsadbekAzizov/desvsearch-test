from app_main import models
from django.db.models import Q


def filter_projects(request):
    if request.GET.get('project'):
        search_param = request.GET.get('project')
    else:
        search_param = None

    if search_param:
        tags = models.Tag.objects.filter(
            name__icontains=search_param
        ).distinct()  # [ {id: 1, name: 'Python'} ]

        projects = models.Project.objects.filter(
            Q(title__icontains=search_param) |
            Q(tags__in=tags) |
            Q(owner__first_name__icontains=search_param) |
            Q(owner__last_name__icontains=search_param)
        ).distinct()

    else:
        projects = models.Project.objects.all()

    return projects
