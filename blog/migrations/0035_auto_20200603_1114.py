# Generated by Django 3.0.6 on 2020-06-03 15:14

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0034_auto_20200603_1112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 3, 15, 14, 3, 700736, tzinfo=utc), verbose_name='Fecha de Publicacion'),
        ),
    ]
