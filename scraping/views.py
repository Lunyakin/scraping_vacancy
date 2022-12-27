from django.core.paginator import Paginator
from django.shortcuts import render

from .forms import FindForm
from .models import Vacancy
from .services import get_data


def home_view(request):
    form = FindForm()
    context = {
        'form': form,
        'title': 'Home',
    }
    return render(request, 'scraping/home.html', context)


def list_view(request):
    form = FindForm()
    data = get_data(request)
    context = {
        'form': form,
        'title': 'Vacancy list',
    }
    context.update(data)
    return render(request, 'scraping/list.html', context)
