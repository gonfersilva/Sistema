# Generated by Django 2.1.3 on 2018-12-10 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('producao', '0011_auto_20181206_1623'),
    ]

    operations = [
        migrations.AlterField(
            model_name='palete',
            name='diametro',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True, verbose_name='Diâmetro das bobines'),
        ),
    ]
