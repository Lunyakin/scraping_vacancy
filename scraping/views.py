from django.shortcuts import render

from .forms import FindForm
from .models import Vacancy
from .services import get_data


def home_view(request):
    form = FindForm()
    qs = ()
    if request.method == 'POST':
        qs = get_data(request.POST)

    context = {
        'form': form,
        'title': 'Home',
        'object_list': qs
    }
    return render(request, 'scraping/home.html', context)
