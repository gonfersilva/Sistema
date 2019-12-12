# Generated by Django 2.2.7 on 2019-12-09 15:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('producao', '0061_nonwoven_vazio'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fornecedor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('designacao', models.CharField(max_length=200, unique=True, verbose_name='Designação')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Username')),
            ],
            options={
                'verbose_name_plural': 'Fornecedores',
                'ordering': ['-timestamp'],
            },
        ),
        migrations.AlterField(
            model_name='nonwoven',
            name='designacao_fornecedor',
            field=models.CharField(max_length=200, unique=True, verbose_name='Designação do Fornecedor'),
        ),
        migrations.AlterField(
            model_name='nonwoven',
            name='fornecedor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='producao.Fornecedor', verbose_name='Fornecedor'),
        ),
    ]
