# Generated by Django 3.0.6 on 2020-06-03 12:14

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0026_auto_20200603_0741'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 3, 12, 14, 20, 50266, tzinfo=utc), verbose_name='Fecha de Publicacion'),
        ),
    ]
