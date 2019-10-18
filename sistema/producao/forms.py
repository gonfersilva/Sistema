from .models import Perfil, Largura, Bobinagem, Bobine, Palete, Emenda, Cliente, Encomenda, Carga, EtiquetaRetrabalho
from django.forms import ModelForm, formset_factory, inlineformset_factory, modelformset_factory
import datetime, time
from django import forms
from django.core.exceptions import ValidationError
from django.db.models import Q


class PerfilCreateForm(ModelForm):
    
    class Meta:
       model = Perfil
       fields =['nome', 'produto', 'num_bobines', 'largura_bobinagem', 'core', 'retrabalho']
    #    fields =['nome', 'num_bobines', 'retrabalho', 'largura_bobinagem', 'core', 'gramagem', 'espessura', 'densidade_mp', 'velocidade', 'producao']


class LarguraForm(ModelForm):

    class Meta:
       model = Largura
       fields = [ 'largura', 'designacao_prod' ]


class BobinagemCreateForm(ModelForm):
    
    class Meta:
       model = Bobinagem
       fields = ['data', 'num_bobinagem', 'perfil', 'tiponwsup', 'tiponwinf', 'lotenwsup', 'lotenwinf', 'nwsup', 'nwinf', 'comp', 'comp_par', 'diam', 'inico', 'fim', 'estado', 'obs']

    def __init__(self, *args, **kwargs):
        bobinagem = Bobinagem.objects.filter(perfil__retrabalho=False)
        num = bobinagem.latest()
        num_b = num.num_bobinagem + 1
        fim = num.fim
        tiponwsup = num.tiponwsup
        tiponwinf = num.tiponwinf
        lotenwsup = num.lotenwsup
        lotenwinf = num.lotenwinf
        perfil = num.perfil
        diam = num.diam
        super(BobinagemCreateForm, self).__init__(*args, **kwargs)
        self.fields['perfil'].queryset = Perfil.objects.filter(Q(retrabalho=False) & Q(obsoleto=False))
        self.fields['num_bobinagem'].initial = num_b
        self.fields['inico'].initial = fim
        self.fields['tiponwsup'].initial = tiponwsup
        self.fields['tiponwinf'].initial = tiponwinf
        self.fields['lotenwsup'].initial = lotenwsup
        self.fields['lotenwinf'].initial = lotenwinf
        self.fields['perfil'].initial = perfil
        self.fields['diam'].initial = diam
    
        
         


class RetrabalhoCreateForm(ModelForm):
    
    class Meta:
        model = Bobinagem
        fields = ['data', 'num_bobinagem', 'perfil', 'inico']

    def __init__(self, *args, **kwargs):
        bobinagem = Bobinagem.objects.filter(perfil__retrabalho=True)
        num = bobinagem.latest()
        num_b = num.num_bobinagem + 1
        perfil = num.perfil
        fim = num.fim

        super(RetrabalhoCreateForm, self).__init__(*args, **kwargs)
        self.fields['perfil'].queryset = Perfil.objects.filter(Q(retrabalho=True) & Q(obsoleto=False))
        # self.fields['num_bobinagem'].widget.attrs['readonly'] = True
        # self.fields['data'].widget.attrs['readonly'] = True
        self.fields['num_bobinagem'].initial = num_b
        self.fields['perfil'].initial = perfil
        self.fields['inico'].widget.attrs['readonly'] = True
        self.fields['inico'].initial = fim
        
        



       
class PaleteCreateForm(ModelForm):
    
    class Meta:
       model = Palete
       fields = ['cliente', 'num', 'data_pal', 'num_bobines', 'largura_bobines', 'core_bobines', 'destino']

    def __init__(self, *args, **kwargs):
        palete = Palete.objects.filter(estado='G', data_pal__year='2019').latest('num')
        cliente = palete.cliente
        num_bobines = palete.num_bobines
        largura_bobines = palete.largura_bobines
        core_bobines = palete.core_bobines
        num = palete.num
        destino = palete.destino
        super(PaleteCreateForm, self).__init__(*args, **kwargs)      
        self.fields['cliente'].initial = cliente
        self.fields['num_bobines'].initial = num_bobines
        self.fields['largura_bobines'].initial = largura_bobines
        self.fields['core_bobines'].initial = core_bobines
        self.fields['num'].initial = num + 1
        self.fields['destino'].initial = destino

class ClienteCreateForm(ModelForm):
    
    class Meta:
       model = Cliente
       fields = ['cod', 'nome', 'abv', 'limsup', 'liminf', 'diam_ref']

    



class BobineStatus(ModelForm):
   
    class Meta:
        model = Bobine
        fields = [ 'largura', 'estado', 'con', 'descen', 'presa', 'diam_insuf', 'furos', 'esp', 'troca_nw', 'buraco', 'outros', 'obs'] 

# class BobinagemUpdate(ModelForm):
#      class Meta:
#         model = Bobinagem
#         fields = ['tiponwsup', 'tiponwinf', 'lotenwsup', 'lotenwinf', 'nwsup', 'nwinf', 'comp', 'comp_par', 'diam', 'inico', 'fim']

class EmendasCreateForm(ModelForm):
    #  bobine = forms.CharField(label='Bobine original')

     class Meta:
        model = Emenda
        fields = [ 'bobine', 'metros', 'num_emenda', 'emenda'] 

    #  def __init__(self, *args, **kwargs):
    #      super(EmendasCreateForm, self).__init__(*args, **kwargs)
    #      self.fields['bobine'].queryset = Bobine.objects.filter(estado='DM')

    

class Picagem(forms.Form):
    nome = forms.CharField(max_length=50)


    
class UpdateBobineForm(ModelForm):
    class Meta:
        model = Bobine
        fields = [ 'estado', 'con', 'descen', 'presa', 'diam_insuf', 'furos', 'esp', 'troca_nw', 'outros', 'buraco', 'obs', 'l_real', 'nok']


class PaleteRetrabalhoForm(ModelForm):

    class Meta:
        model = Palete
        fields = ['num', 'data_pal']

    def __init__(self, *args, **kwargs):
        palete = Palete.objects.filter(estado='DM').latest('num')
        num = palete.num
        super(PaleteRetrabalhoForm, self).__init__(*args, **kwargs)      
        
        self.fields['num'].initial = num + 1

    
class OrdenarBobines(ModelForm):

    class Meta:
        model = Bobine
        fields = ['posicao_palete']

class ClassificacaoBobines(ModelForm):

    class Meta:
        model = Bobine
        fields = ['estado', 'con', 'descen', 'presa', 'diam_insuf', 'furos', 'esp', 'troca_nw', 'outros', 'obs', 'buraco']

        
class RetrabalhoForm(ModelForm):

    bobine = forms.CharField(max_length=14)

    class Meta:
        model = Emenda
        fields = ['bobine', 'metros']

class EncomendaCreateForm(forms.ModelForm):
        
    class Meta:
        model = Encomenda
        fields = ['cliente', 'data', 'eef', 'prf', 'sqm', 'num_cargas']

    def __init__(self, *args, **kwargs):
        encomenda = Encomenda.objects.all().latest('id')
        prf = encomenda.prf
        eef = encomenda.eef
        cliente = encomenda.cliente
        num_cargas = encomenda.num_cargas
        sqm = encomenda.sqm
        
        super(EncomendaCreateForm, self).__init__(*args, **kwargs) 
           
        self.fields['eef'].initial = eef
        self.fields['prf'].initial = prf
        self.fields['cliente'].initial = cliente
        self.fields['num_cargas'].initial = num_cargas
        self.fields['sqm'].initial = sqm



class CargaCreateForm(forms.ModelForm):
    class Meta:
        model = Carga
        fields = ['enc', 'data', 'num_carga', 'num_paletes', 'tipo']
    
    def __init__(self, *args, **kwargs):
        carga = Carga.objects.all().latest('id')
        enc = carga.enc
        num_carga = carga.num_carga + 1
        num_paletes = carga.num_paletes
        tipo = carga.tipo
        super(CargaCreateForm, self).__init__(*args, **kwargs)     
        self.fields['enc'].queryset = Encomenda.objects.filter(estado='A')  
        self.fields['enc'].initial = enc
        self.fields['num_carga'].initial = num_carga
        self.fields['num_paletes'].initial = num_paletes
        self.fields['tipo'].initial = tipo
        

class SelecaoPaleteForm(forms.Form):
    palete = forms.CharField(max_length=10)
    
        
    
class PaletePesagemForm(ModelForm):
    class Meta:
        model = Palete
        fields = [ 'carga', 'stock', 'peso_bruto', 'peso_palete']

    def __init__(self, *args, **kwargs):
        super(PaletePesagemForm, self).__init__(*args, **kwargs)     
        self.fields['carga'].queryset = Carga.objects.filter(estado='I')  
    

class AddPalateStockForm(ModelForm):
    class Meta:
        model = Palete
        fields = [ 'carga' ]

    def __init__(self, *args, **kwargs):
        # carga = Carga.objects.filter(estado='I')
        super(AddPalateStockForm, self).__init__(*args, **kwargs)
        self.fields['carga'].queryset = Carga.objects.filter(estado='I')
        


class AcompanhamentoDiarioSearchForm(forms.Form):
    data_inicio = forms.DateField(input_formats='%Y-%m-%d')
    hora_inicio = forms.TimeField(input_formats='%H:%M')
    data_fim = forms.DateField(input_formats='%Y-%m-%d')
    hora_fim = forms.TimeField(input_formats='%H:%M')


class RetrabalhoFormEmendas(forms.Form):
    bobine_1 = forms.CharField(max_length=14, label='Bobine original 1', required=True)
    bobine_2 = forms.CharField(max_length=14, label='Bobine original 2', required=False)
    bobine_3 = forms.CharField(max_length=14, label='Bobine original 3', required=False)
    m_bobine_1 = forms.DecimalField(max_digits=6, decimal_places=2, label='Metros enrolados da bobine original 1', required=True)
    m_bobine_2 = forms.DecimalField(max_digits=6, decimal_places=2, label='Metros enrolados da bobine original 2', required=False)
    m_bobine_3 = forms.DecimalField(max_digits=6, decimal_places=2, label='Metros enrolados da bobine original 3', required=False)


class ConfirmReciclarForm(forms.Form):
    recycle_1 = forms.BooleanField(initial=False, label='', required=False)
    recycle_2 = forms.BooleanField(initial=False, label='', required=False)
    recycle_3 = forms.BooleanField(initial=False, label='', required=False)

class PicagemBobines(forms.Form):
    bobine = forms.CharField(label='', max_length=14)
    
class ClassificacaoBobines(forms.Form):
    STATUSP = (('G', 'G'), ('DM', 'DM12'), ('R', 'R'), ('BA', 'BA'),('LAB', 'LAB'), ('IND', 'IND'), ('HOLD', 'HOLD'))
    estado = forms.CharField(max_length=4, widget=forms.Select(choices=STATUSP))
    con = forms.BooleanField(initial=False, label='', required=False)
    descen = forms.BooleanField(initial=False, label='', required=False)
    presa = forms.BooleanField(initial=False, label='', required=False)
    diam_insuf = forms.BooleanField(initial=False, label='', required=False)
    furos = forms.BooleanField(initial=False, label='', required=False)
    buraco = forms.BooleanField(initial=False, label='', required=False)
    esp = forms.BooleanField(initial=False, label='', required=False)
    troca_nw = forms.BooleanField(initial=False, label='', required=False)
    outros = forms.BooleanField(initial=False, label='', required=False)
    obs = forms.CharField(max_length=200, label='', required=False)
    l_real = forms.IntegerField(required=False)

class ImprimirEtiquetaBobine(forms.Form):
    IMP = (('Bobinadora_CAB_A4_200', 'BOBINADORA'), ('DM12_CAB_A4_200', 'DM12'))
    impressora = forms.CharField(max_length=200, widget=forms.Select(choices=IMP), required=True)
    num_copias = forms.IntegerField(label="Nº de Cópias", required=True, initial=1, max_value=2, min_value=1)

class ImprimirEtiquetaPalete(forms.Form):
    IMP = (('Bobinadora_CAB_A4_200', 'BOBINADORA'), ('DM12_CAB_A4_200', 'DM12'))
    impressora = forms.CharField(max_length=200, widget=forms.Select(choices=IMP), required=True)
    num_copias = forms.IntegerField(label="Nº de Cópias", required=True, initial=4, max_value=4, min_value=1)
        



   