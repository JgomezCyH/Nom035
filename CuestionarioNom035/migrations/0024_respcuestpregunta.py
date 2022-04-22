# Generated by Django 3.2.6 on 2022-04-20 16:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CuestionarioNom035', '0023_remove_cuestpregunta_valor'),
    ]

    operations = [
        migrations.CreateModel(
            name='RespCuestPregunta',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('edad', models.IntegerField()),
                ('puesto', models.CharField(max_length=100)),
                ('estadoCivil', models.IntegerField(choices=[[0, 'Soltero'], [1, 'Casado'], [2, 'Divorciado'], [3, 'Separado'], [4, 'Viudo'], [5, 'Union Libre']])),
                ('niveldeestudio', models.IntegerField(choices=[[0, 'Primaria'], [1, 'Secundaria'], [2, 'Bachillerato'], [3, 'Licenciatura'], [4, 'PostGrado']])),
                ('valor', models.IntegerField()),
                ('cuestionario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CuestionarioNom035.cuestpregunta')),
            ],
        ),
    ]