# Generated by Django 2.2.1 on 2020-05-22 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('programs', '0016_auto_20200522_1440'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='nombre',
            field=models.CharField(default='2020-05-22 14:45:33.504199', max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='nombre_dato',
            field=models.CharField(default='2020-05-22 14:45:33.504199', max_length=255),
        ),
        migrations.AlterField(
            model_name='datacollection',
            name='nombre',
            field=models.CharField(default='2020-05-22 14:45:33.504199', max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='site',
            name='nombre',
            field=models.CharField(default='2020-05-22 14:45:33.507196', max_length=255, unique=True),
        ),
    ]