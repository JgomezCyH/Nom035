# Generated by Django 3.2.6 on 2022-04-20 16:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CuestionarioNom035', '0022_auto_20220420_1123'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cuestpregunta',
            name='valor',
        ),
    ]
