# Generated by Django 2.2.1 on 2020-05-20 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_auto_20200520_1508'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutus',
            name='nombre',
            field=models.CharField(default='2020-05-20 15:11:21.085216', max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='images',
            name='nombre',
            field=models.CharField(default='2020-05-20 15:11:21.084216', max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='mision',
            name='nombre',
            field=models.CharField(default='2020-05-20 15:11:21.087212', max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='values',
            name='nombre',
            field=models.CharField(default='2020-05-20 15:11:21.088212', max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='vision',
            name='nombre',
            field=models.CharField(default='2020-05-20 15:11:21.087212', max_length=255, unique=True),
        ),
    ]