# Generated by Django 3.2.6 on 2021-08-19 09:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filemanager', '0002_auto_20210819_1258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='change_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 8, 19, 12, 59, 19, 428791)),
        ),
        migrations.AlterField(
            model_name='document',
            name='field',
            field=models.CharField(default='Not defined', max_length=20),
        ),
    ]
