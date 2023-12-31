# Generated by Django 2.2.1 on 2020-05-22 19:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0013_auto_20200520_1511'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2020, 5, 22, 14, 32, 58, 996209)),
        ),
        migrations.AlterField(
            model_name='event',
            name='nombre',
            field=models.CharField(default='2020-05-22 14:32:58.996209', max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='notice',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2020, 5, 22, 14, 32, 58, 998209)),
        ),
        migrations.AlterField(
            model_name='notice',
            name='nombre',
            field=models.CharField(default='2020-05-22 14:32:58.998209', max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='site',
            name='nombre',
            field=models.CharField(default='2020-05-22 14:32:59.000209', max_length=255, unique=True),
        ),
    ]
