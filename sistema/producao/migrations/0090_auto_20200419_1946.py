# Generated by Django 2.2.7 on 2020-04-19 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('producao', '0089_reciclado_timestamp_edit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reciclado',
            name='timestamp_edit',
            field=models.DateTimeField(),
        ),
    ]