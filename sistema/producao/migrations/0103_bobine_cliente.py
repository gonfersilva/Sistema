# Generated by Django 2.2.7 on 2020-06-16 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('producao', '0102_bobine_diam'),
    ]

    operations = [
        migrations.AddField(
            model_name='bobine',
            name='cliente',
            field=models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='Cliente'),
        ),
    ]
