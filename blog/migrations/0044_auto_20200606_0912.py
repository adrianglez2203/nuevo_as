# Generated by Django 3.0.6 on 2020-06-06 13:12

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0043_auto_20200606_0911'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 6, 13, 12, 9, 113298, tzinfo=utc), verbose_name='Fecha de Publicacion'),
        ),
    ]