# Generated by Django 2.2.1 on 2019-10-17 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('producao', '0047_auto_20191017_1042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='etiquetaretrabalho',
            name='impressora',
            field=models.CharField(blank=True, choices=[('Bobinadora_CAB_A4_200', 'BOBINADORA'), ('DM12_CAB_A4_200', 'DM12')], max_length=200, null=True, verbose_name='Impressora'),
        ),
    ]
