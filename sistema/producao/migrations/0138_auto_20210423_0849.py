# Generated by Django 2.2.7 on 2021-04-23 07:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('producao', '0137_auto_20210421_1659'),
    ]

    operations = [
        migrations.AddField(
            model_name='embalamento',
            name='qtd_cartao',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=2, null=True),
        ),
        migrations.AddField(
            model_name='embalamento',
            name='qtd_mdf',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=2, null=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='nome',
            field=models.CharField(blank=True, max_length=255, null=True, unique=True, verbose_name='Nome'),
        ),
        migrations.AlterField(
            model_name='embalamento',
            name='cinta',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='producao.Cinta', verbose_name='Cinta'),
        ),
        migrations.AlterField(
            model_name='embalamento',
            name='mdf',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='producao.Mdf', verbose_name='MDF'),
        ),
        migrations.CreateModel(
            name='Cartao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('cod', models.CharField(max_length=200, verbose_name='Cód. Cartão')),
                ('des', models.CharField(max_length=200, verbose_name='Descrição Cartão')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Username')),
            ],
        ),
        migrations.AddField(
            model_name='embalamento',
            name='cartao',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='producao.Cartao', verbose_name='Cartao'),
        ),
    ]
