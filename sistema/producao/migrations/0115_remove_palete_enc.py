# Generated by Django 2.2.7 on 2020-07-29 17:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('producao', '0114_palete_ordem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='palete',
            name='enc',
        ),
    ]
