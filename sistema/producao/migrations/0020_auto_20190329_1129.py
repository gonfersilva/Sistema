# Generated by Django 2.1.3 on 2019-03-29 11:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('producao', '0019_auto_20190329_1118'),
    ]

    operations = [
        migrations.RenameField(
            model_name='encomenda',
            old_name='num_cargas_sctual',
            new_name='num_cargas_actual',
        ),
    ]