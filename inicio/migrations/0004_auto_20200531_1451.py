# Generated by Django 3.0.6 on 2020-05-31 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inicio', '0003_auto_20190713_0344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testimonio',
            name='testimonio',
            field=models.TextField(max_length=500),
        ),
    ]