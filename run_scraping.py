import asyncio
import json
import os, sys

from django.contrib.auth import get_user_model

proj = os.path.dirname(os.path.abspath('manage.py'))
sys.path.append(proj)
os.environ['DJANGO_SETTINGS_MODULE'] = 'app.settings'

import django

django.setup()

from scraping.scraping_scripts import *
from scraping.models import City, Vacancy, Language, Error, Url
from django.db import DatabaseError

User = get_user_model()

parsers = (
    (work_ua, 'work'),
    (dou_ua, 'dou'),
)
jobs, errors = [], []


def get_settings():
    qs = User.objects.filter(receive_email = True).values()
    list_settings = set((q['city_id'], q['language_id']) for q in qs)
    return list_settings


def get_urls(settings):
    qs = Url.objects.all().values()
    url_dict = {(q['city_id'], q['language_id']): q['url_data'] for q in qs}
    urls = []
    for pair in settings:
        temp = {}
        temp['city'] = pair[0]
        temp['language'] = pair[1]
        temp['url_data'] = url_dict[pair]
        urls.append(temp)
    return urls


async def main(value):
    func, url_data, city, language = value
    job, error = await loop.run_in_executor(None, func, url_data, city, language)
    jobs.extend(job)
    errors.extend(error)


setting = get_settings()
url_list = get_urls(setting)

# import time
# start = time.time()
loop = asyncio.new_event_loop()
list_tasks = [
    (func, data['url_data'][key], data['city'], data['language'])
    for data in url_list
    for func, key in parsers
]
tasks = asyncio.wait([loop.create_task(main(f)) for f in list_tasks])

# for data in url_list:
#
#     for func, key in parsers:
#         url = data['url_data'][key]
#         j, e = func(url, city = data['city'], language = data['language'])
#         jobs += j
#         errors += e

loop.run_until_complete(tasks)
loop.close()
# end = time.time() - start
# print(end)
for job in jobs:
    v = Vacancy(**job)
    try:
        v.save()
    except DatabaseError:
        pass

if errors:
    er = Error(data = errors).save()
