# Generated by Django 2.2.1 on 2020-04-29 19:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('howtohelp', '0006_auto_20200429_1407'),
    ]

    operations = [
        migrations.AlterField(
            model_name='site',
            name='nombre',
            field=models.CharField(default='2020-04-29 14:14:48.092751', max_length=255, unique=True),
        ),
    ]
