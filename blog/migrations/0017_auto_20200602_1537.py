# Generated by Django 3.0.6 on 2020-06-02 19:37

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_auto_20200602_1536'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 2, 19, 37, 50, 173087, tzinfo=utc), verbose_name='Fecha de Publicacion'),
        ),
    ]
