# Generated by Django 3.2.6 on 2022-04-19 22:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CuestionarioNom035', '0007_rename_dimensiones_dimension'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reactivo',
            name='valor',
        ),
    ]
