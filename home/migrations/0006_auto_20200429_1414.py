# Generated by Django 2.2.1 on 2020-04-29 19:14

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_auto_20200429_1407'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutus',
            name='imagenA',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='imageA'),
        ),
        migrations.AlterField(
            model_name='aboutus',
            name='imagenB',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='imageB'),
        ),
        migrations.AlterField(
            model_name='aboutus',
            name='imagenC',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='imageC'),
        ),
        migrations.AlterField(
            model_name='aboutus',
            name='nombre',
            field=models.CharField(default='2020-04-29 14:14:48.085751', max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='directors',
            name='imagen',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='patron'),
        ),
        migrations.AlterField(
            model_name='images',
            name='nombre',
            field=models.CharField(default='2020-04-29 14:14:48.084756', max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='images',
            name='path',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='mision',
            name='nombre',
            field=models.CharField(default='2020-04-29 14:14:48.088750', max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='patrons',
            name='imagen',
            field=cloudinary.models.CloudinaryField(max_length=255, verbose_name='patron'),
        ),
        migrations.AlterField(
            model_name='values',
            name='nombre',
            field=models.CharField(default='2020-04-29 14:14:48.089786', max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='vision',
            name='nombre',
            field=models.CharField(default='2020-04-29 14:14:48.088750', max_length=255, unique=True),
        ),
    ]