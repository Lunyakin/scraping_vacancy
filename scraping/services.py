from django.core.paginator import Paginator

from scraping.models import *


def get_data(request) -> dict:
    data = {}

    city = request.GET.get('city')
    language = request.GET.get('language')

    if city or language:
        my_filter = {}
        if city:
            my_filter.update({'city__slug': city})
        if language:
            my_filter.update({'language__slug': language})
        qs = Vacancy.objects.filter(**my_filter)

        paginator = Paginator(qs, 10)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        data['city'] = city
        data['language'] = language
        data['object_list'] = page_obj

    return data
