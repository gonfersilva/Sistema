# Generated by Django 2.2.7 on 2020-09-18 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planeamento', '0024_auto_20200918_0950'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordemproducao',
            name='hora_prevista_inicio',
            field=models.TimeField(blank=True, null=True, verbose_name='Hora prevista de inicio'),
        ),
        migrations.AddField(
            model_name='ordemproducao',
            name='horas_previstas_producao',
            field=models.IntegerField(blank=True, default=0, null=True, verbose_name='Horas previstas de produção'),
        ),
    ]