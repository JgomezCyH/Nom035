# Generated by Django 3.2.6 on 2022-04-20 16:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CuestionarioNom035', '0025_auto_20220420_1134'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='respcuestpregunta',
            name='cuestionario',
        ),
    ]
