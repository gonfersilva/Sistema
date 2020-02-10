# Generated by Django 2.2.7 on 2020-01-29 12:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('producao', '0072_rececao'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='rececao',
            options={'ordering': ['-timestamp'], 'verbose_name_plural': 'Receções'},
        ),
        migrations.RemoveField(
            model_name='nonwoven',
            name='designacao',
        ),
        migrations.RemoveField(
            model_name='nonwoven',
            name='designacao_fornecedor',
        ),
        migrations.RemoveField(
            model_name='nonwoven',
            name='fornecedor',
        ),
        migrations.RemoveField(
            model_name='nonwoven',
            name='largura',
        ),
        migrations.AddField(
            model_name='nonwoven',
            name='lote',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Lote'),
        ),
        migrations.AddField(
            model_name='nonwoven',
            name='prod',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Produção'),
        ),
        migrations.AddField(
            model_name='nonwoven',
            name='rececao',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='producao.Rececao', verbose_name='Receção'),
        ),
        migrations.AddField(
            model_name='nonwoven',
            name='sqm',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True, verbose_name='Metros quadrados'),
        ),
        migrations.AddField(
            model_name='nonwoven',
            name='stack_num',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Stack number'),
        ),
        migrations.AddField(
            model_name='rececao',
            name='num',
            field=models.IntegerField(blank=True, null=True, verbose_name='Rececao nº'),
        ),
        migrations.AlterField(
            model_name='rececao',
            name='estado',
            field=models.CharField(choices=[('A', 'Aberta'), ('F', 'Fechada')], default='A', max_length=1, verbose_name='Estado da Receção'),
        ),
        migrations.CreateModel(
            name='ArtigoNW',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('cod', models.CharField(max_length=50, unique=True, verbose_name='Código Artigo Nonwoven')),
                ('designacao', models.CharField(max_length=200, unique=True, verbose_name='Designação')),
                ('gsm', models.IntegerField(verbose_name='Gramagem')),
                ('largura', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Largura')),
                ('fornecedor', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='producao.Fornecedor', verbose_name='Fornecedor')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Username')),
            ],
        ),
        migrations.AddField(
            model_name='nonwoven',
            name='artigo_nw',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='producao.ArtigoNW', verbose_name='Artigo Nonwoven'),
        ),
    ]
