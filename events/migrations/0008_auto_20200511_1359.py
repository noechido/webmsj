# Generated by Django 2.2.1 on 2020-05-11 18:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0007_auto_20200429_1438'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2020, 5, 11, 13, 59, 49, 906789)),
        ),
        migrations.AlterField(
            model_name='event',
            name='nombre',
            field=models.CharField(default='2020-05-11 13:59:49.906789', max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='notice',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2020, 5, 11, 13, 59, 49, 907789)),
        ),
        migrations.AlterField(
            model_name='notice',
            name='nombre',
            field=models.CharField(default='2020-05-11 13:59:49.907789', max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='site',
            name='nombre',
            field=models.CharField(default='2020-05-11 13:59:49.908792', max_length=255, unique=True),
        ),
    ]