from django.db.models import Q
from app_main import models


def filter_profiles(request):
    if request.GET.get('profile'):
        search_param = request.GET.get('profile')
    else:
        search_param = None

    if search_param:
        profiles = models.Profile.objects.filter(
            Q(first_name__icontains=search_param) |
            Q(last_name__icontains=search_param) |
            Q(short_intro__icontains=search_param) |
            Q(skill__title__icontains=search_param)
        ).distinct()

    else:
        profiles = models.Profile.objects.all()

    profiles = profiles.exclude(
        Q(bio="") |
        Q(bio=None) |
        Q(short_intro="") |
        Q(short_intro=None) |
        Q(location="") |
        Q(location=None)
    )

    return profiles

