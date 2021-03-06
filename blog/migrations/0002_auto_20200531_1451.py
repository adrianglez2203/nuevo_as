# Generated by Django 3.0.6 on 2020-05-31 18:51

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):
    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 31, 18, 51, 46, 160064, tzinfo=utc),
                                       verbose_name='Fecha de Publicacion'),
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.ImageField(upload_to='')),
                ('position', models.PositiveSmallIntegerField(default=0)),
                ('post',
                 models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='blog.Post')),
            ],
            options={
                'ordering': ['position'],
            },
        ),
    ]
