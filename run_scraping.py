import json
import os, sys

proj = os.path.dirname(os.path.abspath('manage.py'))
sys.path.append(proj)
os.environ['DJANGO_SETTINGS_MODULE'] = 'app.settings'

import django
django.setup()

from scraping.scraping_scripts import *
from scraping.models import City, Vacancy, Language, Error
from django.db import DatabaseError


parsers = (
    (work_ua, 'https://www.work.ua/jobs-kyiv-python/'),
    (dou_ua, 'https://jobs.dou.ua/vacancies/?city=%D0%9A%D0%B8%D0%B5%D0%B2&category=Python'),
)

city = City.objects.filter(slug = 'kiev').first()
language = Language.objects.filter(slug = 'python').first()

jobs, errors = [], []

for func, url in parsers:
    j, e = func(url)
    jobs += j
    errors += e

with open('jobs.json', 'w', encoding = 'utf-8') as file:
    json.dump(jobs, file, indent = 4, ensure_ascii = False)

for job in jobs:
    v = Vacancy(**job, city=city, language=language)
    try:
        v.save()
    except DatabaseError:
        pass

if errors:
    er = Error(data=errors).save()
