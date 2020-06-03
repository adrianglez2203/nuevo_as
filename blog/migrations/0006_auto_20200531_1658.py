# Generated by Django 3.0.6 on 2020-05-31 20:58

import ckeditor.fields
import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):
    dependencies = [
        ('blog', '0005_auto_20200531_1610'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=ckeditor.fields.RichTextField(verbose_name='Contenido'),
        ),
        migrations.AlterField(
            model_name='post',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 31, 20, 58, 12, 392831, tzinfo=utc),
                                       verbose_name='Fecha de Publicacion'),
        ),
    ]
