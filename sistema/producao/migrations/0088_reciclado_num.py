# Generated by Django 2.2.7 on 2020-04-19 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('producao', '0087_auto_20200418_0632'),
    ]

    operations = [
        migrations.AddField(
            model_name='reciclado',
            name='num',
            field=models.PositiveIntegerField(default=0, verbose_name='Número'),
        ),
    ]