# Generated by Django 3.0.6 on 2020-06-09 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recommend', '0006_remove_movie_watch'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='watch',
            field=models.BooleanField(default=False),
        ),
    ]
