# Generated by Django 2.2.7 on 2020-07-29 16:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('planeamento', '0007_ordemproducao_completa'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ordemproducao',
            options={'ordering': ['-ativa'], 'verbose_name_plural': 'Ordens de Produção'},
        ),
    ]
