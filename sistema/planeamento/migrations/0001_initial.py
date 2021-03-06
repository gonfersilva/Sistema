# Generated by Django 2.2.7 on 2020-07-28 20:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('producao', '0113_palete_enc'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CaracteristicasTecnicas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='CTInf',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('basis_weight', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Basis weight (gsm)')),
                ('tensile_peak', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Tensile at peak CD (N/25mm)')),
                ('elong_break_cd', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Elongation at break CD (%)')),
                ('elong_n_cd', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Elongation at 9.81N CD (%)')),
                ('load_five', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Load at 5% elongation 1st cycle CD (N/50 mm)')),
                ('load_ten', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Load at 10% elongation 1st cycle CD (N/50 mm)')),
                ('load_twenty', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Load at 20% elongation 1st cycle CD (N/50 mm)')),
                ('load_fifty', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Load at 50% elongation 1st cycle CD (N/50 mm)')),
                ('perm_set_second', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Permanent set 2nd cycle (%)')),
                ('load_hundred_second', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Load at 100% elongation 2nd cycle (N/50 mm)')),
                ('perm_set_third', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Permanent set 3rd cycle (%)')),
                ('load_hundred_third', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Load at 100% elongation 3rd cycle (N/50 mm)')),
                ('lamination_str', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Lamination strenght (CD) (N/25 mm)')),
            ],
        ),
        migrations.CreateModel(
            name='CTSup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('basis_weight', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Basis weight (gsm)')),
                ('tensile_peak', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Tensile at peak CD (N/25mm)')),
                ('elong_break_cd', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Elongation at break CD (%)')),
                ('elong_n_cd', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Elongation at 9.81N CD (%)')),
                ('load_five', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Load at 5% elongation 1st cycle CD (N/50 mm)')),
                ('load_ten', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Load at 10% elongation 1st cycle CD (N/50 mm)')),
                ('load_twenty', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Load at 20% elongation 1st cycle CD (N/50 mm)')),
                ('load_fifty', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Load at 50% elongation 1st cycle CD (N/50 mm)')),
                ('perm_set_second', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Permanent set 2nd cycle (%)')),
                ('load_hundred_second', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Load at 100% elongation 2nd cycle (N/50 mm)')),
                ('perm_set_third', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Permanent set 3rd cycle (%)')),
                ('load_hundred_third', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Load at 100% elongation 3rd cycle (N/50 mm)')),
                ('lamination_str', models.DecimalField(decimal_places=2, max_digits=5, verbose_name='Lamination strenght (CD) (N/25 mm)')),
            ],
        ),
        migrations.CreateModel(
            name='OrdemProducao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('op', models.CharField(max_length=200, verbose_name='Ordem de Produção')),
                ('largura', models.DecimalField(decimal_places=0, max_digits=6, verbose_name='Largura')),
                ('limsup', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Limite Superior')),
                ('liminf', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Limite Inferior')),
                ('core', models.CharField(max_length=1, verbose_name='Core')),
                ('num_paletes_produzir', models.IntegerField(default=0, verbose_name='Nº de paletes a produzir')),
                ('num_paletes_stock', models.IntegerField(default=0, verbose_name='Nº de paletes em stock')),
                ('num_paletes_total', models.IntegerField(default=0, verbose_name='Nº de paletes total')),
                ('emendas', models.CharField(max_length=200, verbose_name='Emendas')),
                ('nwsup', models.CharField(max_length=200, verbose_name='Nonwoven Superior')),
                ('nwinf', models.CharField(max_length=200, verbose_name='Nonwoven Inferior')),
                ('tipo_paletes', models.CharField(max_length=200, verbose_name='Tipo de Paletes')),
                ('palete_por_palete', models.IntegerField(default=1, verbose_name='Palete por Palete')),
                ('bobines_por_palete', models.IntegerField(default=0, verbose_name='Bobines por Palete')),
                ('enrolamento', models.CharField(max_length=100, verbose_name='Sentido do enrolamento')),
                ('folha_id', models.BooleanField(default=True, verbose_name='Folha de identificação de palete')),
                ('freq_amos', models.IntegerField(default=0, verbose_name='Frequência de amostragem por bobinagem')),
                ('limite_desc', models.DecimalField(decimal_places=0, max_digits=3, verbose_name='Limite Descentrado')),
                ('limite_con', models.DecimalField(decimal_places=0, max_digits=3, verbose_name='Limite Cónico')),
                ('diam_min', models.IntegerField(default=0, verbose_name='Diâmetro minimo')),
                ('diam_max', models.IntegerField(default=0, verbose_name='Diâmetro máximo')),
                ('stock', models.BooleanField(default=False, verbose_name='Stock')),
                ('ficha_processo', models.CharField(max_length=100, verbose_name='Ficha de Processo')),
                ('coa_aprov', models.CharField(max_length=100, verbose_name='Coa de Aprovação')),
                ('tipo_transporte', models.CharField(max_length=20, verbose_name='Tipo de Transporte')),
                ('paletes_camiao', models.IntegerField(default=0, verbose_name='Paletes por camião')),
                ('altura_max', models.DecimalField(decimal_places=2, max_digits=3, verbose_name='Altura máxima')),
                ('paletes_sobre', models.BooleanField(default=False, verbose_name='Paletes Sobrepostas')),
                ('cintas', models.BooleanField(default=False, verbose_name='Cintas')),
                ('topo', models.CharField(max_length=50, verbose_name='Topo')),
                ('base', models.CharField(max_length=50, verbose_name='Base')),
                ('embal', models.CharField(max_length=50, verbose_name='Embalamento')),
                ('etiqueta_bobine', models.IntegerField(default=1, verbose_name='Etiqueta por bobine')),
                ('etiqueta_palete', models.IntegerField(default=2, verbose_name='Etiqueta por palete')),
                ('etiqueta_final', models.IntegerField(default=1, verbose_name='Etiqueta final por palete')),
                ('artigo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='producao.Artigo', verbose_name='Artigo')),
                ('ct', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='planeamento.CaracteristicasTecnicas', verbose_name='Caracteristicas Técnicas')),
                ('enc', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='producao.Encomenda', verbose_name='Encomenda')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Username')),
            ],
        ),
        migrations.AddField(
            model_name='caracteristicastecnicas',
            name='ctinf',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='planeamento.CTInf', verbose_name='Caracteristicas Técnicas Inferior'),
        ),
        migrations.AddField(
            model_name='caracteristicastecnicas',
            name='ctsup',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='planeamento.CTSup', verbose_name='Caracteristicas Técnicas Superior'),
        ),
        migrations.AddField(
            model_name='caracteristicastecnicas',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Username'),
        ),
    ]
