# Generated by Django 2.2.7 on 2021-04-16 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('producao', '0135_auto_20210415_2238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='core',
            name='des',
            field=models.CharField(max_length=200, verbose_name='Descrição Core'),
        ),
    ]
