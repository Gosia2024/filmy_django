# Generated by Django 5.1.1 on 2024-09-12 12:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('filmyweb', '0003_film_imdb_rating_film_opis_film_plakat_film_premiera'),
    ]

    operations = [
        migrations.RenameField(
            model_name='film',
            old_name='plakat',
            new_name='plakaty',
        ),
    ]
