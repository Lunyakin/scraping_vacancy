# Generated by Django 4.1.4 on 2022-12-11 23:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("scraping", "0002_language_alter_city_options_alter_city_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="city",
            name="slug",
            field=models.SlugField(blank=True),
        ),
        migrations.CreateModel(
            name="Vacancy",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("url", models.URLField(unique=True)),
                (
                    "title",
                    models.CharField(max_length=250, verbose_name="Заголовок вакансии"),
                ),
                ("company", models.CharField(max_length=250, verbose_name="Компания")),
                ("description", models.TextField(verbose_name="Описание вакансии")),
                ("timestamp", models.DateField(auto_now_add=True)),
                (
                    "city",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="scraping.city",
                        verbose_name="Город",
                    ),
                ),
                (
                    "language",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="scraping.language",
                        verbose_name="Язык программирования",
                    ),
                ),
            ],
            options={
                "verbose_name": "Вакансия",
                "verbose_name_plural": "Вакансии",
            },
        ),
    ]