# Generated by Django 2.2.7 on 2020-02-07 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('producao', '0076_auto_20200207_1237'),
    ]

    operations = [
        migrations.AddField(
            model_name='nonwoven',
            name='descricao',
            field=models.CharField(blank=True, max_length=50, null=True, unique=True, verbose_name='Stack number'),
        ),
    ]