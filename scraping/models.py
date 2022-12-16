from django.db import models


class City(models.Model):
    name = models.CharField(
        max_length = 50,
        verbose_name = 'Название населенного пункта',
    )
    slug = models.SlugField(
        max_length = 50,
        blank = True
    )

    class Meta:
        verbose_name = 'Название населенного пункта'
        verbose_name_plural = 'Название населенных пунктов'

    def __str__(self):
        return self.name


class Language(models.Model):
    name = models.CharField(
        max_length = 50,
        verbose_name = 'Язык программирования'
    )
    slug = models.CharField(
        max_length = 50,
        blank = True
    )

    class Meta:
        verbose_name = 'Язык программирования'
        verbose_name_plural = 'Языки программирования'

    def __str__(self):
        return self.name


class Vacancy(models.Model):
    url = models.URLField(
        unique = True
    )
    title = models.CharField(
        max_length = 250,
        verbose_name = 'Заголовок вакансии'
    )
    company = models.CharField(
        max_length = 250,
        verbose_name = 'Компания'
    )
    description = models.TextField(
        verbose_name = 'Описание вакансии'
    )
    city = models.ForeignKey(
        'City',
        on_delete = models.CASCADE,
        verbose_name = 'Город'
    )
    language = models.ForeignKey(
        'Language',
        on_delete = models.CASCADE,
        verbose_name = 'Язык программирования'
    )
    timestamp = models.DateField(
        auto_now_add = True,
    )

    class Meta:
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансии'

    def __str__(self):
        return self.title

    @property
    def short_context(self):
        return self.description[:300] + '...'
