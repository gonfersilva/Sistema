# Generated by Django 2.2.7 on 2020-04-19 18:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('producao', '0088_reciclado_num'),
    ]

    operations = [
        migrations.AddField(
            model_name='reciclado',
            name='timestamp_edit',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
