# Generated by Django 2.1.3 on 2019-03-21 14:52

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('producao', '0017_auto_20190321_0958'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carga',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('data', models.DateField(default=datetime.date.today, verbose_name='Data')),
                ('carga', models.CharField(max_length=200, unique=True, verbose_name='Carga')),
                ('num_carga', models.IntegerField(default=0, verbose_name='Carga nº')),
                ('num_paletes', models.IntegerField(default=0, verbose_name='Número de paletes total')),
                ('num_paletes_actual', models.IntegerField(default=0, verbose_name='Número de paletes actual')),
                ('estado', models.CharField(choices=[('I', 'I'), ('C', 'C')], default='I', max_length=1, verbose_name='Estado')),
                ('sqm', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Metros quadrados')),
                ('tipo', models.CharField(choices=[('CONTENTOR', 'CONTENTOR'), ('CAMIÃO', 'CAMIÃO')], default='CONTENTOR', max_length=9, verbose_name='Tipo de Carga')),
            ],
        ),
        migrations.CreateModel(
            name='Encomenda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('data', models.DateField(default=datetime.date.today, verbose_name='Data')),
                ('eef', models.CharField(max_length=200, unique=True, verbose_name='Encomenda')),
                ('prf', models.CharField(max_length=200, unique=True, verbose_name='Proforma')),
                ('sqm', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Metros quadrados')),
                ('estado', models.CharField(choices=[('A', 'A'), ('F', 'F')], default='A', max_length=1, verbose_name='Estado')),
                ('num_cargas', models.IntegerField(default=0)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='producao.Cliente', verbose_name='Cliente')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Username')),
            ],
        ),
        migrations.AddField(
            model_name='palete',
            name='stock',
            field=models.BooleanField(default=False, verbose_name='Stock'),
        ),
        migrations.AddField(
            model_name='carga',
            name='enc',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='producao.Encomenda', verbose_name='Encomenda'),
        ),
        migrations.AddField(
            model_name='carga',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Username'),
        ),
        migrations.AddField(
            model_name='palete',
            name='carga',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='producao.Carga', verbose_name='Carga'),
        ),
    ]