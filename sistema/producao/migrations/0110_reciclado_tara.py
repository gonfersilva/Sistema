# Generated by Django 2.2.7 on 2020-07-23 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('producao', '0109_auto_20200706_0930'),
    ]

    operations = [
        migrations.AddField(
            model_name='reciclado',
            name='tara',
            field=models.CharField(default='30 kg', max_length=5),
            preserve_default=False,
        ),
    ]