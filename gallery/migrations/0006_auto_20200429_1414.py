# Generated by Django 2.2.1 on 2020-04-29 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0005_auto_20200429_1407'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='nombre',
            field=models.CharField(default='2020-04-29 14:14:48.071747', max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='site',
            name='nombre',
            field=models.CharField(default='2020-04-29 14:14:48.073750', max_length=255, unique=True),
        ),
    ]
