# Generated by Django 2.2.1 on 2020-05-22 19:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0015_auto_20200522_1435'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2020, 5, 22, 14, 40, 20, 91344)),
        ),
        migrations.AlterField(
            model_name='event',
            name='nombre',
            field=models.CharField(default='2020-05-22 14:40:20.090344', max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='notice',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2020, 5, 22, 14, 40, 20, 92344)),
        ),
        migrations.AlterField(
            model_name='notice',
            name='nombre',
            field=models.CharField(default='2020-05-22 14:40:20.092344', max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='site',
            name='nombre',
            field=models.CharField(default='2020-05-22 14:40:20.092344', max_length=255, unique=True),
        ),
    ]
