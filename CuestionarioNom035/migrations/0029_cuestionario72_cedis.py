# Generated by Django 3.2.6 on 2022-06-10 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CuestionarioNom035', '0028_auto_20220420_1719'),
    ]

    operations = [
        migrations.AddField(
            model_name='cuestionario72',
            name='Cedis',
            field=models.CharField(default='PIQ', max_length=50),
            preserve_default=False,
        ),
    ]
