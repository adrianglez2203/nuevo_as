# Generated by Django 3.0.6 on 2020-06-02 19:19

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20200602_1511'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 2, 19, 19, 28, 497767, tzinfo=utc), verbose_name='Fecha de Publicacion'),
        ),
    ]
