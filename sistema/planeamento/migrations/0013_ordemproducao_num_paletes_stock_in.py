# Generated by Django 2.2.7 on 2020-08-06 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planeamento', '0012_auto_20200805_1401'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordemproducao',
            name='num_paletes_stock_in',
            field=models.IntegerField(default=0, verbose_name='Nº de paletes de stock inseridas'),
        ),
    ]