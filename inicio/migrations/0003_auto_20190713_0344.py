# Generated by Django 2.1 on 2019-07-13 01:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0002_auto_20190711_0415'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fotos',
            name='fotografia',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
