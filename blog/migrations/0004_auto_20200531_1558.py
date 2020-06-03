# Generated by Django 3.0.6 on 2020-05-31 19:58

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):
    dependencies = [
        ('blog', '0003_auto_20200531_1556'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(default=None, max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 31, 19, 58, 40, 836791, tzinfo=utc),
                                       verbose_name='Fecha de Publicacion'),
        ),
    ]