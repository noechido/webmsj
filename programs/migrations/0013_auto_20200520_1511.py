# Generated by Django 2.2.1 on 2020-05-20 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('programs', '0012_auto_20200520_1508'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='nombre',
            field=models.CharField(default='2020-05-20 15:11:21.096214', max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='data',
            name='nombre_dato',
            field=models.CharField(default='2020-05-20 15:11:21.096214', max_length=255),
        ),
        migrations.AlterField(
            model_name='datacollection',
            name='nombre',
            field=models.CharField(default='2020-05-20 15:11:21.097213', max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='site',
            name='nombre',
            field=models.CharField(default='2020-05-20 15:11:21.101212', max_length=255, unique=True),
        ),
    ]
