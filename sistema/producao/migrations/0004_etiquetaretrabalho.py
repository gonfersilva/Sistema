# Generated by Django 2.0.7 on 2018-11-07 17:36

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('producao', '0003_auto_20181106_1902'),
    ]

    operations = [
        migrations.CreateModel(
            name='EtiquetaRetrabalho',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bobine', models.CharField(max_length=200, verbose_name='Bobine')),
                ('data', models.DateField(default=datetime.date.today, verbose_name='Data')),
                ('produto', models.CharField(max_length=200, verbose_name='Produto')),
                ('largura_bobinagem', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Largura da bobinagem')),
                ('diam', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Diâmetro')),
                ('largura_bobine', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Largura')),
                ('comp_total', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Comprimento total')),
                ('area', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Área')),
                ('bobine_original_1', models.CharField(blank=True, max_length=200, null=True, verbose_name='Bobine1')),
                ('bobine_original_2', models.CharField(blank=True, max_length=200, null=True, verbose_name='Bobine2')),
                ('bobine_original_3', models.CharField(blank=True, max_length=200, null=True, verbose_name='Bobine3')),
                ('emenda1', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Emenda 1')),
                ('metros1', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Metros Consumidos 1')),
                ('emenda2', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Emenda 2')),
                ('metros2', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Metros Consumidos 2')),
                ('emenda3', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Emenda 3')),
                ('metros3', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Metros Consumidos 3')),
                ('bobinagem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='producao.Bobinagem', verbose_name='Bobinagem')),
            ],
        ),
    ]
