# Generated by Django 2.2.7 on 2020-06-16 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('producao', '0100_auto_20200518_1233'),
    ]

    operations = [
        migrations.AddField(
            model_name='bobine',
            name='comp',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True, verbose_name='Comprimento'),
        ),
        migrations.AddField(
            model_name='bobine',
            name='designacao_prod',
            field=models.CharField(blank=True, choices=[('NONWOVEN ELASTIC BANDS ELA-ACE 100 HE', 'NONWOVEN ELASTIC BANDS ELA-ACE 100 HE'), ('STRETCHABLE NONWOVEN ELASTIC BANDS ELA-ACE 100 HE', 'STRETCHABLE NONWOVEN ELASTIC BANDS ELA-ACE 100 HE'), ('NONWOVEN ELASTIC BANDS ELA-ACE 90 HE', 'NONWOVEN ELASTIC BANDS ELA-ACE 90 HE'), ('NONWOVEN ELASTIC BANDS ELA-ACE 100 HT', 'NONWOVEN ELASTIC BANDS ELA-ACE 100 HT'), ('NONWOVEN ELASTIC BANDS ELA-ACE 95 HT', 'NONWOVEN ELASTIC BANDS ELA-ACE 95 HT'), ('NONWOVEN ELASTIC BANDS ELA-ACE 95 HE', 'NONWOVEN ELASTIC BANDS ELA-ACE 95 HE'), ('NONWOVEN ELASTIC BANDS ELA-SPUN 90 HE HL', 'NONWOVEN ELASTIC BANDS ELA-SPUN 90 HE HL'), ('NONWOVEN ELASTIC BANDS ELA-SPUN 95 HE HL', 'NONWOVEN ELASTIC BANDS ELA-SPUN 95 HE HL'), ('NONWOVEN ELASTIC BANDS ELA-SPUN 90 HT HL', 'NONWOVEN ELASTIC BANDS ELA-SPUN 90 HT HL'), ('NONWOVEN ELASTIC BANDS ELA-SPUN 95 HE HL', 'NONWOVEN ELASTIC BANDS ELA-SPUN 95 HE HL'), ('NONWOVEN ELASTIC BANDS ELA-SPUN 100 HE HL', 'NONWOVEN ELASTIC BANDS ELA-SPUN 100 HE HL'), ('SIDE PANEL ELA-ACE 100 HE', 'SIDE PANEL ELA-ACE 100 HE'), ('NONWOVEN ELASTIC BANDS ELA-SPUN 100 HE BICO', 'NONWOVEN ELASTIC BANDS ELA-SPUN 100 HE BICO'), ('NONWOVEN ELASTIC BANDS ELA-ACE 105 HE', 'NONWOVEN ELASTIC BANDS ELA-ACE 105 HE'), ('NONWOVEN ELASTIC BANDS ELA-ACE 100 HE(D)', 'NONWOVEN ELASTIC BANDS ELA-ACE 100 HE(D)'), ('FRONTAL TAPE 48', 'FRONTAL TAPE 48'), ('CAR PROTECTION SHEET 57', 'CAR PROTECTION SHEET 57'), ('ELASTIC FILM', 'ELASTIC FILM'), ('NONWOVEN ELASTIC BANDS ELA-ACE 100 HE(L)', 'NONWOVEN ELASTIC BANDS ELA-ACE 100 HE(L)'), ('NONWOVEN ELASTIC BANDS ELA-ACE 75 HE', 'NONWOVEN ELASTIC BANDS ELA-ACE 75 HE'), ('NONWOVEN ELASTIC BANDS ELA-SPUN 60 HE', 'NONWOVEN ELASTIC BANDS ELA-SPUN 60 HE'), ('NONWOVEN ELASTIC BANDS ELA-SPUN 60 HT', 'NONWOVEN ELASTIC BANDS ELA-SPUN 60 HT'), ('NONWOVEN TEXTILE BACKSHEET ELA-TBS 50 23B', 'NONWOVEN TEXTILE BACKSHEET ELA-TBS 50 23B'), ('NONWOVEN TEXTILE BACKSHEET ELA-TBS 50 23A', 'NONWOVEN TEXTILE BACKSHEET ELA-TBS 50 23A'), ('NONWOVEN TEXTILE BACKSHEET ELA-TBS 45 16B', 'NONWOVEN TEXTILE BACKSHEET ELA-TBS 45 16B'), ('NONWOVEN TEXTILE BACKSHEET ELA-TBS 45 16A', 'NONWOVEN TEXTILE BACKSHEET ELA-TBS 45 16A')], default='', max_length=100, null=True, verbose_name='Produto'),
        ),
        migrations.AlterField(
            model_name='artigo',
            name='gsm',
            field=models.CharField(blank=True, choices=[('105', '105 gsm'), ('100', '100 gsm'), ('95', '95 gsm'), ('90', '90 gsm'), ('80', '80 gsm'), ('60', '60 gsm'), ('75', '75 gsm'), ('57', '57 gsm'), ('50', '50 gsm'), ('48', '48 gsm'), ('45', '45 gsm')], max_length=10, null=True, verbose_name='Gramagem'),
        ),
        migrations.AlterField(
            model_name='artigo',
            name='produto',
            field=models.CharField(choices=[('NONWOVEN ELASTIC BANDS ELA-ACE 100 HE', 'NONWOVEN ELASTIC BANDS ELA-ACE 100 HE'), ('STRETCHABLE NONWOVEN ELASTIC BANDS ELA-ACE 100 HE', 'STRETCHABLE NONWOVEN ELASTIC BANDS ELA-ACE 100 HE'), ('NONWOVEN ELASTIC BANDS ELA-ACE 90 HE', 'NONWOVEN ELASTIC BANDS ELA-ACE 90 HE'), ('NONWOVEN ELASTIC BANDS ELA-ACE 100 HT', 'NONWOVEN ELASTIC BANDS ELA-ACE 100 HT'), ('NONWOVEN ELASTIC BANDS ELA-ACE 95 HT', 'NONWOVEN ELASTIC BANDS ELA-ACE 95 HT'), ('NONWOVEN ELASTIC BANDS ELA-ACE 95 HE', 'NONWOVEN ELASTIC BANDS ELA-ACE 95 HE'), ('NONWOVEN ELASTIC BANDS ELA-SPUN 90 HE HL', 'NONWOVEN ELASTIC BANDS ELA-SPUN 90 HE HL'), ('NONWOVEN ELASTIC BANDS ELA-SPUN 95 HE HL', 'NONWOVEN ELASTIC BANDS ELA-SPUN 95 HE HL'), ('NONWOVEN ELASTIC BANDS ELA-SPUN 90 HT HL', 'NONWOVEN ELASTIC BANDS ELA-SPUN 90 HT HL'), ('NONWOVEN ELASTIC BANDS ELA-SPUN 95 HE HL', 'NONWOVEN ELASTIC BANDS ELA-SPUN 95 HE HL'), ('NONWOVEN ELASTIC BANDS ELA-SPUN 100 HE HL', 'NONWOVEN ELASTIC BANDS ELA-SPUN 100 HE HL'), ('SIDE PANEL ELA-ACE 100 HE', 'SIDE PANEL ELA-ACE 100 HE'), ('NONWOVEN ELASTIC BANDS ELA-SPUN 100 HE BICO', 'NONWOVEN ELASTIC BANDS ELA-SPUN 100 HE BICO'), ('NONWOVEN ELASTIC BANDS ELA-ACE 105 HE', 'NONWOVEN ELASTIC BANDS ELA-ACE 105 HE'), ('NONWOVEN ELASTIC BANDS ELA-ACE 100 HE(D)', 'NONWOVEN ELASTIC BANDS ELA-ACE 100 HE(D)'), ('FRONTAL TAPE 48', 'FRONTAL TAPE 48'), ('CAR PROTECTION SHEET 57', 'CAR PROTECTION SHEET 57'), ('ELASTIC FILM', 'ELASTIC FILM'), ('NONWOVEN ELASTIC BANDS ELA-ACE 100 HE(L)', 'NONWOVEN ELASTIC BANDS ELA-ACE 100 HE(L)'), ('NONWOVEN ELASTIC BANDS ELA-ACE 75 HE', 'NONWOVEN ELASTIC BANDS ELA-ACE 75 HE'), ('NONWOVEN ELASTIC BANDS ELA-SPUN 60 HE', 'NONWOVEN ELASTIC BANDS ELA-SPUN 60 HE'), ('NONWOVEN ELASTIC BANDS ELA-SPUN 60 HT', 'NONWOVEN ELASTIC BANDS ELA-SPUN 60 HT'), ('NONWOVEN TEXTILE BACKSHEET ELA-TBS 50 23B', 'NONWOVEN TEXTILE BACKSHEET ELA-TBS 50 23B'), ('NONWOVEN TEXTILE BACKSHEET ELA-TBS 50 23A', 'NONWOVEN TEXTILE BACKSHEET ELA-TBS 50 23A'), ('NONWOVEN TEXTILE BACKSHEET ELA-TBS 45 16B', 'NONWOVEN TEXTILE BACKSHEET ELA-TBS 45 16B'), ('NONWOVEN TEXTILE BACKSHEET ELA-TBS 45 16A', 'NONWOVEN TEXTILE BACKSHEET ELA-TBS 45 16A')], default='', max_length=100, verbose_name='Produto'),
        ),
        migrations.AlterField(
            model_name='artigocliente',
            name='cod_client',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Cód. Cliente'),
        ),
        migrations.AlterField(
            model_name='bobinagem',
            name='tiponwinf',
            field=models.CharField(blank=True, choices=[('Suominen 25 gsm', 'Suominen 25 gsm'), ('Sandler SPUNLACE 100%PP', 'Sandler SPUNLACE 100%PP'), ('BCN 70%PP/30%PE', 'BCN 70%PP/30%PE'), ('Sandler', 'Sandler'), ('PEGAS BICO 17gsm', 'PEGAS BICO 17gsm'), ('Suominen', 'Suominen'), ('BCN', 'BCN'), ('ORMA', 'ORMA'), ('PEGAS 22', 'PEGAS 22'), ('SAWASOFT', 'SAWASOFT'), ('SAWABOND', 'SAWABOND'), ('Teksis', 'Teksis'), ('Union', 'Union'), ('Radici', 'Radici'), ('Fitesa', 'Fitesa'), ('ALBIS 23', 'ALBIS 23'), ('ALBIS 16', 'ALBIS 16'), ('Union Pillow', 'Union Pillow'), ('Union UV', 'Union UV'), ('Jacob Holm', 'Jacob Holm')], default='', max_length=40, null=True, verbose_name='Tipo Nonwoven Inferior'),
        ),
        migrations.AlterField(
            model_name='bobinagem',
            name='tiponwsup',
            field=models.CharField(blank=True, choices=[('Suominen 25 gsm', 'Suominen 25 gsm'), ('Sandler SPUNLACE 100%PP', 'Sandler SPUNLACE 100%PP'), ('BCN 70%PP/30%PE', 'BCN 70%PP/30%PE'), ('Sandler', 'Sandler'), ('PEGAS BICO 17gsm', 'PEGAS BICO 17gsm'), ('Suominen', 'Suominen'), ('BCN', 'BCN'), ('ORMA', 'ORMA'), ('PEGAS 22', 'PEGAS 22'), ('SAWASOFT', 'SAWASOFT'), ('SAWABOND', 'SAWABOND'), ('Teksis', 'Teksis'), ('Union', 'Union'), ('Radici', 'Radici'), ('Fitesa', 'Fitesa'), ('ALBIS 23', 'ALBIS 23'), ('ALBIS 16', 'ALBIS 16'), ('Union Pillow', 'Union Pillow'), ('Union UV', 'Union UV'), ('Jacob Holm', 'Jacob Holm')], default='', max_length=40, null=True, verbose_name='Tipo Nonwoven Superior'),
        ),
        migrations.AlterField(
            model_name='largura',
            name='designacao_prod',
            field=models.CharField(choices=[('NONWOVEN ELASTIC BANDS ELA-ACE 100 HE', 'NONWOVEN ELASTIC BANDS ELA-ACE 100 HE'), ('STRETCHABLE NONWOVEN ELASTIC BANDS ELA-ACE 100 HE', 'STRETCHABLE NONWOVEN ELASTIC BANDS ELA-ACE 100 HE'), ('NONWOVEN ELASTIC BANDS ELA-ACE 90 HE', 'NONWOVEN ELASTIC BANDS ELA-ACE 90 HE'), ('NONWOVEN ELASTIC BANDS ELA-ACE 100 HT', 'NONWOVEN ELASTIC BANDS ELA-ACE 100 HT'), ('NONWOVEN ELASTIC BANDS ELA-ACE 95 HT', 'NONWOVEN ELASTIC BANDS ELA-ACE 95 HT'), ('NONWOVEN ELASTIC BANDS ELA-ACE 95 HE', 'NONWOVEN ELASTIC BANDS ELA-ACE 95 HE'), ('NONWOVEN ELASTIC BANDS ELA-SPUN 90 HE HL', 'NONWOVEN ELASTIC BANDS ELA-SPUN 90 HE HL'), ('NONWOVEN ELASTIC BANDS ELA-SPUN 95 HE HL', 'NONWOVEN ELASTIC BANDS ELA-SPUN 95 HE HL'), ('NONWOVEN ELASTIC BANDS ELA-SPUN 90 HT HL', 'NONWOVEN ELASTIC BANDS ELA-SPUN 90 HT HL'), ('NONWOVEN ELASTIC BANDS ELA-SPUN 95 HE HL', 'NONWOVEN ELASTIC BANDS ELA-SPUN 95 HE HL'), ('NONWOVEN ELASTIC BANDS ELA-SPUN 100 HE HL', 'NONWOVEN ELASTIC BANDS ELA-SPUN 100 HE HL'), ('SIDE PANEL ELA-ACE 100 HE', 'SIDE PANEL ELA-ACE 100 HE'), ('NONWOVEN ELASTIC BANDS ELA-SPUN 100 HE BICO', 'NONWOVEN ELASTIC BANDS ELA-SPUN 100 HE BICO'), ('NONWOVEN ELASTIC BANDS ELA-ACE 105 HE', 'NONWOVEN ELASTIC BANDS ELA-ACE 105 HE'), ('NONWOVEN ELASTIC BANDS ELA-ACE 100 HE(D)', 'NONWOVEN ELASTIC BANDS ELA-ACE 100 HE(D)'), ('FRONTAL TAPE 48', 'FRONTAL TAPE 48'), ('CAR PROTECTION SHEET 57', 'CAR PROTECTION SHEET 57'), ('ELASTIC FILM', 'ELASTIC FILM'), ('NONWOVEN ELASTIC BANDS ELA-ACE 100 HE(L)', 'NONWOVEN ELASTIC BANDS ELA-ACE 100 HE(L)'), ('NONWOVEN ELASTIC BANDS ELA-ACE 75 HE', 'NONWOVEN ELASTIC BANDS ELA-ACE 75 HE'), ('NONWOVEN ELASTIC BANDS ELA-SPUN 60 HE', 'NONWOVEN ELASTIC BANDS ELA-SPUN 60 HE'), ('NONWOVEN ELASTIC BANDS ELA-SPUN 60 HT', 'NONWOVEN ELASTIC BANDS ELA-SPUN 60 HT'), ('NONWOVEN TEXTILE BACKSHEET ELA-TBS 50 23B', 'NONWOVEN TEXTILE BACKSHEET ELA-TBS 50 23B'), ('NONWOVEN TEXTILE BACKSHEET ELA-TBS 50 23A', 'NONWOVEN TEXTILE BACKSHEET ELA-TBS 50 23A'), ('NONWOVEN TEXTILE BACKSHEET ELA-TBS 45 16B', 'NONWOVEN TEXTILE BACKSHEET ELA-TBS 45 16B'), ('NONWOVEN TEXTILE BACKSHEET ELA-TBS 45 16A', 'NONWOVEN TEXTILE BACKSHEET ELA-TBS 45 16A')], default='', max_length=100, verbose_name='Produto'),
        ),
        migrations.AlterField(
            model_name='largura',
            name='gsm',
            field=models.CharField(blank=True, choices=[('105', '105 gsm'), ('100', '100 gsm'), ('95', '95 gsm'), ('90', '90 gsm'), ('80', '80 gsm'), ('60', '60 gsm'), ('75', '75 gsm'), ('57', '57 gsm'), ('50', '50 gsm'), ('48', '48 gsm'), ('45', '45 gsm')], max_length=7, null=True, verbose_name='Gramagem'),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='gramagem',
            field=models.CharField(blank=True, choices=[('105', '105 gsm'), ('100', '100 gsm'), ('95', '95 gsm'), ('90', '90 gsm'), ('75', '75 gsm'), ('80', '80 gsm'), ('60', '60 gsm'), ('57', '57 gsm'), ('50', '50 gsm'), ('48', '48 gsm'), ('45', '45 gsm')], max_length=10, null=True, verbose_name='Gramagem'),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='produto',
            field=models.CharField(choices=[('NONWOVEN ELASTIC BANDS ELA-ACE 100 HE', 'NONWOVEN ELASTIC BANDS ELA-ACE 100 HE'), ('STRETCHABLE NONWOVEN ELASTIC BANDS ELA-ACE 100 HE', 'STRETCHABLE NONWOVEN ELASTIC BANDS ELA-ACE 100 HE'), ('NONWOVEN ELASTIC BANDS ELA-ACE 90 HE', 'NONWOVEN ELASTIC BANDS ELA-ACE 90 HE'), ('NONWOVEN ELASTIC BANDS ELA-ACE 100 HT', 'NONWOVEN ELASTIC BANDS ELA-ACE 100 HT'), ('NONWOVEN ELASTIC BANDS ELA-ACE 95 HT', 'NONWOVEN ELASTIC BANDS ELA-ACE 95 HT'), ('NONWOVEN ELASTIC BANDS ELA-ACE 95 HE', 'NONWOVEN ELASTIC BANDS ELA-ACE 95 HE'), ('NONWOVEN ELASTIC BANDS ELA-SPUN 90 HE HL', 'NONWOVEN ELASTIC BANDS ELA-SPUN 90 HE HL'), ('NONWOVEN ELASTIC BANDS ELA-SPUN 95 HE HL', 'NONWOVEN ELASTIC BANDS ELA-SPUN 95 HE HL'), ('NONWOVEN ELASTIC BANDS ELA-SPUN 90 HT HL', 'NONWOVEN ELASTIC BANDS ELA-SPUN 90 HT HL'), ('NONWOVEN ELASTIC BANDS ELA-SPUN 95 HE HL', 'NONWOVEN ELASTIC BANDS ELA-SPUN 95 HE HL'), ('NONWOVEN ELASTIC BANDS ELA-SPUN 100 HE HL', 'NONWOVEN ELASTIC BANDS ELA-SPUN 100 HE HL'), ('SIDE PANEL ELA-ACE 100 HE', 'SIDE PANEL ELA-ACE 100 HE'), ('NONWOVEN ELASTIC BANDS ELA-SPUN 100 HE BICO', 'NONWOVEN ELASTIC BANDS ELA-SPUN 100 HE BICO'), ('NONWOVEN ELASTIC BANDS ELA-ACE 105 HE', 'NONWOVEN ELASTIC BANDS ELA-ACE 105 HE'), ('NONWOVEN ELASTIC BANDS ELA-ACE 100 HE(D)', 'NONWOVEN ELASTIC BANDS ELA-ACE 100 HE(D)'), ('FRONTAL TAPE 48', 'FRONTAL TAPE 48'), ('CAR PROTECTION SHEET 57', 'CAR PROTECTION SHEET 57'), ('ELASTIC FILM', 'ELASTIC FILM'), ('NONWOVEN ELASTIC BANDS ELA-ACE 100 HE(L)', 'NONWOVEN ELASTIC BANDS ELA-ACE 100 HE(L)'), ('NONWOVEN ELASTIC BANDS ELA-ACE 75 HE', 'NONWOVEN ELASTIC BANDS ELA-ACE 75 HE'), ('NONWOVEN ELASTIC BANDS ELA-SPUN 60 HE', 'NONWOVEN ELASTIC BANDS ELA-SPUN 60 HE'), ('NONWOVEN ELASTIC BANDS ELA-SPUN 60 HT', 'NONWOVEN ELASTIC BANDS ELA-SPUN 60 HT'), ('NONWOVEN TEXTILE BACKSHEET ELA-TBS 50 23B', 'NONWOVEN TEXTILE BACKSHEET ELA-TBS 50 23B'), ('NONWOVEN TEXTILE BACKSHEET ELA-TBS 50 23A', 'NONWOVEN TEXTILE BACKSHEET ELA-TBS 50 23A'), ('NONWOVEN TEXTILE BACKSHEET ELA-TBS 45 16B', 'NONWOVEN TEXTILE BACKSHEET ELA-TBS 45 16B'), ('NONWOVEN TEXTILE BACKSHEET ELA-TBS 45 16A', 'NONWOVEN TEXTILE BACKSHEET ELA-TBS 45 16A')], default='', max_length=100, verbose_name='Produto'),
        ),
    ]
