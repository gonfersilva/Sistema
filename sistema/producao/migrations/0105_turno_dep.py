# Generated by Django 2.2.7 on 2020-06-17 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('producao', '0104_turno'),
    ]

    operations = [
        migrations.AddField(
            model_name='turno',
            name='dep',
            field=models.CharField(blank=True, choices=[('Produção', 'Produção'), ('Logistica', 'Logistica'), ('Qualidade', 'Qualidade')], max_length=50),
        ),
    ]
