# Generated by Django 2.2.7 on 2020-04-28 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('producao', '0094_auto_20200427_0952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='etiquetareciclado',
            name='timestamp',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]