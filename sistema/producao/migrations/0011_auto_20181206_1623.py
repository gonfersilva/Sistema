# Generated by Django 2.1.3 on 2018-12-06 16:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('producao', '0010_auto_20181121_1652'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bobinagem',
            options={'get_latest_by': ['data', 'fim'], 'ordering': ['-data', '-fim', '-nome'], 'verbose_name_plural': 'Bobinagens'},
        ),
    ]
