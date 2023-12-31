# Generated by Django 2.2.1 on 2020-05-20 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0011_auto_20200511_1419'),
    ]

    operations = [
        migrations.CreateModel(
            name='Certification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(default='2020-05-20 15:08:28.320795', max_length=255, unique=True)),
                ('nombre_certificacion', models.CharField(default='2020-05-20 15:08:28.320795', max_length=255, unique=True)),
            ],
            options={
                'verbose_name': 'Certificación',
                'verbose_name_plural': 'Certificaciones',
            },
        ),
        migrations.CreateModel(
            name='Other',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(default='2020-05-20 15:08:28.320795', max_length=255, unique=True)),
                ('nombre_otro', models.CharField(default='2020-05-20 15:08:28.320795', max_length=255, unique=True)),
            ],
            options={
                'verbose_name': 'Otro',
                'verbose_name_plural': 'Otros',
            },
        ),
        migrations.AlterField(
            model_name='report',
            name='nombre',
            field=models.CharField(default='2020-05-20 15:08:28.319794', max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='report',
            name='reporte_url',
            field=models.CharField(default=None, max_length=1000, unique=True),
        ),
        migrations.AlterField(
            model_name='site',
            name='nombre',
            field=models.CharField(default='2020-05-20 15:08:28.321796', max_length=255, unique=True),
        ),
    ]
