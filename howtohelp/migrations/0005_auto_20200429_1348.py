# Generated by Django 2.2.1 on 2020-04-29 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('howtohelp', '0004_auto_20200420_2223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='site',
            name='nombre',
            field=models.CharField(default='2020-04-29 13:48:01.672245', max_length=255, unique=True),
        ),
    ]
