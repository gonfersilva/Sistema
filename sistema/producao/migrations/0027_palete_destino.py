# Generated by Django 2.2 on 2019-04-17 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('producao', '0026_palete_num_palete_carga'),
    ]

    operations = [
        migrations.AddField(
            model_name='palete',
            name='destino',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Destino'),
        ),
    ]
