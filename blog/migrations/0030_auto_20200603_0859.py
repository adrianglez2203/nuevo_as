# Generated by Django 3.0.6 on 2020-06-03 12:59

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0029_auto_20200603_0856'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 3, 12, 59, 21, 207839, tzinfo=utc), verbose_name='Fecha de Publicacion'),
        ),
    ]
