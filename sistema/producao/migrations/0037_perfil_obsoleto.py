# Generated by Django 2.2 on 2019-05-07 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('producao', '0036_cliente_diam_ref'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfil',
            name='obsoleto',
            field=models.BooleanField(default=False, verbose_name='Obsoleto'),
        ),
    ]
