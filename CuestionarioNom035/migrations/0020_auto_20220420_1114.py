# Generated by Django 3.2.6 on 2022-04-20 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CuestionarioNom035', '0019_auto_20220420_1112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cuestpregunta',
            name='cuestionario',
            field=models.ManyToManyField(to='CuestionarioNom035.Cuestionario'),
        ),
        migrations.AlterField(
            model_name='cuestpregunta',
            name='reactivo',
            field=models.ManyToManyField(to='CuestionarioNom035.Reactivo'),
        ),
    ]
