
from scraping.models import *



def get_all_city():
    ...


def get_data(data):
    my_filter = {}
    city = data['city']
    language = data['language']
    if city:
        my_filter.update({'city__slug': city})
    if language:
        my_filter.update({'language__slug': language})
    qs = Vacancy.objects.filter(**my_filter)

    return qs
