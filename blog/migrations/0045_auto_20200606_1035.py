# Generated by Django 3.0.6 on 2020-06-06 14:35

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0044_auto_20200606_0912'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 6, 14, 35, 45, 400822, tzinfo=utc), verbose_name='Fecha de Publicacion'),
        ),
    ]
