# Generated by Django 2.2.7 on 2020-04-03 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('producao', '0083_auto_20200331_1540'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bobine',
            name='estado',
            field=models.CharField(choices=[('G', 'G'), ('DM', 'DM12'), ('R', 'R'), ('BA', 'BA'), ('LAB', 'LAB'), ('IND', 'IND'), ('HOLD', 'HOLD'), ('SC', 'SC')], default='G', max_length=4, verbose_name='Estado'),
        ),
    ]
