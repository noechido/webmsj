# Generated by Django 2.2.1 on 2020-04-29 19:38

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('programs', '0006_auto_20200429_1414'),
    ]

    operations = [
        migrations.AlterField(
            model_name='program',
            name='imagen',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='program'),
        ),
        migrations.AlterField(
            model_name='site',
            name='imagen',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='site'),
        ),
        migrations.AlterField(
            model_name='site',
            name='nombre',
            field=models.CharField(default='2020-04-29 14:37:39.940415', max_length=255, unique=True),
        ),
    ]
