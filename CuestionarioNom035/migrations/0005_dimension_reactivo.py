# Generated by Django 3.2.6 on 2022-04-19 22:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CuestionarioNom035', '0004_alter_dominio_dominio'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dimension',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('dimension', models.CharField(max_length=100)),
                ('dominio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CuestionarioNom035.dominio')),
            ],
        ),
        migrations.CreateModel(
            name='Reactivo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('numero', models.IntegerField()),
                ('pregunta', models.CharField(max_length=100)),
                ('valor', models.IntegerField()),
                ('dimension', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CuestionarioNom035.dimension')),
            ],
        ),
    ]
