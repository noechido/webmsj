# Generated by Django 2.2.1 on 2020-05-11 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('howtohelp', '0010_auto_20200511_1413'),
    ]

    operations = [
        migrations.AlterField(
            model_name='site',
            name='nombre',
            field=models.CharField(default='2020-05-11 14:18:13.428559', max_length=255, unique=True),
        ),
    ]
