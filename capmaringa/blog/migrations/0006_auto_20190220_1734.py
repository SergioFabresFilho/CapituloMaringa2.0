# Generated by Django 2.1.7 on 2019-02-20 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20190216_1208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='imagem',
            field=models.ImageField(blank=True, null=True, upload_to='imagens/'),
        ),
    ]
