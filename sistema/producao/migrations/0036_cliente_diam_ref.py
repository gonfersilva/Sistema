# Generated by Django 2.2 on 2019-05-07 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('producao', '0035_auto_20190506_1543'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='diam_ref',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Diametro de referência'),
        ),
    ]
