# Generated by Django 2.1.3 on 2019-04-01 06:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('producao', '0021_carga_metros'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='carga',
            options={'ordering': ['-data', '-carga'], 'verbose_name_plural': 'Cargas'},
        ),
        migrations.AlterModelOptions(
            name='encomenda',
            options={'ordering': ['-data', '-eef'], 'verbose_name_plural': 'Encomendas'},
        ),
    ]