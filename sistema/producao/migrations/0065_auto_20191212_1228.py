# Generated by Django 2.2.7 on 2019-12-12 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('producao', '0064_inventariobobinesdm_inventariopaletescliente'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='inventariobobinesdm',
            options={'verbose_name_plural': 'Inventário Bobines DM'},
        ),
        migrations.AlterModelOptions(
            name='inventariopaletescliente',
            options={'verbose_name_plural': 'Intentário Paletes Cliente'},
        ),
        migrations.AddField(
            model_name='inventariobobinesdm',
            name='nome',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='inventariopaletescliente',
            name='nome',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
