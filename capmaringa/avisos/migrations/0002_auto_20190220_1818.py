# Generated by Django 2.1.7 on 2019-02-20 21:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('avisos', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aviso',
            name='data_e_hora',
        ),
        migrations.AddField(
            model_name='aviso',
            name='data',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='aviso',
            name='horario',
            field=models.TimeField(null=True),
        ),
    ]
