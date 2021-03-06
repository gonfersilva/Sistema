# Generated by Django 2.2.7 on 2020-06-25 09:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('producao', '0105_turno_dep'),
    ]

    operations = [
        migrations.AlterField(
            model_name='encomenda',
            name='order_num',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Order Number'),
        ),
        migrations.AlterField(
            model_name='movimentosbobines',
            name='palete',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='producao.Palete', verbose_name='Palete'),
        ),
    ]
