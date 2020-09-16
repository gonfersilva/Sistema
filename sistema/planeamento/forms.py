from producao.models import *
from .models import *
from django.forms import ModelForm, formset_factory, inlineformset_factory, modelformset_factory
from datetime import datetime
from django import forms
from django.core.exceptions import ValidationError
from django.db.models import Q


class OrdemProducaoCreateForm(ModelForm):
    basis_weight_inf            = forms.DecimalField(max_digits=5,decimal_places=2, required=True)
    tensile_peak_inf            = forms.DecimalField(max_digits=5,decimal_places=2, required=True)
    elong_break_cd_inf          = forms.DecimalField(max_digits=5,decimal_places=2, required=True)
    elong_n_cd_inf              = forms.DecimalField(max_digits=5,decimal_places=2, required=True)
    load_five_inf               = forms.DecimalField(max_digits=5,decimal_places=2, required=True)
    load_ten_inf                = forms.DecimalField(max_digits=5,decimal_places=2, required=True)
    load_twenty_inf             = forms.DecimalField(max_digits=5,decimal_places=2, required=True)
    load_fifty_inf              = forms.DecimalField(max_digits=5,decimal_places=2, required=True)
    perm_set_second_inf         = forms.DecimalField(max_digits=5,decimal_places=2, required=True)
    load_hundred_second_inf     = forms.DecimalField(max_digits=5,decimal_places=2, required=True)
    perm_set_third_inf          = forms.DecimalField(max_digits=5,decimal_places=2, required=True)
    load_hundred_third_inf      = forms.DecimalField(max_digits=5,decimal_places=2, required=True)
    lamination_str_inf          = forms.DecimalField(max_digits=5,decimal_places=2, required=True)
    basis_weight_sup            = forms.DecimalField(max_digits=5,decimal_places=2, required=True)
    tensile_peak_sup            = forms.DecimalField(max_digits=5,decimal_places=2, required=True)
    elong_break_cd_sup          = forms.DecimalField(max_digits=5,decimal_places=2, required=True)
    elong_n_cd_sup              = forms.DecimalField(max_digits=5,decimal_places=2, required=True)
    load_five_sup               = forms.DecimalField(max_digits=5,decimal_places=2, required=True)
    load_ten_sup                = forms.DecimalField(max_digits=5,decimal_places=2, required=True)
    load_twenty_sup             = forms.DecimalField(max_digits=5,decimal_places=2, required=True)
    load_fifty_sup              = forms.DecimalField(max_digits=5,decimal_places=2, required=True)
    perm_set_second_sup         = forms.DecimalField(max_digits=5,decimal_places=2, required=True)
    load_hundred_second_sup     = forms.DecimalField(max_digits=5,decimal_places=2, required=True)
    perm_set_third_sup          = forms.DecimalField(max_digits=5,decimal_places=2, required=True)
    load_hundred_third_sup      = forms.DecimalField(max_digits=5,decimal_places=2, required=True)
    lamination_str_sup          = forms.DecimalField(max_digits=5,decimal_places=2, required=True)
    emendas                     = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = OrdemProducao
        fields =['enc', 'artigo','data_prevista_inicio', 'data_prevista_fim', 'largura', 'core', 'num_paletes_produzir', 'num_paletes_stock', 'num_paletes_total', 'tipo_emenda','emendas', 'nwsup', 'nwinf', 'tipo_paletes', 'palete_por_palete',
         'bobines_por_palete', 'enrolamento', 'folha_id', 'freq_amos', 'limite_desc', 'limite_con', 'diam_min', 'diam_max', 'stock', 'ficha_processo', 'coa_aprov', 'tipo_transporte', 'paletes_camiao', 
         'altura_max', 'paletes_sobre', 'cintas', 'topo', 'base', 'embal', 'etiqueta_bobine', 'etiqueta_palete', 'etiqueta_final']

    def __init__(self, *args, **kwargs):
        # palete = Palete.objects.filter(estado='G', data_pal__year='2020').latest('num')
        # num_bobines = palete.num_bobines
        # largura_bobines = palete.largura_bobines
        # core_bobines = palete.core_bobines
        # num = palete.num
        # destino = palete.destino
        super(OrdemProducaoCreateForm, self).__init__(*args, **kwargs)  
        self.fields['enc'].queryset = Encomenda.objects.filter(estado='A')
        # self.fields['num_bobines'].initial = num_bobines
        # self.fields['largura_bobines'].initial = largura_bobines
        # self.fields['core_bobines'].initial = core_bobines
        # self.fields['num'].initial = num + 1
        # self.fields['destino'].initial = destino

class AddStockForm(ModelForm):
    class Meta:
        model = Palete
        fields = ['add']

class OrdemProducaoDMCreateForm(ModelForm):
    emendas                     = forms.CharField(widget=forms.Textarea)
    class Meta:
        model  = OrdemProducao
        fields = ['cliente', 'enc', 'artigo','data_prevista_inicio', 'data_prevista_fim', 'largura', 'core', 'num_paletes_produzir', 'tipo_emenda', 'emendas', 'tipo_paletes', 'palete_por_palete',
         'bobines_por_palete', 'enrolamento', 'diam_min', 'diam_max', 'stock', 'altura_max', 'paletes_sobre', 'cintas', 'topo', 'base', 'embal', 'etiqueta_bobine', 'etiqueta_palete', 'etiqueta_final']

    def __init__(self, *args, **kwargs):
       
        super(OrdemProducaoDMCreateForm, self).__init__(*args, **kwargs)  
        self.fields['enc'].queryset = Encomenda.objects.filter(estado='A')
        

