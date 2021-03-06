# Generated by Django 2.2.7 on 2020-09-18 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('producao', '0122_bobine_para_retrabalho'),
    ]

    operations = [
        migrations.AlterField(
            model_name='palete',
            name='peso_bruto',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Peso bruto'),
        ),
        migrations.AlterField(
            model_name='palete',
            name='peso_liquido',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Peso liqudo'),
        ),
    ]
