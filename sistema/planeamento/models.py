from django.db import models
import datetime, time
from django.conf import settings
from django.shortcuts import render, get_object_or_404, render_to_response, redirect
from django.db import models
from django.dispatch import receiver
from datetime import timedelta
from time import gmtime, strftime
from django.db.models import Max
from django.contrib.auth.models import User
from decimal import *
from producao.models import *

class CTSup(models.Model):
    basis_weight            = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Basis weight (gsm)")
    tensile_peak            = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Tensile at peak CD (N/25mm)")
    elong_break_cd          = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Elongation at break CD (%)")
    elong_n_cd              = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Elongation at 9.81N CD (%)")
    load_five               = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Load at 5% elongation 1st cycle CD (N/50 mm)")
    load_ten                = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Load at 10% elongation 1st cycle CD (N/50 mm)")
    load_twenty             = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Load at 20% elongation 1st cycle CD (N/50 mm)")
    load_fifty              = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Load at 50% elongation 1st cycle CD (N/50 mm)")
    perm_set_second         = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Permanent set 2nd cycle (%)")
    load_hundred_second     = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Load at 100% elongation 2nd cycle (N/50 mm)")
    perm_set_third          = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Permanent set 3rd cycle (%)")
    load_hundred_third      = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Load at 100% elongation 3rd cycle (N/50 mm)")
    lamination_str          = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Lamination strenght (CD) (N/25 mm)")

    class Meta:
        verbose_name_plural = "CTSups"
        
    def __str__(self):
        return '%s' % (self.pk)
    

class CTInf(models.Model):
    basis_weight            = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Basis weight (gsm)")
    tensile_peak            = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Tensile at peak CD (N/25mm)")
    elong_break_cd          = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Elongation at break CD (%)")
    elong_n_cd              = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Elongation at 9.81N CD (%)")
    load_five               = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Load at 5% elongation 1st cycle CD (N/50 mm)")
    load_ten                = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Load at 10% elongation 1st cycle CD (N/50 mm)")
    load_twenty             = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Load at 20% elongation 1st cycle CD (N/50 mm)")
    load_fifty              = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Load at 50% elongation 1st cycle CD (N/50 mm)")
    perm_set_second         = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Permanent set 2nd cycle (%)")
    load_hundred_second     = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Load at 100% elongation 2nd cycle (N/50 mm)")
    perm_set_third          = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Permanent set 3rd cycle (%)")
    load_hundred_third      = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Load at 100% elongation 3rd cycle (N/50 mm)")
    lamination_str          = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Lamination strenght (CD) (N/25 mm)")

    class Meta:
        verbose_name_plural = "CTInfs"

    def __str__(self):
        return '%s' % (self.pk)


class CaracteristicasTecnicas(models.Model):
    user                    = models.ForeignKey(User, on_delete=models.PROTECT,verbose_name="Username")
    timestamp               = models.DateTimeField(auto_now_add=True)
    ctsup                   = models.ForeignKey(CTSup, on_delete=models.PROTECT,verbose_name="Caracteristicas Técnicas Superior")
    ctinf                   = models.ForeignKey(CTInf, on_delete=models.PROTECT,verbose_name="Caracteristicas Técnicas Inferior")

    class Meta:
        verbose_name_plural = "Caracteristicas Técnicas"
    
    def __str__(self):
        return '%s' % (self.pk)   


class OrdemProducao(models.Model):
    TIPOEMENDA = (('Fita Preta', 'Fita Preta'), ('Fita metálica', 'Fita metálica'))
    TIPOTRANS = (('---', '---'), ('Camião', 'Camião'), ('Contentor', 'Contentor'))
    ENR = (('Anti-horário', 'Anti-horário'), ('Horário', 'Horário'))
    CORE = (('3"', '3"'), ('6"', '6"'))
    TIPONW = (('Suominen 25 gsm','Suominen 25 gsm'), ('Sandler SPUNLACE 100%PP','Sandler SPUNLACE 100%PP'), ('BCN 70%PP/30%PE','BCN 70%PP/30%PE'), ('Sandler','Sandler'), ('PEGAS BICO 17gsm','PEGAS BICO 17gsm'), ('Suominen','Suominen'), ('BCN','BCN'), ('ORMA','ORMA'), ('PEGAS 22','PEGAS 22'), ('SAWASOFT','SAWASOFT'), ('SAWABOND','SAWABOND'), ('Teksis','Teksis'), ('Union','Union'),('Radici','Radici'),('Fitesa','Fitesa'),('ALBIS 23','ALBIS 23'),('ALBIS 16','ALBIS 16'),('Union Pillow','Union Pillow'),('Union UV','Union UV'), ('Jacob Holm','Jacob Holm'), ('Nonwoven Nikoo 25gsm Spunlace 100PP', 'Nonwoven Nikoo 25gsm Spunlace 100PP'))
    EMBAL_T = (('Placa Plástico', 'Placa Plástico'), ('Placa Cartão Fino', 'Placa Cartão Fino'))
    EMBAL_E = (('Filme Estirável', 'Filme Estirável'),)
    user                    = models.ForeignKey(User, on_delete=models.PROTECT,verbose_name="Username")
    enc                     = models.ForeignKey(Encomenda, on_delete=models.PROTECT, verbose_name="Encomenda", null=True, blank=True) 
    artigo                  = models.ForeignKey(Artigo, on_delete=models.PROTECT, verbose_name="Artigo")
    cliente                 = models.ForeignKey(Cliente, on_delete=models.PROTECT, verbose_name="Cliente", null=True, blank=True)
    ct                      = models.ForeignKey(CaracteristicasTecnicas, on_delete=models.CASCADE, verbose_name="Caracteristicas Técnicas", null=True, blank=True)
    timestamp               = models.DateTimeField(auto_now_add=True)
    data_prevista_inicio    = models.DateField(auto_now_add=False, auto_now=False, default=datetime.date.today, verbose_name="Data Prevista de Início")
    data_prevista_fim       = models.DateField(auto_now_add=False, auto_now=False, default=datetime.date.today, verbose_name="Data Prevista de Fim")
    inicio                  = models.DateTimeField(auto_now_add=False, null=True, blank=True, verbose_name="Inico")
    op                      = models.CharField(max_length=200,verbose_name="Ordem de Produção")
    largura                 = models.DecimalField(max_digits=6, decimal_places=0, verbose_name="Largura")
    limsup                  = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Limite Superior", null=True, blank=True)
    liminf                  = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Limite Inferior", null=True, blank=True)
    core                    = models.CharField(max_length=2,choices=CORE, verbose_name="Core")
    num_paletes_produzidas  = models.IntegerField(default=0, verbose_name="Nº de paletes produzidas")
    num_paletes_produzir    = models.IntegerField(default=0, verbose_name="Nº de paletes a produzir")
    num_paletes_stock_in    = models.IntegerField(default=0, verbose_name="Nº de paletes de stock inseridas")
    num_paletes_stock       = models.IntegerField(default=0, verbose_name="Nº de paletes em stock")
    num_paletes_total       = models.IntegerField(default=0, verbose_name="Nº de paletes total")
    tipo_emenda             = models.CharField(max_length=200, choices=TIPOEMENDA, default="Fita Preta", verbose_name="Tipo de Emenda")
    emendas                 = models.CharField(max_length=200,verbose_name="Emendas")
    nwsup                   = models.CharField(max_length=200, choices=TIPONW, unique=False, verbose_name="Nonwoven Superior", null=True, blank=True)
    nwinf                   = models.CharField(max_length=200, choices=TIPONW, unique=False, verbose_name="Nonwoven Inferior", null=True, blank=True)
    tipo_paletes            = models.CharField(max_length=200, unique=False, verbose_name="Tipo de Paletes")
    palete_por_palete       = models.IntegerField(default=1, verbose_name="Palete por Palete")
    bobines_por_palete      = models.IntegerField(default=0, verbose_name="Bobines por Palete")
    enrolamento             = models.CharField(max_length=100, unique=False, verbose_name="Sentido do enrolamento", choices=ENR, default="Anti-horario")
    folha_id                = models.BooleanField(default=True, verbose_name="Folha de identificação de palete")
    freq_amos               = models.IntegerField(default=4, verbose_name="Frequência de amostragem por bobinagem")
    limite_desc             = models.DecimalField(max_digits=3, decimal_places=0, verbose_name="Limite Descentrado", null=True, blank=True)
    limite_con              = models.DecimalField(max_digits=3, decimal_places=0, verbose_name="Limite Cónico", null=True, blank=True)
    diam_min                = models.IntegerField(default=0, verbose_name="Diâmetro minimo")
    diam_max                = models.IntegerField(default=0, verbose_name="Diâmetro máximo")
    stock                   = models.BooleanField(default=False, verbose_name="Stock")   
    ficha_processo          = models.CharField(max_length=100, unique=False, verbose_name="Ficha de Processo", null=True, blank=True)
    coa_aprov               = models.CharField(max_length=100, unique=False, verbose_name="Coa de Aprovação", null=True, blank=True)
    tipo_transporte         = models.CharField(max_length=20, unique=False, choices= TIPOTRANS, default="---", verbose_name="Tipo de Transporte", null=True, blank=True)
    paletes_camiao          = models.IntegerField(default=0, verbose_name="Paletes por camião", null=True, blank=True)
    altura_max              = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Altura máxima")
    paletes_sobre           = models.BooleanField(default=False, verbose_name="Paletes Sobrepostas")
    cintas                  = models.BooleanField(default=False, verbose_name="Cintas")
    topo                    = models.CharField(max_length=50, choices=EMBAL_T, unique=False, verbose_name="Topo")
    base                    = models.CharField(max_length=50, choices=EMBAL_T, unique=False, verbose_name="Base")
    embal                   = models.CharField(max_length=50, choices=EMBAL_E, unique=False, verbose_name="Embalamento")
    etiqueta_bobine         = models.IntegerField(default=2, verbose_name="Etiqueta por bobine")
    etiqueta_palete         = models.IntegerField(default=4, verbose_name="Etiqueta por palete")
    etiqueta_final          = models.IntegerField(default=1, verbose_name="Etiqueta final por palete")
    ativa                   = models.BooleanField(default=False, verbose_name="Em progresso")
    completa                = models.BooleanField(default=False, verbose_name="Completa")
    retrabalho              = models.BooleanField(default=False, verbose_name="Ordem de retrabalho")

    class Meta:
        verbose_name_plural = "Ordens de Produção"
        
    def __str__(self):
        return '%s' % (self.op)

class PaletesARetrabalhar(models.Model):
    palete                  = models.ForeignKey(Palete, on_delete=models.PROTECT, verbose_name="Palete")
    ordem                   = models.ForeignKey(OrdemProducao, on_delete=models.PROTECT, verbose_name="Ordem de Produção")

    def __str__(self):
        return '%s - %s' % (self.palete.nome, self.ordem.op)

class BobinesARetrabalhar(models.Model):
    bobine                  = models.ForeignKey(Bobine, on_delete=models.PROTECT, verbose_name="Bobine")
    ordem                   = models.ForeignKey(OrdemProducao, on_delete=models.PROTECT, verbose_name="Ordem de Produção")
    retrabalhar             = models.BooleanField(default=True, verbose_name="Retrabalhar")

    def __str__(self):
        return '%s - %s - %s' % (self.bobine.nome, self.ordem.op, self.retrabalhar)

    