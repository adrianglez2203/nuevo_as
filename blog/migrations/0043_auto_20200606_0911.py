# Generated by Django 3.0.6 on 2020-06-06 13:11

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0042_auto_20200606_0910'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 6, 13, 11, 41, 397019, tzinfo=utc), verbose_name='Fecha de Publicacion'),
        ),
    ]
