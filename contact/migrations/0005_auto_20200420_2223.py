# Generated by Django 2.2.1 on 2020-04-21 03:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0004_auto_20200420_2221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='site',
            name='nombre',
            field=models.CharField(default='2020-04-20 22:23:57.592421', max_length=255, unique=True),
        ),
    ]
