# Generated by Django 2.2.1 on 2020-05-20 20:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0012_auto_20200520_1508'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2020, 5, 20, 15, 11, 21, 80212)),
        ),
        migrations.AlterField(
            model_name='event',
            name='nombre',
            field=models.CharField(default='2020-05-20 15:11:21.080212', max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='notice',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2020, 5, 20, 15, 11, 21, 81213)),
        ),
        migrations.AlterField(
            model_name='notice',
            name='nombre',
            field=models.CharField(default='2020-05-20 15:11:21.081213', max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='site',
            name='nombre',
            field=models.CharField(default='2020-05-20 15:11:21.082212', max_length=255, unique=True),
        ),
    ]