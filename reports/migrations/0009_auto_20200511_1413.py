# Generated by Django 2.2.1 on 2020-05-11 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0008_auto_20200511_1359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='nombre',
            field=models.CharField(default='2020-05-11 14:13:45.760970', max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='site',
            name='nombre',
            field=models.CharField(default='2020-05-11 14:13:45.761974', max_length=255, unique=True),
        ),
    ]
