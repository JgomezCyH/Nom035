# Generated by Django 3.2.6 on 2022-06-10 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CuestionarioNom035', '0029_cuestionario72_cedis'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cuestionario72',
            name='Cedis',
            field=models.IntegerField(choices=[[0, 'PIQ'], [1, 'AGS'], [2, 'PARK V'], [3, 'SJR']]),
        ),
    ]
