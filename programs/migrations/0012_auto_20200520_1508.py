# Generated by Django 2.2.1 on 2020-05-20 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('programs', '0011_auto_20200511_1419'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='nombre',
            field=models.CharField(default='2020-05-20 15:08:28.315794', max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='nombre_dato',
            field=models.CharField(default='2020-05-20 15:08:28.315794', max_length=255),
        ),
        migrations.AlterField(
            model_name='datacollection',
            name='nombre',
            field=models.CharField(default='2020-05-20 15:08:28.315794', max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='site',
            name='nombre',
            field=models.CharField(default='2020-05-20 15:08:28.318794', max_length=255, unique=True),
        ),
    ]
