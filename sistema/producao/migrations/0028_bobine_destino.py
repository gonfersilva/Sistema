# Generated by Django 2.2 on 2019-04-30 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('producao', '0027_palete_destino'),
    ]

    operations = [
        migrations.AddField(
            model_name='bobine',
            name='destino',
            field=models.TextField(blank=True, default='', max_length=500, null=True, verbose_name='Destino'),
        ),
    ]