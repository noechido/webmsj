# Generated by Django 2.2.1 on 2020-05-22 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0017_auto_20200522_1435'),
    ]

    operations = [
        migrations.AlterField(
            model_name='site',
            name='nombre',
            field=models.CharField(default='2020-05-22 14:40:20.082342', max_length=255, unique=True),
        ),
    ]
