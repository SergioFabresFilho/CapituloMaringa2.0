# Generated by Django 2.1.7 on 2019-02-16 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20190216_1035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagempost',
            name='imagem',
            field=models.ImageField(blank=True, upload_to='imagens/'),
        ),
    ]