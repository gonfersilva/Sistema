# Generated by Django 2.2.7 on 2020-09-02 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('producao', '0120_palete_ordem_original_stock'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artigo',
            name='gsm',
            field=models.CharField(blank=True, choices=[('105', '105 gsm'), ('100', '100 gsm'), ('95', '95 gsm'), ('90', '90 gsm'), ('80', '80 gsm'), ('60', '60 gsm'), ('75', '75 gsm'), ('57', '57 gsm'), ('50', '50 gsm'), ('48', '48 gsm'), ('45', '45 gsm'), ('25', '25 gsm')], max_length=10, null=True, verbose_name='Gramagem'),
        ),
        migrations.AlterField(
            model_name='bobinagem',
            name='tiponwinf',
            field=models.CharField(blank=True, choices=[('Suominen 25 gsm', 'Suominen 25 gsm'), ('Sandler SPUNLACE 100%PP', 'Sandler SPUNLACE 100%PP'), ('BCN 70%PP/30%PE', 'BCN 70%PP/30%PE'), ('Sandler', 'Sandler'), ('PEGAS BICO 17gsm', 'PEGAS BICO 17gsm'), ('Suominen', 'Suominen'), ('BCN', 'BCN'), ('ORMA', 'ORMA'), ('PEGAS 22', 'PEGAS 22'), ('SAWASOFT', 'SAWASOFT'), ('SAWABOND', 'SAWABOND'), ('Teksis', 'Teksis'), ('Union', 'Union'), ('Radici', 'Radici'), ('Fitesa', 'Fitesa'), ('ALBIS 23', 'ALBIS 23'), ('ALBIS 16', 'ALBIS 16'), ('Union Pillow', 'Union Pillow'), ('Union UV', 'Union UV'), ('Jacob Holm', 'Jacob Holm'), ('Nonwoven Nikoo 25gsm Spunlace 100PP', 'Nonwoven Nikoo 25gsm Spunlace 100PP')], default='', max_length=40, null=True, verbose_name='Tipo Nonwoven Inferior'),
        ),
        migrations.AlterField(
            model_name='bobinagem',
            name='tiponwsup',
            field=models.CharField(blank=True, choices=[('Suominen 25 gsm', 'Suominen 25 gsm'), ('Sandler SPUNLACE 100%PP', 'Sandler SPUNLACE 100%PP'), ('BCN 70%PP/30%PE', 'BCN 70%PP/30%PE'), ('Sandler', 'Sandler'), ('PEGAS BICO 17gsm', 'PEGAS BICO 17gsm'), ('Suominen', 'Suominen'), ('BCN', 'BCN'), ('ORMA', 'ORMA'), ('PEGAS 22', 'PEGAS 22'), ('SAWASOFT', 'SAWASOFT'), ('SAWABOND', 'SAWABOND'), ('Teksis', 'Teksis'), ('Union', 'Union'), ('Radici', 'Radici'), ('Fitesa', 'Fitesa'), ('ALBIS 23', 'ALBIS 23'), ('ALBIS 16', 'ALBIS 16'), ('Union Pillow', 'Union Pillow'), ('Union UV', 'Union UV'), ('Jacob Holm', 'Jacob Holm'), ('Nonwoven Nikoo 25gsm Spunlace 100PP', 'Nonwoven Nikoo 25gsm Spunlace 100PP')], default='', max_length=40, null=True, verbose_name='Tipo Nonwoven Superior'),
        ),
        migrations.AlterField(
            model_name='largura',
            name='gsm',
            field=models.CharField(blank=True, choices=[('105', '105 gsm'), ('100', '100 gsm'), ('95', '95 gsm'), ('90', '90 gsm'), ('80', '80 gsm'), ('60', '60 gsm'), ('75', '75 gsm'), ('57', '57 gsm'), ('50', '50 gsm'), ('48', '48 gsm'), ('45', '45 gsm'), ('25', '25 gsm')], max_length=7, null=True, verbose_name='Gramagem'),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='gramagem',
            field=models.CharField(blank=True, choices=[('105', '105 gsm'), ('100', '100 gsm'), ('95', '95 gsm'), ('90', '90 gsm'), ('75', '75 gsm'), ('80', '80 gsm'), ('60', '60 gsm'), ('57', '57 gsm'), ('50', '50 gsm'), ('48', '48 gsm'), ('45', '45 gsm'), ('25', '25 gsm')], max_length=10, null=True, verbose_name='Gramagem'),
        ),
    ]
