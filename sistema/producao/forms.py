from .models import Perfil, Largura, Bobinagem, Bobine, Palete, Emenda, Cliente
from django.forms import ModelForm, formset_factory, inlineformset_factory, modelformset_factory
import datetime, time
from django import forms

class PerfilCreateForm(ModelForm):
    
    class Meta:
       model = Perfil
       fields =['nome', 'produto', 'num_bobines', 'largura_bobinagem', 'core', 'retrabalho']
    #    fields =['nome', 'num_bobines', 'retrabalho', 'largura_bobinagem', 'core', 'gramagem', 'espessura', 'densidade_mp', 'velocidade', 'producao']


class LarguraForm(ModelForm):

    class Meta:
       model = Largura
       fields =[ 'largura' ]


class BobinagemCreateForm(ModelForm):
    
    class Meta:
       model = Bobinagem
       fields = ['data', 'num_bobinagem', 'perfil', 'tiponwsup', 'tiponwinf', 'lotenwsup', 'lotenwinf', 'nwsup', 'nwinf', 'comp', 'comp_par', 'diam', 'inico', 'fim', 'estado', 'obs']

    def __init__(self, *args, **kwargs):
         num = Bobinagem.objects.latest()
         num_b = num.num_bobinagem + 1
         fim = num.fim
         tiponwsup = num.tiponwsup
         tiponwinf = num.tiponwinf
         lotenwsup = num.lotenwsup
         lotenwinf = num.lotenwinf
         perfil = num.perfil
         diam = num.diam
         super(BobinagemCreateForm, self).__init__(*args, **kwargs)
         self.fields['perfil'].queryset = Perfil.objects.filter(retrabalho=False)
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
        
        # bobinagem_all = Bobinagem.objects.all()
        # for b in bobinagem_all:
        #     if b.perfil.retrabalho == True:
        #         bobinagem = b

        # num_l = bobinagem.num_bobinagem + 1
        # perfil_l = bobinagem.perfil


        super(RetrabalhoCreateForm, self).__init__(*args, **kwargs)
        self.fields['perfil'].queryset = Perfil.objects.filter(retrabalho=True)
        # self.fields['num_bobinagem'].initial = num_l
        # self.fields['perfil'].initial = perfil_l



       
class PaleteCreateForm(ModelForm):
    
    class Meta:
       model = Palete
       fields = ['cliente', 'data_pal', 'num_bobines', 'largura_bobines', 'core_bobines']

    def __init__(self, *args, **kwargs):
        palete = Palete.objects.filter(estado='G').latest('num')
        cliente = palete.cliente
        num_bobines = palete.num_bobines
        largura_bobines = palete.largura_bobines
        core_bobines = palete.core_bobines
        super(PaleteCreateForm, self).__init__(*args, **kwargs)      
        self.fields['cliente'].initial = cliente
        self.fields['num_bobines'].initial = num_bobines
        self.fields['largura_bobines'].initial = largura_bobines
        self.fields['core_bobines'].initial = core_bobines
         

class ClienteCreateForm(ModelForm):
    
    class Meta:
       model = Cliente
       fields = ['cod', 'nome', 'limsup', 'liminf']

    



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
        fields = [ 'estado', 'con', 'descen', 'presa', 'diam_insuf', 'furos', 'esp', 'troca_nw', 'outros', 'buraco', 'obs']


class PaleteRetrabalhoForm(ModelForm):

    class Meta:
        model = Palete
        fields = ['data_pal', 'num_bobines', 'largura_bobines', 'core_bobines']

    def __init__(self, *args, **kwargs):
        palete = Palete.objects.filter(estado='DM').latest('num')
        num_bobines = palete.num_bobines
        largura_bobines = palete.largura_bobines
        core_bobines = palete.core_bobines
        super(PaleteRetrabalhoForm, self).__init__(*args, **kwargs)      
        self.fields['num_bobines'].initial = num_bobines
        self.fields['largura_bobines'].initial = largura_bobines
        self.fields['core_bobines'].initial = core_bobines

    
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
        