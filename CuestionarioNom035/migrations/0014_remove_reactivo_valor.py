# Generated by Django 3.2.6 on 2022-04-20 02:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CuestionarioNom035', '0013_reactivo_valor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reactivo',
            name='valor',
        ),
    ]
