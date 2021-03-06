# Generated by Django 2.2.7 on 2020-09-08 21:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('producao', '0121_auto_20200902_1049'),
        ('planeamento', '0017_auto_20200908_1635'),
    ]

    operations = [
        migrations.CreateModel(
            name='BobinesARetrabalhar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('retrabalhar', models.BooleanField(default=True, verbose_name='Retrabalhar')),
                ('bobine', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='producao.Bobine', verbose_name='Bobine')),
                ('ordem', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='planeamento.OrdemProducao', verbose_name='Ordem de Produção')),
                ('palete', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='producao.Palete', verbose_name='Palete')),
            ],
        ),
    ]
