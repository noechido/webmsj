# Generated by Django 2.2.1 on 2020-05-20 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0011_auto_20200511_1419'),
    ]

    operations = [
        migrations.AlterField(
            model_name='images',
            name='nombre',
            field=models.CharField(default='2020-05-20 15:08:28.304793', max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='site',
            name='nombre',
            field=models.CharField(default='2020-05-20 15:08:28.304793', max_length=255, unique=True),
        ),
    ]
