# Generated by Django 3.2.6 on 2022-04-20 01:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CuestionarioNom035', '0010_respuesta'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='respuesta',
            name='valor',
        ),
        migrations.AddField(
            model_name='cuestionario',
            name='valor',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
