from django import forms

from scraping.models import City, Language


class FindForm(forms.Form):
    city = forms.ModelChoiceField(
        queryset = City.objects.all(),
        to_field_name = 'slug',
        required = False,
        empty_label = 'Выбери город',
        widget = forms.Select(attrs = {
            'class': "form-control"
        })
    )
    language = forms.ModelChoiceField(
        queryset = Language.objects.all(),
        to_field_name = 'slug',
        required = False,
        empty_label = 'Выбери специальность',
        widget = forms.Select(attrs = {
            'class': "form-control"
        })
    )
