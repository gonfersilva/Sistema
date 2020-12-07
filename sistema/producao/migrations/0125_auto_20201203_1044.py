# Generated by Django 2.2.7 on 2020-12-03 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('producao', '0124_palete_num_palete_ordem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artigo',
            name='produto',
            field=models.CharField(choices=[('NONWOVEN ELASTIC BANDS ELA-ACE 100 HE', 'NONWOVEN ELASTIC BANDS ELA-ACE 100 HE'), ('STRETCHABLE NONWOVEN ELASTIC BANDS ELA-ACE 100 HE', 'STRETCHABLE NONWOVEN ELASTIC BANDS ELA-ACE 100 HE'), ('NONWOVEN ELASTIC BANDS ELA-ACE 90 HE', 'NONWOVEN ELASTIC BANDS ELA-ACE 90 HE'), ('NONWOVEN ELASTIC BANDS ELA-ACE 100 HT', 'NONWOVEN ELASTIC BANDS ELA-ACE 100 HT'), ('NONWOVEN ELASTIC BANDS ELA-ACE 95 HT', 'NONWOVEN ELASTIC BANDS ELA-ACE 95 HT'), ('NONWOVEN ELASTIC BANDS ELA-ACE 95 HE', 'NONWOVEN ELASTIC BANDS ELA-ACE 95 HE'), ('NONWOVEN ELASTIC BANDS ELA-SPUN 90 HE HL', 'NONWOVEN ELASTIC BANDS ELA-SPUN 90 HE HL'), ('NONWOVEN ELASTIC BANDS ELA-SPUN 95 HE HL', 'NONWOVEN ELASTIC BANDS ELA-SPUN 95 HE HL'), ('NONWOVEN ELASTIC BANDS ELA-SPUN 90 HT HL', 'NONWOVEN ELASTIC BANDS ELA-SPUN 90 HT HL'), ('NONWOVEN ELASTIC BANDS ELA-SPUN 95 HE HL', 'NONWOVEN ELASTIC BANDS ELA-SPUN 95 HE HL'), ('NONWOVEN ELASTIC BANDS ELA-SPUN 100 HE HL', 'NONWOVEN ELASTIC BANDS ELA-SPUN 100 HE HL'), ('SIDE PANEL ELA-ACE 100 HE', 'SIDE PANEL ELA-ACE 100 HE'), ('NONWOVEN ELASTIC BANDS ELA-SPUN 100 HE BICO', 'NONWOVEN ELASTIC BANDS ELA-SPUN 100 HE BICO'), ('NONWOVEN ELASTIC BANDS ELA-ACE 105 HE', 'NONWOVEN ELASTIC BANDS ELA-ACE 105 HE'), ('NONWOVEN ELASTIC BANDS ELA-ACE 100 HE(D)', 'NONWOVEN ELASTIC BANDS ELA-ACE 100 HE(D)'), ('FRONTAL TAPE 48', 'FRONTAL TAPE 48'), ('CAR PROTECTION SHEET 57', 'CAR PROTECTION SHEET 57'), ('ELASTIC FILM', 'ELASTIC FILM'), ('NONWOVEN ELASTIC BANDS ELA-ACE 100 HE(L)', 'NONWOVEN ELASTIC BANDS ELA-ACE 100 HE(L)'), ('NONWOVEN ELASTIC BANDS ELA-ACE 75 HE', 'NONWOVEN ELASTIC BANDS ELA-ACE 75 HE'), ('NONWOVEN ELASTIC BANDS ELA-SPUN 60 HE', 'NONWOVEN ELASTIC BANDS ELA-SPUN 60 HE'), ('NONWOVEN ELASTIC BANDS ELA-SPUN 60 HT', 'NONWOVEN ELASTIC BANDS ELA-SPUN 60 HT'), ('NONWOVEN TEXTILE BACKSHEET ELA-TBS 50 23B', 'NONWOVEN TEXTILE BACKSHEET ELA-TBS 50 23B'), ('NONWOVEN TEXTILE BACKSHEET ELA-TBS 50 23A', 'NONWOVEN TEXTILE BACKSHEET ELA-TBS 50 23A'), ('NONWOVEN TEXTILE BACKSHEET ELA-TBS 45 16B', 'NONWOVEN TEXTILE BACKSHEET ELA-TBS 45 16B'), ('NONWOVEN TEXTILE BACKSHEET ELA-TBS 45 16A', 'NONWOVEN TEXTILE BACKSHEET ELA-TBS 45 16A'), ('NONWOVEN ELASTIC BAND ELA-CARDED AMOSTRA', 'NONWOVEN ELASTIC BAND ELA-CARDED AMOSTRA'), ('NONWOVEN ELASTIC BAND ELA-SPUN 75 HT', 'NONWOVEN ELASTIC BAND ELA-SPUN 75 HT')], default='', max_length=100, verbose_name='Produto'),
        ),
        migrations.AlterField(
            model_name='bobinagem',
            name='tiponwinf',
            field=models.CharField(blank=True, choices=[('Suominen 25 gsm', 'Suominen 25 gsm'), ('Sandler SPUNLACE 100%PP', 'Sandler SPUNLACE 100%PP'), ('BCN 70%PP/30%PE', 'BCN 70%PP/30%PE'), ('Sandler', 'Sandler'), ('PEGAS BICO 17gsm', 'PEGAS BICO 17gsm'), ('Suominen', 'Suominen'), ('BCN', 'BCN'), ('ORMA', 'ORMA'), ('PEGAS 22', 'PEGAS 22'), ('SAWASOFT', 'SAWASOFT'), ('SAWABOND', 'SAWABOND'), ('Teksis', 'Teksis'), ('Union', 'Union'), ('Radici', 'Radici'), ('Fitesa', 'Fitesa'), ('ALBIS 23', 'ALBIS 23'), ('ALBIS 16', 'ALBIS 16'), ('Union Pillow', 'Union Pillow'), ('Union UV', 'Union UV'), ('Jacob Holm', 'Jacob Holm'), ('Nonwoven Nikoo 25gsm Spunlace 100PP', 'Nonwoven Nikoo 25gsm Spunlace 100PP'), ('ELA-ACE', 'ELA-ACE'), ('ELA-SPUN', 'ELA-SPUN')], default='', max_length=40, null=True, verbose_name='Tipo Nonwoven Inferior'),
        ),
        migrations.AlterField(
            model_name='bobinagem',
            name='tiponwsup',
            field=models.CharField(blank=True, choices=[('Suominen 25 gsm', 'Suominen 25 gsm'), ('Sandler SPUNLACE 100%PP', 'Sandler SPUNLACE 100%PP'), ('BCN 70%PP/30%PE', 'BCN 70%PP/30%PE'), ('Sandler', 'Sandler'), ('PEGAS BICO 17gsm', 'PEGAS BICO 17gsm'), ('Suominen', 'Suominen'), ('BCN', 'BCN'), ('ORMA', 'ORMA'), ('PEGAS 22', 'PEGAS 22'), ('SAWASOFT', 'SAWASOFT'), ('SAWABOND', 'SAWABOND'), ('Teksis', 'Teksis'), ('Union', 'Union'), ('Radici', 'Radici'), ('Fitesa', 'Fitesa'), ('ALBIS 23', 'ALBIS 23'), ('ALBIS 16', 'ALBIS 16'), ('Union Pillow', 'Union Pillow'), ('Union UV', 'Union UV'), ('Jacob Holm', 'Jacob Holm'), ('Nonwoven Nikoo 25gsm Spunlace 100PP', 'Nonwoven Nikoo 25gsm Spunlace 100PP'), ('ELA-ACE', 'ELA-ACE'), ('ELA-SPUN', 'ELA-SPUN')], default='', max_length=40, null=True, verbose_name='Tipo Nonwoven Superior'),
        ),
        migrations.AlterField(
            model_name='bobine',
            name='designacao_prod',
            field=models.CharField(blank=True, choices=[('NONWOVEN ELASTIC BANDS ELA-ACE 100 HE', 'NONWOVEN ELASTIC BANDS ELA-ACE 100 HE'), ('STRETCHABLE NONWOVEN ELASTIC BANDS ELA-ACE 100 HE', 'STRETCHABLE NONWOVEN ELASTIC BANDS ELA-ACE 100 HE'), ('NONWOVEN ELASTIC BANDS ELA-ACE 90 HE', 'NONWOVEN ELASTIC BANDS ELA-ACE 90 HE'), ('NONWOVEN ELASTIC BANDS ELA-ACE 100 HT', 'NONWOVEN ELASTIC BANDS ELA-ACE 100 HT'), ('NONWOVEN ELASTIC BANDS ELA-ACE 95 HT', 'NONWOVEN ELASTIC BANDS ELA-ACE 95 HT'), ('NONWOVEN ELASTIC BANDS ELA-ACE 95 HE', 'NONWOVEN ELASTIC BANDS ELA-ACE 95 HE'), ('NONWOVEN ELASTIC BANDS ELA-SPUN 90 HE HL', 'NONWOVEN ELASTIC BANDS ELA-SPUN 90 HE HL'), ('NONWOVEN ELASTIC BANDS ELA-SPUN 95 HE HL', 'NONWOVEN ELASTIC BANDS ELA-SPUN 95 HE HL'), ('NONWOVEN ELASTIC BANDS ELA-SPUN 90 HT HL', 'NONWOVEN ELASTIC BANDS ELA-SPUN 90 HT HL'), ('NONWOVEN ELASTIC BANDS ELA-SPUN 95 HE HL', 'NONWOVEN ELASTIC BANDS ELA-SPUN 95 HE HL'), ('NONWOVEN ELASTIC BANDS ELA-SPUN 100 HE HL', 'NONWOVEN ELASTIC BANDS ELA-SPUN 100 HE HL'), ('SIDE PANEL ELA-ACE 100 HE', 'SIDE PANEL ELA-ACE 100 HE'), ('NONWOVEN ELASTIC BANDS ELA-SPUN 100 HE BICO', 'NONWOVEN ELASTIC BANDS ELA-SPUN 100 HE BICO'), ('NONWOVEN ELASTIC BANDS ELA-ACE 105 HE', 'NONWOVEN ELASTIC BANDS ELA-ACE 105 HE'), ('NONWOVEN ELASTIC BANDS ELA-ACE 100 HE(D)', 'NONWOVEN ELASTIC BANDS ELA-ACE 100 HE(D)'), ('FRONTAL TAPE 48', 'FRONTAL TAPE 48'), ('CAR PROTECTION SHEET 57', 'CAR PROTECTION SHEET 57'), ('ELASTIC FILM', 'ELASTIC FILM'), ('NONWOVEN ELASTIC BANDS ELA-ACE 100 HE(L)', 'NONWOVEN ELASTIC BANDS ELA-ACE 100 HE(L)'), ('NONWOVEN ELASTIC BANDS ELA-ACE 75 HE', 'NONWOVEN ELASTIC BANDS ELA-ACE 75 HE'), ('NONWOVEN ELASTIC BANDS ELA-SPUN 60 HE', 'NONWOVEN ELASTIC BANDS ELA-SPUN 60 HE'), ('NONWOVEN ELASTIC BANDS ELA-SPUN 60 HT', 'NONWOVEN ELASTIC BANDS ELA-SPUN 60 HT'), ('NONWOVEN TEXTILE BACKSHEET ELA-TBS 50 23B', 'NONWOVEN TEXTILE BACKSHEET ELA-TBS 50 23B'), ('NONWOVEN TEXTILE BACKSHEET ELA-TBS 50 23A', 'NONWOVEN TEXTILE BACKSHEET ELA-TBS 50 23A'), ('NONWOVEN TEXTILE BACKSHEET ELA-TBS 45 16B', 'NONWOVEN TEXTILE BACKSHEET ELA-TBS 45 16B'), ('NONWOVEN TEXTILE BACKSHEET ELA-TBS 45 16A', 'NONWOVEN TEXTILE BACKSHEET ELA-TBS 45 16A'), ('NONWOVEN ELASTIC BAND ELA-CARDED AMOSTRA', 'NONWOVEN ELASTIC BAND ELA-CARDED AMOSTRA'), ('NONWOVEN ELASTIC BAND ELA-SPUN 75 HT', 'NONWOVEN ELASTIC BAND ELA-SPUN 75 HT')], default='', max_length=100, null=True, verbose_name='Produto'),
        ),
        migrations.AlterField(
            model_name='largura',
            name='designacao_prod',
            field=models.CharField(choices=[('NONWOVEN ELASTIC BANDS ELA-ACE 100 HE', 'NONWOVEN ELASTIC BANDS ELA-ACE 100 HE'), ('STRETCHABLE NONWOVEN ELASTIC BANDS ELA-ACE 100 HE', 'STRETCHABLE NONWOVEN ELASTIC BANDS ELA-ACE 100 HE'), ('NONWOVEN ELASTIC BANDS ELA-ACE 90 HE', 'NONWOVEN ELASTIC BANDS ELA-ACE 90 HE'), ('NONWOVEN ELASTIC BANDS ELA-ACE 100 HT', 'NONWOVEN ELASTIC BANDS ELA-ACE 100 HT'), ('NONWOVEN ELASTIC BANDS ELA-ACE 95 HT', 'NONWOVEN ELASTIC BANDS ELA-ACE 95 HT'), ('NONWOVEN ELASTIC BANDS ELA-ACE 95 HE', 'NONWOVEN ELASTIC BANDS ELA-ACE 95 HE'), ('NONWOVEN ELASTIC BANDS ELA-SPUN 90 HE HL', 'NONWOVEN ELASTIC BANDS ELA-SPUN 90 HE HL'), ('NONWOVEN ELASTIC BANDS ELA-SPUN 95 HE HL', 'NONWOVEN ELASTIC BANDS ELA-SPUN 95 HE HL'), ('NONWOVEN ELASTIC BANDS ELA-SPUN 90 HT HL', 'NONWOVEN ELASTIC BANDS ELA-SPUN 90 HT HL'), ('NONWOVEN ELASTIC BANDS ELA-SPUN 95 HE HL', 'NONWOVEN ELASTIC BANDS ELA-SPUN 95 HE HL'), ('NONWOVEN ELASTIC BANDS ELA-SPUN 100 HE HL', 'NONWOVEN ELASTIC BANDS ELA-SPUN 100 HE HL'), ('SIDE PANEL ELA-ACE 100 HE', 'SIDE PANEL ELA-ACE 100 HE'), ('NONWOVEN ELASTIC BANDS ELA-SPUN 100 HE BICO', 'NONWOVEN ELASTIC BANDS ELA-SPUN 100 HE BICO'), ('NONWOVEN ELASTIC BANDS ELA-ACE 105 HE', 'NONWOVEN ELASTIC BANDS ELA-ACE 105 HE'), ('NONWOVEN ELASTIC BANDS ELA-ACE 100 HE(D)', 'NONWOVEN ELASTIC BANDS ELA-ACE 100 HE(D)'), ('FRONTAL TAPE 48', 'FRONTAL TAPE 48'), ('CAR PROTECTION SHEET 57', 'CAR PROTECTION SHEET 57'), ('ELASTIC FILM', 'ELASTIC FILM'), ('NONWOVEN ELASTIC BANDS ELA-ACE 100 HE(L)', 'NONWOVEN ELASTIC BANDS ELA-ACE 100 HE(L)'), ('NONWOVEN ELASTIC BANDS ELA-ACE 75 HE', 'NONWOVEN ELASTIC BANDS ELA-ACE 75 HE'), ('NONWOVEN ELASTIC BANDS ELA-SPUN 60 HE', 'NONWOVEN ELASTIC BANDS ELA-SPUN 60 HE'), ('NONWOVEN ELASTIC BANDS ELA-SPUN 60 HT', 'NONWOVEN ELASTIC BANDS ELA-SPUN 60 HT'), ('NONWOVEN TEXTILE BACKSHEET ELA-TBS 50 23B', 'NONWOVEN TEXTILE BACKSHEET ELA-TBS 50 23B'), ('NONWOVEN TEXTILE BACKSHEET ELA-TBS 50 23A', 'NONWOVEN TEXTILE BACKSHEET ELA-TBS 50 23A'), ('NONWOVEN TEXTILE BACKSHEET ELA-TBS 45 16B', 'NONWOVEN TEXTILE BACKSHEET ELA-TBS 45 16B'), ('NONWOVEN TEXTILE BACKSHEET ELA-TBS 45 16A', 'NONWOVEN TEXTILE BACKSHEET ELA-TBS 45 16A'), ('NONWOVEN ELASTIC BAND ELA-CARDED AMOSTRA', 'NONWOVEN ELASTIC BAND ELA-CARDED AMOSTRA'), ('NONWOVEN ELASTIC BAND ELA-SPUN 75 HT', 'NONWOVEN ELASTIC BAND ELA-SPUN 75 HT')], default='', max_length=100, verbose_name='Produto'),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='produto',
            field=models.CharField(choices=[('NONWOVEN ELASTIC BANDS ELA-ACE 100 HE', 'NONWOVEN ELASTIC BANDS ELA-ACE 100 HE'), ('STRETCHABLE NONWOVEN ELASTIC BANDS ELA-ACE 100 HE', 'STRETCHABLE NONWOVEN ELASTIC BANDS ELA-ACE 100 HE'), ('NONWOVEN ELASTIC BANDS ELA-ACE 90 HE', 'NONWOVEN ELASTIC BANDS ELA-ACE 90 HE'), ('NONWOVEN ELASTIC BANDS ELA-ACE 100 HT', 'NONWOVEN ELASTIC BANDS ELA-ACE 100 HT'), ('NONWOVEN ELASTIC BANDS ELA-ACE 95 HT', 'NONWOVEN ELASTIC BANDS ELA-ACE 95 HT'), ('NONWOVEN ELASTIC BANDS ELA-ACE 95 HE', 'NONWOVEN ELASTIC BANDS ELA-ACE 95 HE'), ('NONWOVEN ELASTIC BANDS ELA-SPUN 90 HE HL', 'NONWOVEN ELASTIC BANDS ELA-SPUN 90 HE HL'), ('NONWOVEN ELASTIC BANDS ELA-SPUN 95 HE HL', 'NONWOVEN ELASTIC BANDS ELA-SPUN 95 HE HL'), ('NONWOVEN ELASTIC BANDS ELA-SPUN 90 HT HL', 'NONWOVEN ELASTIC BANDS ELA-SPUN 90 HT HL'), ('NONWOVEN ELASTIC BANDS ELA-SPUN 95 HE HL', 'NONWOVEN ELASTIC BANDS ELA-SPUN 95 HE HL'), ('NONWOVEN ELASTIC BANDS ELA-SPUN 100 HE HL', 'NONWOVEN ELASTIC BANDS ELA-SPUN 100 HE HL'), ('SIDE PANEL ELA-ACE 100 HE', 'SIDE PANEL ELA-ACE 100 HE'), ('NONWOVEN ELASTIC BANDS ELA-SPUN 100 HE BICO', 'NONWOVEN ELASTIC BANDS ELA-SPUN 100 HE BICO'), ('NONWOVEN ELASTIC BANDS ELA-ACE 105 HE', 'NONWOVEN ELASTIC BANDS ELA-ACE 105 HE'), ('NONWOVEN ELASTIC BANDS ELA-ACE 100 HE(D)', 'NONWOVEN ELASTIC BANDS ELA-ACE 100 HE(D)'), ('FRONTAL TAPE 48', 'FRONTAL TAPE 48'), ('CAR PROTECTION SHEET 57', 'CAR PROTECTION SHEET 57'), ('ELASTIC FILM', 'ELASTIC FILM'), ('NONWOVEN ELASTIC BANDS ELA-ACE 100 HE(L)', 'NONWOVEN ELASTIC BANDS ELA-ACE 100 HE(L)'), ('NONWOVEN ELASTIC BANDS ELA-ACE 75 HE', 'NONWOVEN ELASTIC BANDS ELA-ACE 75 HE'), ('NONWOVEN ELASTIC BANDS ELA-SPUN 60 HE', 'NONWOVEN ELASTIC BANDS ELA-SPUN 60 HE'), ('NONWOVEN ELASTIC BANDS ELA-SPUN 60 HT', 'NONWOVEN ELASTIC BANDS ELA-SPUN 60 HT'), ('NONWOVEN TEXTILE BACKSHEET ELA-TBS 50 23B', 'NONWOVEN TEXTILE BACKSHEET ELA-TBS 50 23B'), ('NONWOVEN TEXTILE BACKSHEET ELA-TBS 50 23A', 'NONWOVEN TEXTILE BACKSHEET ELA-TBS 50 23A'), ('NONWOVEN TEXTILE BACKSHEET ELA-TBS 45 16B', 'NONWOVEN TEXTILE BACKSHEET ELA-TBS 45 16B'), ('NONWOVEN TEXTILE BACKSHEET ELA-TBS 45 16A', 'NONWOVEN TEXTILE BACKSHEET ELA-TBS 45 16A'), ('NONWOVEN ELASTIC BAND ELA-CARDED AMOSTRA', 'NONWOVEN ELASTIC BAND ELA-CARDED AMOSTRA')], default='', max_length=100, verbose_name='Produto'),
        ),
    ]
