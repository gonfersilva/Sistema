# Generated by Django 2.2 on 2019-05-02 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('producao', '0031_auto_20190502_1549'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artigo',
            name='gsm',
            field=models.CharField(blank=True, choices=[('100', '100 gsm'), ('95', '95 gsm'), ('90', '90 gsm'), ('80', '80 gsm')], max_length=10, null=True, verbose_name='Gramagem'),
        ),
    ]
