# Generated by Django 2.2.7 on 2020-07-05 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('producao', '0107_auto_20200626_1212'),
    ]

    operations = [
        migrations.AddField(
            model_name='etiquetafinal',
            name='turno',
            field=models.CharField(blank=True, max_length=1, null=True, verbose_name='Turno'),
        ),
    ]
