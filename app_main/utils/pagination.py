from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def pagination(request, queryset):
    page = 1
    if request.GET.get('page'):
        page = request.GET.get('page')

    paginator = Paginator(object_list=queryset, per_page=1)

    try:
        queryset = paginator.page(page)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)
    except PageNotAnInteger:
        queryset = paginator.page(1)

    left_index = int(page) - 2
    if left_index < 1:
        left_index = 1

    right_index = int(page) + 2
    if right_index > paginator.num_pages:
        right_index = paginator.num_pages

    custom_range = range(left_index, right_index + 1)

    return queryset, custom_range
