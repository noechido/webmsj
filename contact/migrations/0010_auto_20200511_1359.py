# Generated by Django 2.2.1 on 2020-05-11 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0009_auto_20200429_1438'),
    ]

    operations = [
        migrations.AlterField(
            model_name='site',
            name='nombre',
            field=models.CharField(default='2020-05-11 13:59:49.891792', max_length=255, unique=True),
        ),
    ]
