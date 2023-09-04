# Generated by Django 2.2.1 on 2020-04-21 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(default='2020-04-20 22:21:11.018824', max_length=255, unique=True)),
                ('reporte_url', models.FileField(upload_to='reports/uploads/')),
            ],
            options={
                'verbose_name': 'Reporte',
                'verbose_name_plural': 'Reportes',
            },
        ),
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(default='2020-04-20 22:21:11.018824', max_length=255, unique=True)),
                ('descripcion', models.CharField(default='Reportes de la institución.', max_length=1000, unique=True)),
                ('imagen', models.ImageField(upload_to='reports/images/')),
            ],
            options={
                'verbose_name': 'Sitio',
                'verbose_name_plural': 'Sitio',
            },
        ),
    ]
