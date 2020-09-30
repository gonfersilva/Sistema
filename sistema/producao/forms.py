from .models import Perfil, Largura, Bobinagem, Bobine, Palete, Emenda, Cliente, Encomenda, Carga, EtiquetaRetrabalho,Nonwoven, ArtigoCliente, Fornecedor, Rececao, ArtigoNW, ProdutoGranulado, Reciclado,MovimentoMP
from django.forms import ModelForm, formset_factory, inlineformset_factory, modelformset_factory
from datetime import datetime
from planeamento.models import *
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
    ESTADO = (('G', 'G'), ('R', 'R'), ('BA', 'BA'), ('LAB', 'LAB'), ('IND', 'IND'), ('HOLD','HOLD'), ('SC','SC'))
    estado = forms.CharField(max_length=4, required=True, widget=forms.Select(choices=ESTADO))
    class Meta:
       model = Bobinagem
       fields = ['data', 'num_bobinagem', 'perfil', 'tiponwsup', 'tiponwinf', 'lotenwsup', 'lotenwinf', 'nwsup', 'nwinf', 'comp', 'comp_par', 'diam', 'inico', 'fim', 'estado', 'obs', 'tipo_desp']

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
        self.fields['estado'].initial = 'LAB'

class BobinagemCreateFormV2(ModelForm):
    nonwoven_sup = forms.CharField(max_length=20, label='Nonwoven Superior', required=True)
    nonwoven_inf = forms.CharField(max_length=20, label='Nonwoven Inferior', required=True)
    consumo_sup = forms.DecimalField(max_digits=6, decimal_places=2, label='Consumo Superior', required=True)
    consumo_inf = forms.DecimalField(max_digits=6, decimal_places=2, label='Consumo Inferior', required=True)
    
    class Meta:
       model = Bobinagem
       fields = ['data', 'num_bobinagem', 'perfil', 'comp', 'comp_par', 'diam', 'inico', 'fim', 'estado', 'obs']

    def __init__(self, *args, **kwargs):
        bobinagem = Bobinagem.objects.filter(perfil__retrabalho=False)
        num = bobinagem.latest()
        num_b = num.num_bobinagem + 1
        fim = num.fim
        perfil = num.perfil
        diam = num.diam
        super(BobinagemCreateFormV2, self).__init__(*args, **kwargs)
        self.fields['perfil'].queryset = Perfil.objects.filter(Q(retrabalho=False) & Q(obsoleto=False))
        self.fields['num_bobinagem'].initial = num_b
        self.fields['inico'].initial = fim
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
       fields = ['ordem', 'num', 'data_pal', 'num_bobines', 'largura_bobines', 'core_bobines']

    def __init__(self, *args, **kwargs):
        palete = Palete.objects.filter(estado='G', data_pal__year='2020').latest('num')
        num_bobines = palete.num_bobines
        largura_bobines = palete.largura_bobines
        core_bobines = palete.core_bobines
        num = palete.num
        # destino = palete.destino
        super(PaleteCreateForm, self).__init__(*args, **kwargs)  
        self.fields['ordem'].queryset = OrdemProducao.objects.filter(Q(ativa=True) & Q(completa=False))
        self.fields['num_bobines'].initial = num_bobines
        self.fields['largura_bobines'].initial = largura_bobines
        self.fields['core_bobines'].initial = core_bobines
        self.fields['num'].initial = num + 1
        # self.fields['destino'].initial = destino

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
        fields = ['num', 'data_pal', 'num_bobines']

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
        fields = ['cliente', 'data', 'data_prevista', 'eef', 'prf', 'sqm', 'num_paletes', 'order_num']
        ordering = ('cliente')

    def __init__(self, *args, **kwargs):
        encomenda = Encomenda.objects.all().latest('id')
        prf = encomenda.prf
        eef = encomenda.eef
        cliente = encomenda.cliente
        sqm = encomenda.sqm
        
        super(EncomendaCreateForm, self).__init__(*args, **kwargs) 
           
        self.fields['eef'].initial = eef
        self.fields['prf'].initial = prf
        self.fields['cliente'].initial = cliente
        self.fields['sqm'].initial = sqm
        self.fields['cliente'].queryset = Cliente.objects.order_by('nome')



class CargaCreateForm(forms.ModelForm):
    class Meta:
        model = Carga
        fields = ['enc', 'data', 'data_prevista', 'num_carga', 'num_paletes', 'tipo']
    
    def __init__(self, *args, **kwargs):
        carga = Carga.objects.all().latest('id')
        enc = carga.enc
        num_carga = carga.num_carga + 1
        num_paletes = carga.num_paletes
        tipo = carga.tipo
        super(CargaCreateForm, self).__init__(*args, **kwargs)     
        self.fields['enc'].queryset = Encomenda.objects.filter(estado='A').order_by('-eef')
        self.fields['enc'].initial = enc
        self.fields['num_carga'].initial = num_carga
        self.fields['num_paletes'].initial = num_paletes
        self.fields['tipo'].initial = tipo
        

class SelecaoPaleteForm(forms.Form):
    palete = forms.CharField(max_length=11)
    
        
    
class PaletePesagemForm(ModelForm):
    class Meta:
        model = Palete
        fields = [ 'stock', 'peso_bruto', 'peso_palete']
    

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
    bobine_1 = forms.CharField(max_length=15, label='Bobine original 1', required=True)
    bobine_2 = forms.CharField(max_length=15, label='Bobine original 2', required=False)
    bobine_3 = forms.CharField(max_length=15, label='Bobine original 3', required=False)
    m_bobine_1 = forms.DecimalField(max_digits=6, decimal_places=2, label='Metros enrolados da bobine original 1', required=True)
    m_bobine_2 = forms.DecimalField(max_digits=6, decimal_places=2, label='Metros enrolados da bobine original 2', required=False)
    m_bobine_3 = forms.DecimalField(max_digits=6, decimal_places=2, label='Metros enrolados da bobine original 3', required=False)


class ConfirmReciclarForm(forms.Form):
    recycle_1 = forms.BooleanField(initial=False, label='', required=False)
    recycle_2 = forms.BooleanField(initial=False, label='', required=False)
    recycle_3 = forms.BooleanField(initial=False, label='', required=False)

class PicagemBobines(forms.Form):
    bobine = forms.CharField(label='', max_length=15)
    
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
    obs = forms.CharField(max_length=500, label='', required=False)
    l_real = forms.IntegerField(required=False)

class ImprimirEtiquetaBobine(forms.Form):
    IMP = (('Bobinadora_CAB_A4_200', 'BOBINADORA'), ('DM12_CAB_A4_200', 'DM12'))
    impressora = forms.CharField(max_length=200, widget=forms.Select(choices=IMP), required=True)
    num_copias = forms.IntegerField(label="Nº de Cópias", required=True, initial=1, max_value=5, min_value=1)

class ImprimirEtiquetaPalete(forms.Form):
    IMP = (('Bobinadora_CAB_A4_200', 'BOBINADORA'), ('DM12_CAB_A4_200', 'DM12'))
    impressora = forms.CharField(max_length=200, widget=forms.Select(choices=IMP), required=True)
    num_copias = forms.IntegerField(label="Nº de Cópias", required=True, initial=4, max_value=4, min_value=1)

class ImprimirEtiquetaFinalPalete(forms.Form):
    num_copias = forms.IntegerField(label="Nº de Cópias", required=True, initial=1, max_value=4, min_value=1)

class PerfilLinhaForm(ModelForm):
    largura_bobines = forms.DecimalField(required=False)
       
    class Meta:
        model = Perfil
        fields = [ 'produto', 'num_bobines', 'core', 'gramagem']

class PerfilDMForm(ModelForm):
    CORE = ((None, '---------'), ('3', '3"'),('6', '6"'))
    largura_bobines = forms.DecimalField(required=False)
    core_original = forms.CharField(label="Core original", max_length=200, required=True, widget=forms.Select(choices=CORE))
    largura_original = forms.DecimalField(required=True)
    class Meta:
        model = Perfil
        fields = ['produto', 'num_bobines', 'core', 'gramagem']

class SearchPerfil(forms.Form):
    CORE = ((None, '---------'), ('3', '3"'),('6', '6"'))
    PRODUTO = ((None, '---------'), ('NONWOVEN ELASTIC BANDS ELA-ACE 100 HE', 'NONWOVEN ELASTIC BANDS ELA-ACE 100 HE'), ('NONWOVEN ELASTIC BANDS ELA-ACE 100 HT', 'NONWOVEN ELASTIC BANDS ELA-ACE 100 HT'), ('NONWOVEN ELASTIC BANDS ELA-ACE 95 HE', 'NONWOVEN ELASTIC BANDS ELA-ACE 95 HE'), ('NONWOVEN ELASTIC BANDS ELA-SPUN 90 HE HL', 'NONWOVEN ELASTIC BANDS ELA-SPUN 90 HE HL'), ('NONWOVEN ELASTIC BANDS ELA-SPUN 95 HE HL', 'NONWOVEN ELASTIC BANDS ELA-SPUN 95 HE HL'), ('NONWOVEN ELASTIC BANDS ELA-SPUN 90 HT HL', 'NONWOVEN ELASTIC BANDS ELA-SPUN 90 HT HL'), ('NONWOVEN ELASTIC BANDS ELA-SPUN 95 HE HL', 'NONWOVEN ELASTIC BANDS ELA-SPUN 95 HE HL'), ('NONWOVEN ELASTIC BANDS ELA-SPUN 100 HE HL', 'NONWOVEN ELASTIC BANDS ELA-SPUN 100 HE HL'), ('SIDE PANEL ELA-ACE 100 HE', 'SIDE PANEL ELA-ACE 100 HE'),('NONWOVEN ELASTIC BANDS ELA-SPUN 100 HE BICO', 'NONWOVEN ELASTIC BANDS ELA-SPUN 100 HE BICO'),('NONWOVEN ELASTIC BANDS ELA-ACE 105 HE', 'NONWOVEN ELASTIC BANDS ELA-ACE 105 HE'), ('NONWOVEN ELASTIC BANDS ELA-ACE 100 HE(D)', 'NONWOVEN ELASTIC BANDS ELA-ACE 100 HE(D)'), ('FRONTAL TAPE 48', 'FRONTAL TAPE 48'), ('CAR PROTECTION SHEET 57', 'CAR PROTECTION SHEET 57'), ('ELASTIC FILM', 'ELASTIC FILM'))
    nome = forms.CharField(label="Produto" ,max_length=200, required=False, widget=forms.Select(choices=PRODUTO))
    num_bobines = forms.IntegerField(label="Nº de bobines", required=False)
    core = forms.CharField(label="Core", max_length=200, required=False, widget=forms.Select(choices=CORE))
    largura_bobinagem = forms.DecimalField(label="Largura da Bobinagem", required=False)
    retrabalho = forms.BooleanField(required=False)

class SearchBobinagem(forms.Form):
    nome = forms.CharField(label="Bobinagem",max_length=200, required=True)





class InventarioBobineDMInsert(forms.Form):
    bobine = forms.CharField(max_length=15, required=True)

class InventarioPaleteClienteInsert(forms.Form):
    palete = forms.CharField(max_length=20, required=True)

class ArtigoClientInsert(ModelForm):
    class Meta:
        model = ArtigoCliente
        fields = ['artigo', 'cod_client']

class FornecedorCreateForm(ModelForm):
    class Meta:
        model = Fornecedor
        fields = ['cod', 'abv', 'designacao']

class FornecedorEditForm(ModelForm):
    class Meta:
        model = Fornecedor
        fields = ['abv', 'designacao']

class RececaoCreateForm(ModelForm):
    class Meta:
        model = Rececao
        fields = ['fornecedor', 'encomenda']

class ArtigoNWCreateForm(ModelForm):
    class Meta:
        model = ArtigoNW
        fields = ['cod', 'designacao', 'fornecedor', 'largura', 'gsm']


class RececaoInsertNW(forms.Form):
    artigo_nw = forms.CharField(max_length=20, required=True, widget=forms.TextInput(attrs={'autofocus': True, 'value': ''}))
    sqm = forms.CharField(max_length=20, required=True)
    lote = forms.CharField(max_length=20, required=True)
    prod = forms.CharField(max_length=20, required=True)
    stack_num = forms.CharField(max_length=20, required=True)


class ClasssificacaoBobineDm(forms.Form):
    nok = forms.BooleanField(required=False)
    con = forms.BooleanField(required=False)
    descen = forms.BooleanField(required=False)
    presa = forms.BooleanField(required=False)
    diam_insuf = forms.BooleanField(required=False)
    suj = forms.BooleanField(required=False)
    car = forms.BooleanField(required=False)
    lac = forms.BooleanField(required=False)
    ncore = forms.BooleanField(required=False)
    sbrt = forms.BooleanField(required=False)
    fc = forms.BooleanField(required=False)
    ff = forms.BooleanField(required=False)
    fmp = forms.BooleanField(required=False)
    furos = forms.BooleanField(required=False)
    buraco = forms.BooleanField(required=False)
    esp = forms.BooleanField(required=False)
    prop = forms.BooleanField(required=False)
    outros = forms.BooleanField(required=False)
    troca_nw = forms.BooleanField(required=False)
    prop_obs = forms.CharField(max_length=500, required=False, widget=forms.Textarea)
    obs = forms.CharField(max_length=500, required=False, widget=forms.Textarea)
    fc_diam_ini = forms.DecimalField(required=False)
    fc_diam_fim = forms.DecimalField(required=False)
    ff_m_ini = forms.DecimalField(required=False)
    ff_m_fim = forms.DecimalField(required=False)

class ProdutoGranuladoCreateForm(ModelForm):
    class Meta:
        model = ProdutoGranulado
        fields = ['produto_granulado']

class RecicladoCreateForm(ModelForm):
    ESTADO = (('G', 'G'),('R', 'R'))
    TARA = (('15 kg', '15 kg'),('30 kg', '30 kg'))
    estado = forms.CharField(max_length=1, required=True, widget=forms.Select(choices=ESTADO))
    tara = forms.CharField(max_length=5, required=True, widget=forms.Select(choices=TARA))

    class Meta:
        model = Reciclado
        fields = ['produto_granulado', 'num', 'peso', 'tara', 'obs']

    def __init__(self, *args, **kwargs):
        reciclado = Reciclado.objects.all()
        data = datetime.now().date()
        try:
            reciclado = reciclado.latest('timestamp')
            data_reciclado = reciclado.timestamp.date()
            if data == data_reciclado:
                num = reciclado.num + 1
            elif data > data_reciclado:
                num = 1

        except:
            num = 1
  
        super(RecicladoCreateForm, self).__init__(*args, **kwargs)     
        
        self.fields['num'].initial = num

class RecicladoEditForm(ModelForm):
    ESTADO = (('G', 'G'),('R', 'R'))
    estado = forms.CharField(max_length=1, required=True, widget=forms.Select(choices=ESTADO))
    class Meta:
        model = Reciclado
        fields = ['produto_granulado', 'estado', 'peso', 'obs']

class ImprimirEtiquetaReciclado(forms.Form):
    num_copias = forms.IntegerField(label="Nº de Cópias", required=True, initial=4, max_value=4, min_value=1)

class MovimentoCreateForm(ModelForm):
  
    class Meta:
        model = MovimentoMP
        fields = ['lote', 'tipo', 'motivo']
    
class ExportBobinesToExcel(forms.Form):
    abv = forms.CharField(max_length=3, required=False)
    data_inicial = forms.DateField(required=False)
    data_final = forms.DateField(required=False)

class BobinagemEditForm(ModelForm):
    class Meta:
        model = Bobinagem
        fields = ['inico', 'fim', 'diam', 'comp', 'comp_par', 'tiponwsup', 'tiponwinf', 'lotenwsup', 'lotenwinf', 'nwsup', 'nwinf', 'obs', 'tipo_desp']

class BobinagemEditHasPaleteForm(ModelForm):
    class Meta:
        model = Bobinagem
        fields = ['inico', 'fim', 'tiponwsup', 'tiponwinf', 'lotenwsup', 'lotenwinf', 'nwsup', 'nwinf', 'obs']

class BobineEditForm(ModelForm):
    CLIENTE = (
        ('Novatis','Novatis'),('El Ghazou','El Ghazou'), ('CEPRO','CEPRO'),('SAH','SAH'),
        ('PAKTEN SAGLIK URUNLERI','PAKTEN SAGLIK URUNLERI'),('BB DISTRIBE SAS','BB DISTRIBE SAS'),
        ('Fine Hygienic Paper Co.','Fine Hygienic Paper Co.'),('Ali Bardi Paper Mill Co.','Ali Bardi Paper Mill Co.'),('Hygienic Paper Company Ltd','Hygienic Paper Company Ltd'),
        ('ONTEX','ONTEX'),('ABENA','ABENA'),('NORSUDEX','NORSUDEX'),('HALK HYGIENE','HALK HYGIENE'),('MEDIANE','MEDIANE'),('PAUL HARTMANN AG','PAUL HARTMANN AG'),
        ('PANAI S.A.L.','PANAI S.A.L.'),('NUNEX','NUNEX'),('Sanita S.A.L.','Sanita S.A.L.'),('PARMON','PARMON'),('ARKAN','ARKAN'),('MEGA DISPOSABLES S.A.','MEGA DISPOSABLES S.A.'),('National Pride','National Pride'),
        ('Drylock Technologies SL','Drylock Technologies SL'),('Cleopatra Tissue Products (PTY) Ltd','Cleopatra Tissue Products (PTY) Ltd'),('Celluloses de Brocéliande','Celluloses de Brocéliande'),
        ('Pozzani Disposables S.p.A.','Pozzani Disposables S.p.A.'),('SANCELLA TUNISIE','SANCELLA TUNISIE'),('Faderco SPA','Faderco SPA'),('MADAR GROUP','MADAR GROUP'),
        ('Sté SOFAS S.A.R.L.','Sté SOFAS S.A.R.L.'),('PREMIUM HYGIENE','PREMIUM HYGIENE'),('DIATEC S.r.l','DIATEC S.r.l'),
        ('ENKA HIJYEN','ENKA HIJYEN'),('Ontex Tuketim Urunleri San.ve TIC.A','Ontex Tuketim Urunleri San.ve TIC.A'),('FAS SOCIETA´ PER AZIONI','FAS SOCIETA´ PER AZIONI'),('NAPCO RIYADH PAPER PRODUCTS CO.','NAPCO RIYADH PAPER PRODUCTS CO.'),
        ('Activ Medical Disposable','Activ Medical Disposable'),('Drylock Technologies Ltd','Drylock Technologies Ltd'),('Drylock Technologies sro','Drylock Technologies sro'),
        ('NANO','NANO'),('ClotheUp','ClotheUp'),('Obviperiplo, Lda','Obviperiplo, Lda'),('Hospital Doutor Francisco Zagalo','Hospital Doutor Francisco Zagalo'),
        ('MACONFIL, Unipessoal, Lda','MACONFIL, Unipessoal, Lda'),('NORTE EM AÇÃO (SAOM - Serviços de Assistência)','NORTE EM AÇÃO (SAOM - Serviços de Assistência)'),
        ('Hospital Garcia de Orta','Hospital Garcia de Orta'),('Napco Consumer Products Co.','Napco Consumer Products Co.'),('National Paper Company Ltd.','National Paper Company Ltd.'),
        ('SANITA CONSUMER PRODUCTS S.A.E.','SANITA CONSUMER PRODUCTS S.A.E.'))
    cliente = forms.CharField(max_length=100, required=True, widget=forms.Select(choices=CLIENTE))
    
    class Meta:
        model = Bobine
        fields = ['cliente', 'artigo', 'designacao_prod', 'comp', 'diam']


class BobinagemFinalizarForm(ModelForm):

    class Meta:
        model = Bobinagem
        fields = ['fim', 'diam']

      

    

    










    




   