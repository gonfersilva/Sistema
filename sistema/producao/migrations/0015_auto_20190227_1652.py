# Generated by Django 2.1.3 on 2019-02-27 16:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('producao', '0014_auto_20190121_1117'),
    ]

    operations = [
        migrations.CreateModel(
            name='Artigo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cod', models.CharField(max_length=50, unique=True, verbose_name='Cód. Artigo')),
                ('des', models.CharField(max_length=200, unique=True, verbose_name='Descrição artigo')),
                ('tipo', models.CharField(max_length=50, verbose_name='Tipo')),
            ],
            options={
                'verbose_name_plural': 'Artigos',
                'ordering': ['cod'],
            },
        ),
        migrations.AlterField(
            model_name='bobinagem',
            name='tiponwinf',
            field=models.CharField(blank=True, choices=[('Suominen 25 gsm', 'Suominen 25 gsm'), ('Sandler SPUNLACE 100%PP', 'Sandler SPUNLACE 100%PP'), ('BCN 70%PP/30%PE', 'BCN 70%PP/30%PE'), ('Sandler', 'Sandler'), ('PEGAS BICO 17gsm', 'PEGAS BICO 17gsm'), ('Suominen', 'Suominen'), ('BCN', 'BCN'), ('ORMA', 'ORMA'), ('PEGAS 22', 'PEGAS 22'), ('SAWASOFT', 'SAWASOFT'), ('SAWABOND', 'SAWABOND'), ('Teksis', 'Teksis'), ('Union', 'Union'), ('Radici', 'Radici'), ('Fitesa', 'Fitesa')], default='', max_length=40, null=True, verbose_name='Tipo Nonwoven Inferior'),
        ),
        migrations.AlterField(
            model_name='bobinagem',
            name='tiponwsup',
            field=models.CharField(blank=True, choices=[('Suominen 25 gsm', 'Suominen 25 gsm'), ('Sandler SPUNLACE 100%PP', 'Sandler SPUNLACE 100%PP'), ('BCN 70%PP/30%PE', 'BCN 70%PP/30%PE'), ('Sandler', 'Sandler'), ('PEGAS BICO 17gsm', 'PEGAS BICO 17gsm'), ('Suominen', 'Suominen'), ('BCN', 'BCN'), ('ORMA', 'ORMA'), ('PEGAS 22', 'PEGAS 22'), ('SAWASOFT', 'SAWASOFT'), ('SAWABOND', 'SAWABOND'), ('Teksis', 'Teksis'), ('Union', 'Union'), ('Radici', 'Radici'), ('Fitesa', 'Fitesa')], default='', max_length=40, null=True, verbose_name='Tipo Nonwoven Superior'),
        ),
        migrations.AddField(
            model_name='largura',
            name='artigo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='producao.Artigo', verbose_name='Artigo'),
        ),
    ]