from django.contrib import admin
from .models import *


class CityAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('name',)
    search_fields = ('name',)
    prepopulated_fields = {
        'slug': ('name',)
    }


class LanguageAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ('name',)
    }


class VacancyAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'language', 'company', 'city')
    list_display_links = ('title',)
    search_fields = ('title', 'company')


admin.site.register(City, CityAdmin)
admin.site.register(Language, LanguageAdmin)
admin.site.register(Vacancy, VacancyAdmin)
