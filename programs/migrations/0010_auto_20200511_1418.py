# Generated by Django 2.2.1 on 2020-05-11 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('programs', '0009_auto_20200511_1413'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='nombre',
            field=models.CharField(default='2020-05-11 14:18:13.429559', max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='nombre_dato',
            field=models.CharField(default='2020-05-11 14:18:13.429559', max_length=255),
        ),
        migrations.AlterField(
            model_name='datacollection',
            name='nombre',
            field=models.CharField(default='2020-05-11 14:18:13.430556', max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='datacollection',
            name='titulo_datos',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='site',
            name='nombre',
            field=models.CharField(default='2020-05-11 14:18:13.435558', max_length=255, unique=True),
        ),
    ]
