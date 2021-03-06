# Generated by Django 2.2.7 on 2020-01-21 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('producao', '0068_auto_20200109_1459'),
    ]

    operations = [
        migrations.AddField(
            model_name='etiquetapalete',
            name='artigo',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Artigo'),
        ),
        migrations.AddField(
            model_name='etiquetapalete',
            name='cod_cliente',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Código do Cliente'),
        ),
        migrations.AddField(
            model_name='etiquetaretrabalho',
            name='artigo',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Artigo'),
        ),
        migrations.AddField(
            model_name='etiquetaretrabalho',
            name='cod_cliente',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Código do Cliente'),
        ),
        migrations.AlterField(
            model_name='artigo',
            name='produto',
            field=models.CharField(choices=[('NONWOVEN ELASTIC BANDS ELA-ACE 100 HE', 'NONWOVEN ELASTIC BANDS ELA-ACE 100 HE'), ('NONWOVEN ELASTIC BANDS ELA-ACE 90 HE', 'NONWOVEN ELASTIC BANDS ELA-ACE 90 HE'), ('NONWOVEN ELASTIC BANDS ELA-ACE 100 HT', 'NONWOVEN ELASTIC BANDS ELA-ACE 100 HT'), ('NONWOVEN ELASTIC BANDS ELA-ACE 95 HE', 'NONWOVEN ELASTIC BANDS ELA-ACE 95 HE'), ('NONWOVEN ELASTIC BANDS ELA-SPUN 90 HE HL', 'NONWOVEN ELASTIC BANDS ELA-SPUN 90 HE HL'), ('NONWOVEN ELASTIC BANDS ELA-SPUN 95 HE HL', 'NONWOVEN ELASTIC BANDS ELA-SPUN 95 HE HL'), ('NONWOVEN ELASTIC BANDS ELA-SPUN 90 HT HL', 'NONWOVEN ELASTIC BANDS ELA-SPUN 90 HT HL'), ('NONWOVEN ELASTIC BANDS ELA-SPUN 95 HE HL', 'NONWOVEN ELASTIC BANDS ELA-SPUN 95 HE HL'), ('NONWOVEN ELASTIC BANDS ELA-SPUN 100 HE HL', 'NONWOVEN ELASTIC BANDS ELA-SPUN 100 HE HL'), ('SIDE PANEL ELA-ACE 100 HE', 'SIDE PANEL ELA-ACE 100 HE'), ('NONWOVEN ELASTIC BANDS ELA-SPUN 100 HE BICO', 'NONWOVEN ELASTIC BANDS ELA-SPUN 100 HE BICO'), ('NONWOVEN ELASTIC BANDS ELA-ACE 105 HE', 'NONWOVEN ELASTIC BANDS ELA-ACE 105 HE'), ('NONWOVEN ELASTIC BANDS ELA-ACE 100 HE(D)', 'NONWOVEN ELASTIC BANDS ELA-ACE 100 HE(D)'), ('FRONTAL TAPE 48', 'FRONTAL TAPE 48'), ('CAR PROTECTION SHEET 57', 'CAR PROTECTION SHEET 57'), ('ELASTIC FILM', 'ELASTIC FILM')], default='', max_length=100, verbose_name='Produto'),
        ),
        migrations.AlterField(
            model_name='largura',
            name='designacao_prod',
            field=models.CharField(choices=[('NONWOVEN ELASTIC BANDS ELA-ACE 100 HE', 'NONWOVEN ELASTIC BANDS ELA-ACE 100 HE'), ('NONWOVEN ELASTIC BANDS ELA-ACE 90 HE', 'NONWOVEN ELASTIC BANDS ELA-ACE 90 HE'), ('NONWOVEN ELASTIC BANDS ELA-ACE 100 HT', 'NONWOVEN ELASTIC BANDS ELA-ACE 100 HT'), ('NONWOVEN ELASTIC BANDS ELA-ACE 95 HE', 'NONWOVEN ELASTIC BANDS ELA-ACE 95 HE'), ('NONWOVEN ELASTIC BANDS ELA-SPUN 90 HE HL', 'NONWOVEN ELASTIC BANDS ELA-SPUN 90 HE HL'), ('NONWOVEN ELASTIC BANDS ELA-SPUN 95 HE HL', 'NONWOVEN ELASTIC BANDS ELA-SPUN 95 HE HL'), ('NONWOVEN ELASTIC BANDS ELA-SPUN 90 HT HL', 'NONWOVEN ELASTIC BANDS ELA-SPUN 90 HT HL'), ('NONWOVEN ELASTIC BANDS ELA-SPUN 95 HE HL', 'NONWOVEN ELASTIC BANDS ELA-SPUN 95 HE HL'), ('NONWOVEN ELASTIC BANDS ELA-SPUN 100 HE HL', 'NONWOVEN ELASTIC BANDS ELA-SPUN 100 HE HL'), ('SIDE PANEL ELA-ACE 100 HE', 'SIDE PANEL ELA-ACE 100 HE'), ('NONWOVEN ELASTIC BANDS ELA-SPUN 100 HE BICO', 'NONWOVEN ELASTIC BANDS ELA-SPUN 100 HE BICO'), ('NONWOVEN ELASTIC BANDS ELA-ACE 105 HE', 'NONWOVEN ELASTIC BANDS ELA-ACE 105 HE'), ('NONWOVEN ELASTIC BANDS ELA-ACE 100 HE(D)', 'NONWOVEN ELASTIC BANDS ELA-ACE 100 HE(D)'), ('FRONTAL TAPE 48', 'FRONTAL TAPE 48'), ('CAR PROTECTION SHEET 57', 'CAR PROTECTION SHEET 57'), ('ELASTIC FILM', 'ELASTIC FILM')], default='', max_length=100, verbose_name='Produto'),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='produto',
            field=models.CharField(choices=[('NONWOVEN ELASTIC BANDS ELA-ACE 100 HE', 'NONWOVEN ELASTIC BANDS ELA-ACE 100 HE'), ('NONWOVEN ELASTIC BANDS ELA-ACE 90 HE', 'NONWOVEN ELASTIC BANDS ELA-ACE 90 HE'), ('NONWOVEN ELASTIC BANDS ELA-ACE 100 HT', 'NONWOVEN ELASTIC BANDS ELA-ACE 100 HT'), ('NONWOVEN ELASTIC BANDS ELA-ACE 95 HE', 'NONWOVEN ELASTIC BANDS ELA-ACE 95 HE'), ('NONWOVEN ELASTIC BANDS ELA-SPUN 90 HE HL', 'NONWOVEN ELASTIC BANDS ELA-SPUN 90 HE HL'), ('NONWOVEN ELASTIC BANDS ELA-SPUN 95 HE HL', 'NONWOVEN ELASTIC BANDS ELA-SPUN 95 HE HL'), ('NONWOVEN ELASTIC BANDS ELA-SPUN 90 HT HL', 'NONWOVEN ELASTIC BANDS ELA-SPUN 90 HT HL'), ('NONWOVEN ELASTIC BANDS ELA-SPUN 95 HE HL', 'NONWOVEN ELASTIC BANDS ELA-SPUN 95 HE HL'), ('NONWOVEN ELASTIC BANDS ELA-SPUN 100 HE HL', 'NONWOVEN ELASTIC BANDS ELA-SPUN 100 HE HL'), ('SIDE PANEL ELA-ACE 100 HE', 'SIDE PANEL ELA-ACE 100 HE'), ('NONWOVEN ELASTIC BANDS ELA-SPUN 100 HE BICO', 'NONWOVEN ELASTIC BANDS ELA-SPUN 100 HE BICO'), ('NONWOVEN ELASTIC BANDS ELA-ACE 105 HE', 'NONWOVEN ELASTIC BANDS ELA-ACE 105 HE'), ('NONWOVEN ELASTIC BANDS ELA-ACE 100 HE(D)', 'NONWOVEN ELASTIC BANDS ELA-ACE 100 HE(D)'), ('FRONTAL TAPE 48', 'FRONTAL TAPE 48'), ('CAR PROTECTION SHEET 57', 'CAR PROTECTION SHEET 57'), ('ELASTIC FILM', 'ELASTIC FILM')], default='', max_length=100, verbose_name='Produto'),
        ),
    ]
