# Generated by Django 2.1.3 on 2019-04-05 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('producao', '0025_auto_20190405_1149'),
    ]

    operations = [
        migrations.AddField(
            model_name='palete',
            name='num_palete_carga',
            field=models.IntegerField(blank=True, null=True, verbose_name='Nº Palete Carga'),
        ),
    ]
