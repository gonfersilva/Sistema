# Generated by Django 2.2.7 on 2019-12-13 15:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('producao', '0065_auto_20191212_1228'),
    ]

    operations = [
        migrations.AddField(
            model_name='inventariopaletescliente',
            name='area',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=15, null=True, verbose_name='Área'),
        ),
        migrations.AddField(
            model_name='inventariopaletescliente',
            name='artigo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='producao.Artigo', verbose_name='Artigo'),
        ),
        migrations.AddField(
            model_name='inventariopaletescliente',
            name='cliente',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='inventariopaletescliente',
            name='comp_total',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True, verbose_name='Comprimento Total'),
        ),
        migrations.AddField(
            model_name='inventariopaletescliente',
            name='core_bobines',
            field=models.CharField(blank=True, max_length=1, null=True, verbose_name='Core das bobines'),
        ),
        migrations.AddField(
            model_name='inventariopaletescliente',
            name='diam_max',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Diâmetro máximo'),
        ),
        migrations.AddField(
            model_name='inventariopaletescliente',
            name='diam_min',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Diâmetro minimo'),
        ),
        migrations.AddField(
            model_name='inventariopaletescliente',
            name='largura_bobine',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Largura'),
        ),
    ]
