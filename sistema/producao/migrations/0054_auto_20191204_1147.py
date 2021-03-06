# Generated by Django 2.2.7 on 2019-12-04 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('producao', '0053_auto_20191203_0935'),
    ]

    operations = [
        migrations.AlterField(
            model_name='palete',
            name='peso_palete',
            field=models.CharField(blank=True, choices=[('0', '0 Kg'), ('8', '8 Kg'), ('13', '13 Kg')], max_length=5, null=True, verbose_name='Peso palete'),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='token',
            field=models.CharField(blank=True, max_length=255, null=True, unique=True, verbose_name='Token'),
        ),
    ]
