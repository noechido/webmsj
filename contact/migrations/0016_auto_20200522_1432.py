# Generated by Django 2.2.1 on 2020-05-22 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0015_auto_20200520_1511'),
    ]

    operations = [
        migrations.AlterField(
            model_name='site',
            name='nombre',
            field=models.CharField(default='2020-05-22 14:32:58.964212', max_length=255, unique=True),
        ),
    ]
