# Generated by Django 2.2.7 on 2020-02-28 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('producao', '0080_auto_20200211_1603'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bobine',
            name='fc_diam_fim',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True, verbose_name='Falha de corte fim'),
        ),
        migrations.AlterField(
            model_name='bobine',
            name='fc_diam_ini',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True, verbose_name='Falha de corte inicio'),
        ),
        migrations.AlterField(
            model_name='bobine',
            name='ff_m_fim',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True, verbose_name='Falha de fimle fim'),
        ),
        migrations.AlterField(
            model_name='bobine',
            name='ff_m_ini',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=10, null=True, verbose_name='Falha de filme inicio'),
        ),
    ]
