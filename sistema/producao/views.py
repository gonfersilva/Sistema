from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy, resolve
from django.forms.models import modelformset_factory, inlineformset_factory
from django import forms
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, redirect, reverse, HttpResponse
from django.views.generic import CreateView
from django.views.generic import ListView, DetailView, CreateView, TemplateView, View, FormView, UpdateView
from .forms import PicagemBobines, PerfilCreateForm, ClassificacaoBobines, LarguraForm, BobinagemCreateForm, BobineStatus, AcompanhamentoDiarioSearchForm, ConfirmReciclarForm, RetrabalhoFormEmendas, PaleteCreateForm, SelecaoPaleteForm, AddPalateStockForm, PaletePesagemForm, RetrabalhoCreateForm, CargaCreateForm, EmendasCreateForm, ClienteCreateForm, UpdateBobineForm, PaleteRetrabalhoForm, OrdenarBobines, ClassificacaoBobines, RetrabalhoForm, EncomendaCreateForm
from .models import Largura, Perfil, Bobinagem, Bobine, Palete, Emenda, Cliente, EtiquetaRetrabalho, Encomenda
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, Http404, HttpResponse
from django.db.models.signals import pre_save, post_save
from django.contrib import messages
from time import gmtime, strftime
import datetime
import time
from .funcs import *
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q
from django.forms import formset_factory



# class CreatePerfil(LoginRequiredMixin, CreateView):
#     template_name = 'perfil/perfil_create.html'
#     form_class = PerfilCreateForm
#     success_url = '/producao/perfil/{id}/'
     
#     def form_valid(self, form):
#         form.instance.user = self.request.user
#         return super().form_valid(form)

@login_required
def create_perfil(request):
    
    template_name = 'perfil/perfil_create.html'
    form = PerfilCreateForm(request.POST or None)
           
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        
        for i in range(instance.num_bobines):
            lar = Largura.objects.create(perfil=instance, num_bobine=i+1, designacao_prod=instance.produto)
            lar.save()
        
        return redirect('producao:perfil_details', pk=instance.pk)

    context = {
        "form": form
    }

    return render(request, template_name, context)


@login_required
def create_bobinagem(request):
    
    template_name = 'producao/bobinagem_create.html'
    form = BobinagemCreateForm(request.POST or None)
    
    # form = BobinagemCreateForm(initial=num)
    
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        bobinagem_create(instance.pk)
        
        
        if not instance.estado == 'LAB' or instance.estado == 'HOLD':
            areas(instance.pk)
        
        return redirect('producao:etiqueta_retrabalho', pk=instance.pk)

    context = {
        "form": form
    }

    return render(request, template_name, context)



def perfil_list(request):
    perfil = Perfil.objects.all()
    # paginator = Paginator(perfil, 15)
    # page = request.GET.get('page')
    template_name = 'perfil/perfil_home.html'
    
    # try:
    #     perfil = paginator.page(page)
    # except PageNotAnInteger:
    #     perfil = paginator.page(1)
    # except EmptyPage:
    #     perfil = paginator.page(paginator.num_pages)

    context = {
        "perfil": perfil,
    }
    return render (request, template_name, context)


@login_required
def perfil_detail(request, pk):
    perfil = Perfil.objects.get(pk=pk)
    largura = Largura.objects.filter(perfil=pk)
    template_name = 'perfil/perfil_detail.html'
    context = {
        'perfil': perfil,
        'largura': largura,
    }
    return render(request, template_name, context)


   
# class BobinagemListView(LoginRequiredMixin, ListView):
#     model = Bobinagem
#     template_name = 'producao/bobinagem_home.html'
    
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['now'] = timezone.now()
#         return context

def bobinagem_list(request):
    now = datetime.datetime.now()
    bobinagem = Bobinagem.objects.all()
        
    template_name = 'producao/bobinagem_home.html'
    bobine = Bobine.objects.all()
  

    

    context = {
        "bobinagem": bobinagem,
        "bobine": bobine,
        "now": now
        
    }
    return render (request, template_name, context)

def bobinagem_historico(request):
    bobinagem = Bobinagem.objects.all()
    s = request.GET.get("s")
    if s:
        bobinagem = Bobinagem.objects.filter(Q(nome__icontains=s) | Q(data__icontains=s))
        

    paginator = Paginator(bobinagem, 17)
    page = request.GET.get('page')
    template_name = 'producao/bobinagem_all.html'
    bobine = Bobine.objects.all()
  

    try:
        bobinagem = paginator.page(page)
    except PageNotAnInteger:
        bobinagem = paginator.page(1)
    except EmptyPage:
        bobinagem = paginator.page(paginator.num_pages)

    context = {
        "bobinagem": bobinagem,
        "bobine": bobine,
        
        
    }
    return render (request, template_name, context)



@login_required
def bobinagem_status(request, pk):
    template_name = 'producao/bobine_list.html'
    bobinagem = Bobinagem.objects.get(pk=pk)
    bobine = Bobine.objects.filter(bobinagem=pk)
    emenda = Emenda.objects.filter(bobinagem=pk)

    context = {
        "bobinagem": bobinagem,
        "bobine": bobine,
        "emenda":emenda
    }

    return render(request, template_name, context) 

class LarguraUpdate(LoginRequiredMixin, UpdateView):
    model = Largura
    fields = ['largura', 'designacao_prod', 'gsm']
    template_name = 'perfil/largura_update.html'

def update_bobine(request, pk=None):

    instance = get_object_or_404(Bobine, pk=pk)
    template_name = 'producao/bobine_update.html'
    estado_anterior = instance.estado
    form = UpdateBobineForm(request.POST or None, instance=instance)
    context = {
        "form": form,
        "instance": instance,
        "title": instance.nome
    }
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        update_areas_bobine(instance.pk, estado_anterior)
        return redirect('producao:bobinestatus', pk=instance.bobinagem.pk)
   

    return render(request, template_name, context)

class BobinagemUpdate(LoginRequiredMixin, UpdateView):
    model = Bobinagem
    fields = ['tiponwsup', 'tiponwinf', 'lotenwsup', 'lotenwinf', 'nwsup', 'nwinf', 'comp', 'comp_par', 'diam', 'inico', 'fim']
    template_name = 'producao/bobinagem_update.html'
    
    
# class PaleteListView(LoginRequiredMixin, ListView):
#     model = Palete
#     template_name = 'palete/palete_home.html'
    
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['now'] = timezone.now()
#         return context

@login_required
def pelete_list(request):
    palete = Palete.objects.all()
    e_p = EtiquetaPalete.objects.all()
    # paginator = Paginator(palete, 15)
    # page = request.GET.get('page')
    template_name = 'palete/palete_home.html'
    
    # try:
    #     palete = paginator.page(page)
    # except PageNotAnInteger:
    #     palete = paginator.page(1)
    # except EmptyPage:
    #     palete = paginator.page(paginator.num_pages)

    context = {
        "palete": palete,
        "e_p": e_p
    }
    return render (request, template_name, context)


# class PaleteCreateView(LoginRequiredMixin, CreateView):
#     form_class = PaleteCreateForm
#     template_name = "palete/palete_create.html"
#     success_url = "/producao/palete/{id}"

#     def form_valid(self, form):
#         form.instance.user = self.request.user
#         return super().form_valid(form)

def create_palete(request):
    form = PaleteCreateForm(request.POST or None)
    template_name = "palete/palete_create.html"
    
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.estado = 'G'
        instance.area = 0
        instance.comp_total = 0
        instance.save()
        palete_nome(instance.pk)
                
        return redirect('producao:palete_picagem', pk=instance.pk)

    context = {
        "form": form
    }

    return render(request, template_name, context)



def ordenar_bobines_op(request, pk, operation):
    bobine = Bobine.objects.get(pk=pk)
    palete = Palete.objects.get(pk=bobine.palete.pk)
    pos = bobine.posicao_palete
    # pos_up = 0
    # pos_down = 0
    # bobine_up = 0
    # bobine_down = 0

    if Bobine.objects.filter(posicao_palete=pos-1, palete=palete).exists():
        bobine_up = Bobine.objects.get(posicao_palete=pos-1, palete=palete)
        pos_up = bobine_up.posicao_palete
    
    if Bobine.objects.filter(posicao_palete=pos+1, palete=palete).exists():
        bobine_down = Bobine.objects.get(posicao_palete=pos+1, palete=palete)
        pos_down = bobine_down.posicao_palete
   
    
    if operation == 'up':
        bobine.posicao_palete = pos - 1
        bobine_up.posicao_palete =  pos_up + 1
        bobine.save()
        bobine_up.save()
    elif operation == 'down':
        bobine.posicao_palete = pos + 1
        bobine_down.posicao_palete = pos_down - 1
        bobine.save()
        bobine_down.save()
        

    return redirect('producao:addbobinepalete', pk=palete.pk)
    
    

def create_palete_retrabalho(request):
    
    form = PaleteRetrabalhoForm(request.POST or None)
    template_name = "retrabalho/palete_retrabalho_create.html"

    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.retrabalhada = True
        instance.estado = 'DM'
        instance.num_bobines = 0
        instance.num_bobines_act = 0
        instance.largura_bobines = 0
        instance.area = 0
        instance.comp_total = 0        
        instance.save()
        palete_nome(instance.pk)
        

        if EtiquetaPalete.objects.filter(palete=instance).exists():
            return redirect('producao:picagem_palete_dm', pk=instance.pk)
        else:
            e_p = EtiquetaPalete.objects.create(palete=instance, palete_nome=instance.nome, largura_bobine=instance.largura_bobines)
            e_p.save()
            return redirect('producao:picagem_palete_dm', pk=instance.pk)
                
        return redirect('producao:picagem_palete_dm', pk=instance.pk)

        
    context = {
        "form": form, 
        }
    return render(request, template_name, context)


@login_required
def add_bobine_palete(request, pk):
    template_name = 'palete/add_bobine_palete.html'
    palete = Palete.objects.get(pk=pk)
    bobinagem = Bobinagem.objects.filter(diam=palete.diametro)
    bobine = Bobine.objects.all().order_by('posicao_palete')
    bobines = Bobine.objects.filter(palete=palete)
         
    context = {"palete": palete, 
               "bobine": bobine,
               "bobinagem": bobinagem,
            
               
                }
    return render(request, template_name, context)


@login_required
def palete_change(request, operation, pk_bobine, pk_palete):
    
    palete = Palete.objects.get(pk=pk_palete)
    bobine = Bobine.objects.get(pk=pk_bobine)
    
    if operation == 'add':
        Bobine.add_bobine(palete.pk, bobine.pk)
    elif operation == 'remove':
        Bobine.remove_bobine(palete.pk, bobine.pk)
                 
    
    return redirect('producao:addbobinepalete', pk=palete.pk)



class RetrabalhoCreateView(LoginRequiredMixin, CreateView):
     form_class = RetrabalhoCreateForm
     template_name = 'retrabalho/retrabalho_create.html'
     success_url = "/producao/retrabalho/filter/{id}"
    
     def form_valid(self, form):
         form.instance.user = self.request.user
         return super().form_valid(form)

@login_required
def create_bobinagem_retrabalho(request):
    template_name = 'retrabalho/retrabalho_create.html'
    form = RetrabalhoCreateForm(request.POST or None)
        
    if form.is_valid():
        instance = form.save(commit=False)
        
        bobinagem_nome = bobinagem_retrabalho_nome(instance.data, instance.num_bobinagem)

        if Bobinagem.objects.filter(nome=bobinagem_nome[0]).exists() or Bobinagem.objects.filter(nome=bobinagem_nome[1]).exists():
            messages.error(request, 'A bobinagem que deseja criar já existe. por favor verifique o numero da bobinagem.')
        else:
            instance.user = request.user
            instance.nome = bobinagem_nome[0]
            instance.save()
            area_bobinagem(instance.pk) 
            create_bobine(instance.pk) 
            return redirect('producao:retrabalho_v2', pk=instance.pk)       
   
            
            
        

    context = {
        "form": form
    }

    return render(request, template_name, context)


@login_required
def picagem_retrabalho(request, pk):
    
    bobinagem = Bobinagem.objects.get(pk=pk)
    palete = Palete.objects.filter(estado="DM")
    bobine = Bobine.objects.all()
    emenda = Emenda.objects.filter(bobinagem=pk)

    q_largura = request.GET.get("l")
   
    if q_largura:
        palete = palete.filter(largura_bobines__gte=q_largura)
        
    template_name = 'retrabalho/retrabalho_inicio.html'
    context = {
        
        "palete": palete,
        "bobine": bobine,
        "bobinagem": bobinagem,
        "emenda": emenda
        
    }

    return render(request, template_name, context)

@login_required
def picagem_retrabalho_add(request, pk):
    
    bobinagem = Bobinagem.objects.get(pk=pk)
    
    q_bobine = request.POST.get('b')
    q_metros = int(request.POST.get('m'))
    # else:
    #     messages.error(request, 'Por favor introduza a bobine desejada e os metros a retrabalhar.')
    #     return redirect('producao:retrabalho_filter', pk=bobinagem.pk)
    

    try:
        bobine = Bobine.objects.get(nome=q_bobine)
    except:
        messages.error(request, 'A bobine selecionada não existe.')
        return redirect('producao:retrabalho_filter', pk=bobinagem.pk)

    
    if bobine:
        if bobine.estado != 'DM':
            messages.error(request, 'O estado da bobine selecionada não permite efectuar esta operação.')
        elif q_metros > bobine.comp_actual:
            messages.error(request, 'A bobine selecionada não tem comprimento suficiente para efectuar esta operação.')
        else:
            emenda = Emenda.objects.create(bobinagem=bobinagem, bobine=bobine, metros=q_metros)
            bobine.comp_actual -= emenda.metros
            bobine.save()
            emenda.num_emenda = bobinagem.num_emendas + 1
            emenda.save()
            emenda_num = emenda.num_emenda
            if emenda_num == 0:
                emenda.emenda = 0
                emenda.save()
            elif emenda_num > 0:
                if emenda_num == 1:
                    emenda.emenda = emenda.metros
                    emenda.save()
                elif emenda_num == 2:
                    emenda_ul_bob = Emenda.objects.get(bobinagem=bobinagem, num_emenda=1)
                    emenda.emenda = emenda_ul_bob.emenda + emenda.metros 
                    emenda.save()
                elif emenda_num == 3:
                    emenda_ul_bob = Emenda.objects.get(bobinagem=bobinagem, num_emenda=2)
                    emenda.emenda = emenda_ul_bob.emenda + emenda.metros 
                    emenda.save()
            
            bobinagem.num_emendas += 1 
            data = bobinagem.data
            data = data.strftime('%Y%m%d')
            map(int, data)
            if bobinagem.perfil.retrabalho == True and bobinagem.num_emendas > 1:
                if bobinagem.num_bobinagem < 10:
                    bobinagem.nome = '3%s-0%s' % (data[1:], bobinagem.num_bobinagem)
                    bobinagem_pk = bobinagem.pk
                    bobine_nome(bobinagem_pk)
                else:
                    bobinagem.nome = '3%s-%s' % (data[1:], bobinagem.num_bobinagem)
            elif bobinagem.perfil.retrabalho == True and bobinagem.num_emendas == 0:
                if bobinagem.num_bobinagem < 10:
                    bobinagem.nome = '4%s-0%s' % (data[1:], bobinagem.num_bobinagem)
                else:
                    bobinagem.nome = '4%s-%s' % (data[1:], bobinagem.num_bobinagem)
            
            bobinagem.comp = bobinagem.comp + q_metros
            bobinagem.save()

        return redirect('producao:retrabalho_filter', pk=bobinagem.pk)





class ClienteCreateView(LoginRequiredMixin, CreateView):
     form_class = ClienteCreateForm
     template_name = 'cliente/cliente_create.html'
     success_url = "/producao/clientes/"
    
 


@login_required
def picagem(request, pk):
    palete = Palete.objects.get(pk=pk)
    bob = request.POST.get('q')
    try:
        bobine = Bobine.objects.get(nome=bob)
    except:
        messages.error(request, 'A bobine selecionada não existe.')
        return redirect('producao:addbobinepalete', pk=palete.pk)
    if bobine:
        if bobine.palete:
            if bobine.palete == palete:
                messages.error(request, 'A bobine já faz parte desta palete.')
                # erro = 4
                # return redirect('producao:addbobinepaleteerro', pk=palete.pk, e=erro)
                return redirect('producao:addbobinepalete', pk=palete.pk)
            else:
                messages.error(request, 'A bobine já faz parte de outra palate.')
                # erro = 5
                # return redirect('producao:addbobinepaleteerro', pk=palete.pk, e=erro)
                return redirect('producao:addbobinepalete', pk=palete.pk)
        else:
            if (bobine.estado == 'G' or bobine.estado == 'LAB') and palete.estado != 'DM':
                if palete.num_bobines_act == palete.num_bobines:
                    messages.error(request, 'A palete já se encontra completa.')
                    #  erro = 3
                    #  return redirect('producao:addbobinepaleteerro', pk=palete.pk, e=erro)
                    return redirect('producao:addbobinepalete', pk=palete.pk)
                else:
                     if (bobine.bobinagem.diam == palete.diametro or palete.cliente.limsup >= bobine.bobinagem.diam >= palete.cliente.liminf) and bobine.bobinagem.perfil.core == palete.core_bobines and bobine.largura.largura == palete.largura_bobines:
                         Bobine.add_bobine(palete.pk, bobine.pk)
                        #  etiqueta_add_bobine(palete.pk, bobine.pk)
                         return redirect('producao:addbobinepalete', pk=palete.pk)
                     else:
                         messages.error(request, 'A bobine selecionada está fora de especificações.')
                        #  erro = 1
                        #  return redirect('producao:addbobinepaleteerro', pk=palete.pk, e=erro)
                         return redirect('producao:addbobinepalete', pk=palete.pk)
            elif (bobine.estado == 'DM' or bobine.estado == 'G' or bobine.estado == 'IND' or bobine.estado == 'HOLD') and palete.estado == 'DM':
                  Bobine.add_bobine(palete.pk, bobine.pk)
                #   etiqueta_add_bobine(palete.pk, bobine.pk)
                  return redirect('producao:addbobinepalete', pk=palete.pk) 
            else:
                messages.error(request, 'A bobine selecionada está fora de especificações.')
                return redirect('producao:addbobinepalete', pk=palete.pk)
            
    else:
        messages.error(request, 'A bobine selecionada não existe.')
        #  erro = 2
        #  return redirect('producao:addbobinepaleteerro', pk=palete.pk, e=erro)  
        return redirect('producao:addbobinepalete', pk=palete.pk)        
            

@login_required
def reabrir_palete(request, pk):
    palete = get_object_or_404(Palete, pk=pk)
    etiqueta = EtiquetaPalete.objects.get(palete=palete)

    etiqueta.produto = ""
    etiqueta.diam_max = 0
    etiqueta.diam_min = 0
    etiqueta.save()
    

    return redirect('producao:addbobinepalete', pk=palete.pk)

   
@login_required
def add_bobine_palete_erro(request, pk, e):
    template_name = 'palete/add_bobine_erro.html'
    palete = Palete.objects.get(pk=pk)
    
    erro = e
    
    context = {"palete":palete, "erro":erro}
    
    return render(request, template_name, context)

    
@login_required
def perfil_delete(request, pk):
    obj = get_object_or_404(Perfil, pk=pk)
    bobinagem = Bobinagem.objects.filter(perfil=pk)
    if request.method == "POST":
        obj.delete()
        return redirect('producao:perfil')
            
    context = {
        "object": obj,
    }
    return render(request, "perfil/perfil_delete.html", context)

@login_required
def bobinagem_delete(request, pk):
    obj = get_object_or_404(Bobinagem, pk=pk)
    bobine = Bobine.objects.filter(bobinagem=obj)
    template_name = "producao/bobinagem_delete.html"
    emenda = Emenda.objects.filter(bobinagem=obj)
    pal = False
    if request.method == "POST":
        for b in bobine:
            if b.palete != None:
                pal = True
                break
            else:
                pal = False 

        if pal == False:
            if obj.perfil.retrabalho == True:
                # emenda = Emenda.objects.filter(bobinagem=obj)
                for e in emenda:
                    bobine = Bobine.objects.get(pk=e.bobine.pk)
                    bobine.comp_actual += e.metros
                    if bobine.recycle == True:
                        bobine.recycle = False
                    bobine.save()
                    e.delete()
                obj.delete()
                if obj.perfil.retrabalho == False:
                    return redirect('producao:bobinagem_list_all')
                else:
                    return redirect('producao:retrabalho_home')
            else:
                obj.delete()
                if obj.perfil.retrabalho == False:
                    return redirect('producao:bobinagem_list_all')
                else:
                    return redirect('producao:retrabalho_home')

        else:
            messages.error(request, 'A bobinagem não pode ser apagada porque existem bobines atribuidas a paletes.') 

            
    context = {
        "object": obj,
        "bobine": bobine,
        "emenda": emenda
    }
    return render(request, template_name, context)


@login_required
def palete_delete(request, pk):
    obj = get_object_or_404(Palete, pk=pk)
    bobine = Bobine.objects.filter(palete=obj)
    e_p = EtiquetaPalete.objects.get(palete=obj)
    if request.method == "POST":
        obj.delete()
        e_p.delete()
        if obj.estado == 'G':
            return redirect('producao:palete_list_all')
        else:
            return redirect('producao:paletes_retrabalho')    
    context = {
        "object": obj,
        "bobine": bobine
    }
    return render(request, "palete/palete_delete.html", context)
    
@login_required
def status_bobinagem(request, operation, pk):
    bobinagem = Bobinagem.objects.get(pk=pk)
    if operation == 'ap':
        bobinagem.estado = 'G'
        bobinagem.save()
        num = 1
        for i in range(bobinagem.perfil.num_bobines):
            largura = Largura.objects.get(perfil=bobinagem.perfil, num_bobine=num)
            bobine = Bobine.objects.get(bobinagem=bobinagem, largura=largura)
            if bobine.estado == 'LAB' or bobine.estado == 'HOLD':
                bobine.estado = 'G'
                bobine.save()
            num += 1
        areas(pk)
    elif operation == 'rej':
        bobinagem.estado = 'R'
        bobinagem.save()
        num = 1
        for i in range(bobinagem.perfil.num_bobines):
            largura = Largura.objects.get(perfil=bobinagem.perfil, num_bobine=num)
            bobine = Bobine.objects.get(bobinagem=bobinagem, largura=largura)
            if bobine.estado == 'LAB' or bobine.estado == 'HOLD':
                bobine.estado = 'R'
                bobine.save()
            num += 1
        areas(pk)
    elif operation == 'dm':
        bobinagem.estado = 'DM'
        bobinagem.save()
        num = 1
        for i in range(bobinagem.perfil.num_bobines):
            largura = Largura.objects.get(perfil=bobinagem.perfil, num_bobine=num)
            bobine = Bobine.objects.get(bobinagem=bobinagem, largura=largura)
            if bobine.estado == 'LAB' or bobine.estado == 'HOLD':
                bobine.estado = 'DM'
                bobine.save()
            num += 1
        areas(pk)
    elif operation == 'hold':
        bobinagem.estado = 'hold'
        bobinagem.save()
        num = 1
        for i in range(bobinagem.perfil.num_bobines):
            largura = Largura.objects.get(perfil=bobinagem.perfil, num_bobine=num)
            bobine = Bobine.objects.get(bobinagem=bobinagem, largura=largura)
            if bobine.estado == 'LAB':
                bobine.estado = 'HOLD'
                bobine.save()
            num += 1
        areas(pk)

       
            
    return redirect('producao:bobinestatus', pk=bobinagem.pk)


@login_required
def palete_retrabalho(request):
    palete = Palete.objects.filter(estado='DM')
    template_name = 'palete/palete_retrabalho.html'
    
    context = {
        "palete": palete,
    }
    return render (request, template_name, context)


@login_required
def palete_create_retrabalho(request):
    palete = Palete.objects.create(estado="DM", num_bobines=0, largura_bobines=0, diametro=0, core_bobines='3', user=request.user)   
    palete.save()
    return redirect('producao:addbobinepalete', pk=palete.pk)

@login_required
def retrabalho_home(request):
    palete = Palete.objects.filter(estado='DM')
    bobine = Bobine.objects.all()
    bobinagem = Bobinagem.objects.all()
    template_name = 'retrabalho/retrabalho_home.html'
    
  
    context = {
        "palete": palete,
        "bobine": bobine,
        "bobinagem": bobinagem,
    }
    return render(request, template_name, context)

@login_required
def retrabalho_filter(request, pk):
    # palete = Palete.objects.filter(estado="DM")
    # bobine = Bobine.objects.all()
    bobinagem = Bobinagem.objects.get(pk=pk)
    # q_largura = request.GET.get("l")
    # if q_largura:
    #     palete = palete.filter(largura_bobines__gte=q_largura)
    # bobinagem = Bobinagem.objects.get(pk=pk)
    form = EmendasCreateForm
    
    if request.method == "POST":
        form = EmendasCreateForm(request.POST)
               
        if form.is_valid():
            bobine_ori = int(form['bobine'].value())
            comp_bobine_ori = int(form['metros'].value())
            bobine = Bobine.objects.get(pk=bobine_ori)
            if comp_bobine_ori > bobine.comp_actual:
                messages.error(request, 'A bobine selecionada não tem comprimento suficiente para efectuar esta operação.')
                # redirect('producao:retrabalho_filter', pk=bobinagem.pk)
            else:
                emenda = Emenda.objects.create(**form.cleaned_data, bobinagem=bobinagem)
                bobine.comp_actual = bobine.comp_actual - emenda.metros 
                bobine.save()
                emenda.num_emenda = bobinagem.num_emendas + 1
                emenda.save()
                emenda_num = emenda.num_emenda
                print(emenda_num)
                if emenda_num == 0:
                    emenda.emenda = 0
                    emenda.save()
                elif emenda_num > 0:
                    if emenda_num == 1:
                        emenda.emenda = emenda.metros
                        emenda.save()
                    elif emenda_num == 2:
                        emenda_ul_bob = Emenda.objects.get(bobinagem=bobinagem, num_emenda=1)
                        emenda.emenda = emenda_ul_bob.emenda + emenda.metros 
                        emenda.save()
                    elif emenda_num == 3:
                        emenda_ul_bob = Emenda.objects.get(bobinagem=bobinagem, num_emenda=2)
                        emenda.emenda = emenda_ul_bob.emenda + emenda.metros 
                        emenda.save()

                bobinagem.num_emendas += 1 
                data = bobinagem.data
                data = data.strftime('%Y%m%d')
                map(int, data)
                if bobinagem.perfil.retrabalho == True and bobinagem.num_emendas > 1:
                    if bobinagem.num_bobinagem < 10:
                        # instance.nome = '3%s-0%s' % (data, instance.num_bobinagem)
                        bobinagem.nome = '3%s-0%s' % (data[1:], bobinagem.num_bobinagem)
                        bobinagem_pk = bobinagem.pk
                        bobine_nome(bobinagem_pk)
                    else:
                        bobinagem.nome = '3%s-0%s' % (data[1:], bobinagem.num_bobinagem)
                elif bobinagem.perfil.retrabalho == True and bobinagem.num_emendas == 0:
                    if bobinagem.num_bobinagem < 10:
                        bobinagem.nome = '4%s-0%s' % (data[1:], bobinagem.num_bobinagem)
                    else:
                        bobinagem.nome = '4%s-%s' % (data[1:], bobinagem.num_bobinagem)
                


                comp_parcial = int(form['metros'].value())
                bobinagem.comp = bobinagem.comp + comp_parcial
                bobinagem.save()

        return redirect('producao:retrabalho_filter', pk=bobinagem.pk)
         

    palete = Palete.objects.filter(estado="DM")
    bobine = Bobine.objects.all()
    emenda = Emenda.objects.filter(bobinagem=pk)

    q_largura = request.GET.get("l")
    

    if q_largura:
        palete = palete.filter(largura_bobines__gte=q_largura)
        
    template_name = 'retrabalho/retrabalho_inicio.html'
    context = {
        
        "palete": palete,
        "bobine": bobine,
        "form": form,
        "bobinagem": bobinagem,
        "emenda": emenda
        
    }

    return render(request, template_name, context)



# Funções de apoio

def bobine_nome(pk):
    bobinagem = Bobinagem.objects.get(pk=pk)
    bobine = Bobine.objects.filter(bobinagem=bobinagem)
    for b in bobine:
        data = bobinagem.data
        data = data.strftime('%Y%m%d')
        map(int, data)
        if bobinagem.num_bobinagem < 10 and b.largura.num_bobine < 10:
            b.nome = '3%s-0%s-0%s' % (data[1:], bobinagem.num_bobinagem, b.largura.num_bobine)
            b.save()
        elif bobinagem.num_bobinagem >= 10 and b.largura.num_bobine < 10:
            b.nome = '3%s-%s-0%s' % (data[1:], bobinagem.num_bobinagem, b.largura.num_bobine)
            b.save()
        elif bobinagem.num_bobinagem > 10 and b.largura.num_bobine >= 10:
            b.nome = '3%s-%s-%s' % (data[1:], bobinagem.num_bobinagem, b.largura.num_bobine)
            b.save()

            

def comprimento_bobine_original(pk):
    pass

# def finalizar_retrabalho(request, pk):
#     bobinagem = get_object_or_404(Bobinagem, pk=pk)
#     form = BobinagemCreateForm(request.POST or None, instance=bobinagem)
#     if form.is_valid():
#         bobinagem = form.save(commit=False)
#         bobinagem.save()
#         return redirect('producao:retrabalho_home')

#     template_name = 'retrabalho/retrabalho_finalizar.html'
#     context = {
#         "bobinagem": bobinagem,
#         "form": form
#     }

#     return render(request, template_name, context)

class BobinagemRetrabalhoFinalizar(LoginRequiredMixin, UpdateView):
    model = Bobinagem
    fields = ['fim', 'diam']
    template_name = 'retrabalho/retrabalho_finalizar.html'
    success_url = '/producao/etiqueta/retrabalho/{id}/'

    def form_valid(self, form):
        # bobinagem = Bobinagem.objects.get(pk=self.kwargs['pk'])
        b = form.save(commit=False)

        fim = b.fim
        fim = fim.strftime('%H:%M')
        inico = b.inico
        inico = inico.strftime('%H:%M')
        (hf, mf) = fim.split(':')
        (hi, mi) = inico.split(':')
        if hf < hi: 
            result = (int(hf) * 3600 + int(mf) * 60) - (int(hi) * 3600 + int(mi) * 60) + 86400
        else:
            result = (int(hf) * 3600 + int(mf) * 60) - (int(hi) * 3600 + int(mi) * 60) 
        
        result_str = strftime("%H:%M", gmtime(result))
        b.duracao = result_str

        # b.comp_cli = b.comp
        # bobine = Bobine.objects.filter(bobinagem=b.pk)
        # for bob in bobine:
        #     largura = bob.largura.largura
        #     bob.comp_actual = b.comp_cli
        #     largura = b.perfil.largura_bobinagem / 1000
        #     bob.area = largura * b.comp_cli
        #     cont = 0
        #     cont += largura
        #     bob.save()

        # b.area = b.comp_cli * cont

        b.save()
            
        return super(BobinagemRetrabalhoFinalizar, self).form_valid(form)
   
def finalizar_retarbalho(request, pk):
    bobinagem = get_object_or_404(Bobinagem, pk=pk)
    form = BobinagemCreateForm(request.POST or None, instance=bobinagem)
    if form.is_valid():
        bobinagem = form.save(commit=False)
        bobinagem.save()
        # tempo_duracao(bobinagem.pk)
        return redirect('producao:etiqueta_retrabalho', pk=bobinagem.pk)

    template_name = 'retrabalho/retrabalho_finalizar.html'
    context = {
        "bobinagem": bobinagem,
        "form": form
    }

    return render(request, template_name, context)


@login_required
def emenda_delete(request, pk):
    emenda = get_object_or_404(Emenda, pk=pk)
    bobine = get_object_or_404(Bobine, pk=emenda.bobine.pk)
    bobinagem = get_object_or_404(Bobinagem, pk=emenda.bobinagem.pk)
    bob = Bobine.objects.filter(bobinagem=bobinagem)
    if request.method == "POST":
        bobinagem.num_emendas -= 1
        bobinagem.comp -= emenda.metros
        bobine.comp_actual += emenda.metros 
        data = bobinagem.data
        data = data.strftime('%Y%m%d')
        map(int, data)
        if bobinagem.perfil.retrabalho == True and bobinagem.num_emendas > 1:
            if bobinagem.num_bobinagem < 10:
                # instance.nome = '3%s-0%s' % (data, instance.num_bobinagem)
                bobinagem.nome = '3%s-0%s' % (data[1:], bobinagem.num_bobinagem)
                for b in bob:
                    if b.largura.num_bobine < 10:
                        b.nome = '%s-0%s' % (bobinagem.nome, b.largura.num_bobine)
                        b.save()
                    else:
                        b.nome = '%s-%s' % (bobinagem.nome, b.largura.num_bobine)
                        b.save()
            else:
                bobinagem.nome = '3%s-0%s' % (data[1:], bobinagem.num_bobinagem)
                for b in bob:
                    if b.largura.num_bobine < 10:
                        b.nome = '%s-0%s' % (bobinagem.nome, b.largura.num_bobine)
                        b.save()
                    else:
                        b.nome = '%s-%s' % (bobinagem.nome, b.largura.num_bobine)
                        b.save()
                
        elif bobinagem.perfil.retrabalho == True and (bobinagem.num_emendas == 0 or bobinagem.num_emendas == 1):
            if bobinagem.num_bobinagem < 10:
                bobinagem.nome = '4%s-0%s' % (data[1:], bobinagem.num_bobinagem)
                for b in bob:
                    if b.largura.num_bobine < 10:
                        b.nome = '%s-0%s' % (bobinagem.nome, b.largura.num_bobine)
                        b.save()
                    else:
                        b.nome = '%s-%s' % (bobinagem.nome, b.largura.num_bobine)
                        b.save()
                
            else:
                bobinagem.nome = '4%s-%s' % (data[1:], bobinagem.num_bobinagem)
                for b in bob:
                    if b.largura.num_bobine < 10:
                        b.nome = '%s-0%s' % (bobinagem.nome, b.largura.num_bobine)
                        b.save()
                    else:
                        b.nome = '%s-%s' % (bobinagem.nome, b.largura.num_bobine)
                        b.save()
                
        bobinagem.save()
        # bobinagem_pk = bobinagem.pk
        # bobine_nome(bobinagem_pk)
        bobine.save()
        emenda.delete()
        return redirect('producao:retrabalho_filter', pk=emenda.bobinagem.pk)

    template_name =  'retrabalho/emenda_delete.html'    
    context = {
           "emenda": emenda,
           "bobinagem": bobinagem,
           "bobine":bobine
    }
    return render(request, template_name, context)

@login_required
def cliente_home(request):
    cliente = Cliente.objects.all()

    template_name = 'cliente/cliente_home.html'
    context = {
        "cliente":cliente
    }
    return render(request, template_name, context)


@login_required
def producao_home(request):
    template_name = 'producao/producao_home.html'
    context = {}

    return render(request, template_name, context)

@login_required
def planeamento_home(request):
    template_name = 'producao/planeamento_home.html'
    context = {}

    return render(request, template_name, context)

@login_required
def bobine_details(request, pk):
     bobine = get_object_or_404(Bobine, pk=pk)
     
     emenda = Emenda.objects.filter(bobinagem=bobine.bobinagem)

     template_name = 'producao/bobine_details.html'
     context = {
         "bobine": bobine,
         "emenda": emenda,
     }
     return render(request, template_name, context)

@login_required
def relatorio_diario(request):
    inicio_data = request.GET.get("id")
    fim_data = request.GET.get("fd")
    inicio_hora = request.GET.get("fd")
    fim_hora = request.GET.get("fd")
    
    bobinagem = []

    area_g = 0
    area_r = 0
    area_dm = 0
    area_ind = 0
    area_ba = 0
  
    if inicio_data and fim_data:
         bobinagem = Bobinagem.objects.filter(data__range=(inicio_data, fim_data))
         for bob in bobinagem:
             area_g += bob.area_g
             area_r += bob.area_r
             area_dm += bob.area_dm
             area_ind += bob.area_ind
             area_ba += bob.area_ba

    template_name = 'relatorio/relatorio_diario_linha.html'
    context = {     
        "bobinagem": bobinagem,
        "area_g":area_g,
        "area_dm":area_dm,
        "area_r":area_r,
        "area_ba":area_ba,
        "area_ind":area_ind,
              
    }

    return render(request, template_name, context)

@login_required
def relatorio_consumos(request):
    inicio_data = request.GET.get("id")
    fim_data = request.GET.get("fd")
    inicio_hora = request.GET.get("fd")
    fim_hora = request.GET.get("fd")
      
    bobinagem = []
    c_sup_total = 0
    c_inf_total = 0
    c_sup = 0
    c_inf = 0
           
    if inicio_data and fim_data:
        bobinagem = Bobinagem.objects.filter(data__range=(inicio_data, fim_data))
        
        for bob in bobinagem:
            if bob.perfil.retrabalho == False:
                c_sup = bob.nwsup
                c_inf = bob.nwinf
                c_sup_total += c_sup
                c_inf_total += c_inf

    template_name = 'relatorio/relatorio_consumos.html'
    context = {     
        "bobinagem": bobinagem,
        "c_sup_total": c_sup_total,
        "c_inf_total": c_inf_total,
             
    }

    return render(request, template_name, context)

@login_required
def relatorio_paletes(request):
    inicio_data = request.GET.get("id")
    fim_data = request.GET.get("fd")
    inicio_hora = request.GET.get("fd")
    fim_hora = request.GET.get("fd")
      
    palete = []
    num_paletes = 0
    area_total = 0
    
           
    if inicio_data and fim_data:
        palete = Palete.objects.filter(data_pal__range=(inicio_data, fim_data), estado='G')
        
        for p in palete:
            area_total += p.area
            num_paletes += 1



    template_name = 'relatorio/relatorio_paletes.html'
    context = {     
        "palete": palete,
        "num_paletes": num_paletes,
        "area_total": area_total,
        
             
    }

    return render(request, template_name, context)

@login_required
def relatorio_home(request):
    template_name = 'relatorio/relatorio_home.html'
    context = {}

    return render(request, template_name, context)

@login_required
def etiqueta_retrabalho(request, pk):
    bobinagem = Bobinagem.objects.get(pk=pk)
    bobine = Bobine.objects.filter(bobinagem=bobinagem)

    if EtiquetaRetrabalho.objects.filter(bobinagem=bobinagem).exists():
        
        return redirect('producao:bobinestatus', pk=bobinagem.pk)
    else:
        for b in bobine:
            e_r = EtiquetaRetrabalho.objects.create(bobinagem=bobinagem, bobine=b.nome, data=bobinagem.data, produto=b.largura.designacao_prod, largura_bobinagem=bobinagem.perfil.largura_bobinagem, largura_bobine=b.largura.largura, diam=bobinagem.diam, comp_total=bobinagem.comp_cli, area=b.area)
            if Emenda.objects.filter(bobinagem=bobinagem).exists():
                emenda = Emenda.objects.filter(bobinagem=bobinagem)
                for e in emenda:
                    if e.num_emenda == 1:
                        e_r.bobine_original_1 = e.bobine.nome
                        e_r.emenda1 = e.emenda
                        e_r.metros1 = e.metros
                    elif e.num_emenda == 2:
                        e_r.bobine_original_2 = e.bobine.nome
                        e_r.emenda2 = e.emenda
                        e_r.metros2 = e.metros
                    elif e.num_emenda == 3:
                        e_r.bobine_original_3 = e.bobine.nome
                        e_r.emenda3 = e.emenda
                        e_r.metros3 = e.metros

                e_r.save()
        if bobinagem.perfil.retrabalho == True:
            return redirect('producao:bobinestatus', pk=bobinagem.pk)
        else:
            return redirect('producao:bobinagem_list_all')

@login_required
def etiqueta_palete(request, pk):
    palete = Palete.objects.get(pk=pk)
    bobine = Bobine.objects.filter(palete=palete)
    e_p = EtiquetaPalete.objects.get(palete=palete)
    d_min = 0
    d_max = 0
    e_p.produto = bobine[0].bobinagem.perfil.produto
    bobines = [None] * 61
    
    for b in bobine:
        pos = b.posicao_palete
        bobines[pos] = b.nome
        d = b.bobinagem.diam
        if d_max == 0:
            d_max = d
        elif d > d_max:
            d_max = d
        elif d_min == 0:
            d_min = d
        elif d < d_min:
            d_min = d 

    e_p.bobine1 = bobines[1]
    e_p.bobine2 = bobines[2]
    e_p.bobine3 = bobines[3]
    e_p.bobine4 = bobines[4]
    e_p.bobine5 = bobines[5]
    e_p.bobine6 = bobines[6]
    e_p.bobine7 = bobines[7]
    e_p.bobine8 = bobines[8]
    e_p.bobine9 = bobines[9]
    e_p.bobine10 = bobines[10]
    e_p.bobine11 = bobines[11]
    e_p.bobine12 = bobines[12]
    e_p.bobine13 = bobines[13]
    e_p.bobine14 = bobines[14]
    e_p.bobine15 = bobines[15]
    e_p.bobine16 = bobines[16]
    e_p.bobine17 = bobines[17]
    e_p.bobine18 = bobines[18]
    e_p.bobine19 = bobines[19]
    e_p.bobine20 = bobines[20]
    e_p.bobine21 = bobines[21]
    e_p.bobine22 = bobines[22]
    e_p.bobine23 = bobines[23]
    e_p.bobine24 = bobines[24]
    e_p.bobine25 = bobines[25]
    e_p.bobine26 = bobines[26]
    e_p.bobine27 = bobines[27]
    e_p.bobine28 = bobines[28]
    e_p.bobine29 = bobines[29]
    e_p.bobine30 = bobines[30]
    e_p.bobine31 = bobines[31]
    e_p.bobine32 = bobines[32]
    e_p.bobine33 = bobines[33]
    e_p.bobine34 = bobines[34]
    e_p.bobine35 = bobines[35]
    e_p.bobine36 = bobines[36]
    e_p.bobine37 = bobines[37]
    e_p.bobine38 = bobines[38]
    e_p.bobine39 = bobines[39]
    e_p.bobine40 = bobines[40]
    e_p.bobine41 = bobines[41]
    e_p.bobine42 = bobines[42]
    e_p.bobine43 = bobines[43]
    e_p.bobine44 = bobines[44]
    e_p.bobine45 = bobines[45]
    e_p.bobine46 = bobines[46]
    e_p.bobine47 = bobines[47]
    e_p.bobine48 = bobines[48]
    e_p.bobine49 = bobines[49]
    e_p.bobine50 = bobines[50]
    e_p.bobine51 = bobines[51]
    e_p.bobine52 = bobines[52]
    e_p.bobine53 = bobines[53]
    e_p.bobine54 = bobines[54]
    e_p.bobine55 = bobines[55]
    e_p.bobine56 = bobines[56]
    e_p.bobine57 = bobines[57]
    e_p.bobine58 = bobines[58]
    e_p.bobine59 = bobines[59]
    e_p.bobine60 = bobines[60]
    e_p.diam_min = d_min
    e_p.diam_max = d_max
    e_p.save()
                
    return redirect('producao:addbobinepalete', pk=palete.pk)



@login_required
def error_500(request):
    data = {}
    return render(request, 'error/error_500.html', data)

@login_required
def ordenar_bobines(request, pk):
    template_name = "palete/ordenar_bobines_formset.html"
    OrdenarBobinesFormSet = modelformset_factory(Bobine, form=OrdenarBobines, extra=0)
    palete = Palete.objects.get(pk=pk)
    bobines = Bobine.objects.filter(palete=palete)
    formset = OrdenarBobinesFormSet(request.POST or None, queryset=bobines)
    if formset.is_valid():
        bobs = formset.save(commit=False)
        for bob in bobs:
            bob.save()

    context = {
        "formset": formset,
        "bobines":bobines
    }

    return render(request, template_name, context)

@login_required
def c_bobines(request, pk):
    template_name = "producao/classificacao_bobines_formset.html"
    ClassificacaoBobinesFormSet = modelformset_factory(Bobine, form=ClassificacaoBobines, extra=0)
    bobinagem = Bobinagem.objects.get(pk=pk)
    bobines = Bobine.objects.filter(bobinagem=bobinagem)
    formset = ClassificacaoBobinesFormSet(request.POST or None, queryset=bobines)
    if formset.is_valid():
        bobs = formset.save(commit=False)
        for bob in bobs:
            bob.save()
    
    context = {
        "formset": formset,
        "bobines": bobines, 
        "bobinagem": bobinagem
        
    }

    return render(request, template_name, context)



@login_required
def retrabalho(request):
    template_name = 'retrabalho/retrabalho_formset.html'
    RetrabalhoFormSet = modelformset_factory(Emenda, form=RetrabalhoForm, extra=3)
    formset = RetrabalhoFormSet(request.POST or None)

    

    for f in formset:
        bobine = f['bobine'].value()
        print(bobine)
        bobine = Bobine.objects.get(nome=bobine)
        f.bobine = bobine.id


        print(f.bobine)
        

    
   
    if formset.is_valid():
        retrabalho = formset.save(commit=False)
        for r in retrabalho:
            r.save()


    context = {
        "formset": formset,
             
    }

    return render(request, template_name, context)

def destruir_bobine(request, pk_bobinagem, pk_bobine):
    bobine = Bobine.objects.get(pk=pk_bobine)
    bobinagem = Bobinagem.objects.get(pk=pk_bobinagem)

    margem_min = bobine.bobinagem.comp_cli * Decimal('0.20')
    print(margem_min)
    if bobine.comp_actual < margem_min:
        bobine.recycle = True
        bobine.save()
        return redirect('producao:retrabalho_filter', pk=bobinagem.pk)
    else:
        return redirect('producao:retrabalho_filter', pk=bobinagem.pk)




@login_required
def bobinagem_list_all(request):
    
    bobinagem = Bobinagem.objects.all()
   
        
    template_name = 'producao/bobinagem_list_all.html'
    context = {
               
        "bobinagem": bobinagem,
              
    }

    return render(request, template_name, context)

@login_required
def bobinagem_list_all_historico(request):
    
    bobinagem = Bobinagem.objects.all()
         
    template_name = 'producao/bobinagem_list_all_historico.html'
   
    context = {
               
        "bobinagem": bobinagem,
              
    }

    return render(request, template_name, context)


@login_required
def palete_list_all(request):
    
    palete = Palete.objects.all()
   
        
    template_name = 'palete/palete_list_all.html'
    context = {
               
        "palete": palete,
              
    }

    return render(request, template_name, context)

@login_required
def palete_list_all_historico(request):
    
    palete = Palete.objects.all()
   
        
    template_name = 'palete/palete_list_all_historico.html'
    context = {
               
        "palete": palete,
              
    }

    return render(request, template_name, context)

@login_required
def palete_details(request, pk):
    palete = Palete.objects.get(pk=pk)

    template_name = 'palete/palete_details.html'


    context = {
        "palete":palete,
    }

    return render(request, template_name, context)



@login_required
def palete_confirmation(request, pk, id_bobines):
    palete = Palete.objects.get(pk=pk)
    e_p = EtiquetaPalete.objects.get(palete=palete)
    bobines = id_bobines
    num = 1
    comp = 0
    area = 0
    bobines_array = bobines.split("-")
    del bobines_array[-1]
    for x in bobines_array:
        id_b = int(x)
        bobine = Bobine.objects.get(pk=id_b)
        if bobine.palete != None:
            palete_o = Palete.objects.get(id=bobine.palete.id)
            palete_o.area -= bobine.area
            palete_o.comp_total -= bobine.bobinagem.comp 
            palete_o.num_bobines_act -= 1
            palete_o.num_bobines -= 1
            palete_o.save()
        bobine.palete = palete
        bobine.posicao_palete = num
        comp += bobine.comp_actual
        area += bobine.area
        bobine.save()
        num += 1
                 

        
    palete.num_bobines_act = num - 1
    palete.area = area
    palete.comp_total = comp
    palete.save()
        
    d_min = 0
    d_max = 0
    
    b = int(bobines_array[0])
    bobine_produto = Bobine.objects.get(pk=b)
    e_p.produto = bobine_produto.largura.designacao_prod
    bobine_posicao = [None] * 61
    
    for x in bobines_array:
        id_b = int(x)
        bobine = Bobine.objects.get(pk=id_b)
        pos = bobine.posicao_palete
        bobine_posicao[pos] = bobine.nome
        d = bobine.bobinagem.diam
        
        if d_min == 0 and d_max == 0: 
            d_min = d
            d_max = d
        elif d <= d_min:
            d_min = d
        elif d >= d_max:
            d_max = d
      

    e_p.bobine1 = bobine_posicao[1]
    e_p.bobine2 = bobine_posicao[2]
    e_p.bobine3 = bobine_posicao[3]
    e_p.bobine4 = bobine_posicao[4]
    e_p.bobine5 = bobine_posicao[5]
    e_p.bobine6 = bobine_posicao[6]
    e_p.bobine7 = bobine_posicao[7]
    e_p.bobine8 = bobine_posicao[8]
    e_p.bobine9 = bobine_posicao[9]
    e_p.bobine10 = bobine_posicao[10]
    e_p.bobine11 = bobine_posicao[11]
    e_p.bobine12 = bobine_posicao[12]
    e_p.bobine13 = bobine_posicao[13]
    e_p.bobine14 = bobine_posicao[14]
    e_p.bobine15 = bobine_posicao[15]
    e_p.bobine16 = bobine_posicao[16]
    e_p.bobine17 = bobine_posicao[17]
    e_p.bobine18 = bobine_posicao[18]
    e_p.bobine19 = bobine_posicao[19]
    e_p.bobine20 = bobine_posicao[20]
    e_p.bobine21 = bobine_posicao[21]
    e_p.bobine22 = bobine_posicao[22]
    e_p.bobine23 = bobine_posicao[23]
    e_p.bobine24 = bobine_posicao[24]
    e_p.bobine25 = bobine_posicao[25]
    e_p.bobine26 = bobine_posicao[26]
    e_p.bobine27 = bobine_posicao[27]
    e_p.bobine28 = bobine_posicao[28]
    e_p.bobine29 = bobine_posicao[29]
    e_p.bobine30 = bobine_posicao[30]
    e_p.bobine31 = bobine_posicao[31]
    e_p.bobine32 = bobine_posicao[32]
    e_p.bobine33 = bobine_posicao[33]
    e_p.bobine34 = bobine_posicao[34]
    e_p.bobine35 = bobine_posicao[35]
    e_p.bobine36 = bobine_posicao[36]
    e_p.bobine37 = bobine_posicao[37]
    e_p.bobine38 = bobine_posicao[38]
    e_p.bobine39 = bobine_posicao[39]
    e_p.bobine40 = bobine_posicao[40]
    e_p.bobine41 = bobine_posicao[41]
    e_p.bobine42 = bobine_posicao[42]
    e_p.bobine43 = bobine_posicao[43]
    e_p.bobine44 = bobine_posicao[44]
    e_p.bobine45 = bobine_posicao[45]
    e_p.bobine46 = bobine_posicao[46]
    e_p.bobine47 = bobine_posicao[47]
    e_p.bobine48 = bobine_posicao[48]
    e_p.bobine49 = bobine_posicao[49]
    e_p.bobine50 = bobine_posicao[50]
    e_p.bobine51 = bobine_posicao[51]
    e_p.bobine52 = bobine_posicao[52]
    e_p.bobine53 = bobine_posicao[53]
    e_p.bobine54 = bobine_posicao[54]
    e_p.bobine55 = bobine_posicao[55]
    e_p.bobine56 = bobine_posicao[56]
    e_p.bobine57 = bobine_posicao[57]
    e_p.bobine58 = bobine_posicao[58]
    e_p.bobine59 = bobine_posicao[59]
    e_p.bobine60 = bobine_posicao[60]
    e_p.diam_min = d_min
    e_p.diam_max = d_max
    e_p.save()

    for x in bobines_array:
        id_b = int(x)
        bobine = Bobine.objects.get(pk=id_b)
        if bobine.bobinagem.perfil.retrabalho == True:
            
            ano = palete.data_pal
            ano = ano.strftime('%Y')
            num = palete.num
            if num < 10:    
                palete.nome = 'R000%s-%s' % (num, ano)  
                e_p.palete_nome = palete.nome
            elif num < 100:
                palete.nome = 'R00%s-%s' % (num, ano)
                e_p.palete_nome = palete.nome
            elif num < 1000: 
                palete.nome = 'R0%s-%s' % (num, ano)
                e_p.palete_nome = palete.nome
            else: 
                palete.nome = 'R%s-%s' % (num, ano)
                e_p.palete_nome = palete.nome
            
            palete.save()
            e_p.save()
            break
    
    add_artigo_to_bobine(pk)
          
    return redirect('producao:addbobinepalete', pk=palete.pk)
    
@login_required
def palete_rabrir(request, pk):
    palete = Palete.objects.get(pk=pk)
    
    bobines = Bobine.objects.filter(palete=palete)
    e_p = EtiquetaPalete.objects.get(palete=palete)
    e_p.diam_min = 0  
    e_p.diam_max = 0 
    if palete.estado == 'G':
        ano = palete.data_pal
        ano = ano.strftime('%Y')
        num = palete.num
        if num < 10:    
            palete.nome = 'P000%s-%s' % (num, ano)  
            e_p.palete_nome = palete.nome
        elif num < 100:
            palete.nome = 'P00%s-%s' % (num, ano)
            e_p.palete_nome = palete.nome
        elif num < 1000: 
            palete.nome = 'P0%s-%s' % (num, ano)
            e_p.palete_nome = palete.nome
        else: 
            palete.nome = 'P%s-%s' % (num, ano)
            e_p.palete_nome = palete.nome

    palete.num_bobines_act = 0
    palete.save()
    e_p.save()
    for b in bobines:
        b.palete = None
        b.save()
    if palete.estado == 'G':
        return redirect('producao:palete_picagem', pk=palete.pk)
    elif palete.estado == 'DM':
        return redirect('producao:picagem_palete_dm', pk=palete.pk)

@login_required
def picagem_palete_dm(request, pk):
    palete = Palete.objects.get(pk=pk)
    e_p = EtiquetaPalete.objects.get(palete=palete)

    template_name = 'palete/picagem_palete_dm.html'


    context = {
        "palete":palete,
        "e_p":e_p,
    }

    return render(request, template_name, context)

@login_required
def validate_palete_dm(request, pk, id_bobines):
    palete = Palete.objects.get(pk=pk)
    e_p = EtiquetaPalete.objects.get(palete=palete)
    bobines = id_bobines
    num = 1
    comp = 0
    area = 0
    bobines_array = bobines.split("-")
    del bobines_array[-1]
    for x in bobines_array:
        id_b = int(x)
        bobine = Bobine.objects.get(pk=id_b)
        bobine.palete = palete
        bobine.posicao_palete = num
        comp += bobine.comp_actual
        
            
        area += bobine.area
        bobine.save()
        num += 1
    
    palete.num_bobines_act = num - 1
    if palete.retrabalhada == True:
        palete.num_bobines = palete.num_bobines_act
    palete.area = area
    palete.comp_total = comp
    palete.save()
       
    d_min = 0
    d_max = 0
    
    b = int(bobines_array[0])
    bobine_produto = Bobine.objects.get(pk=b)
    e_p.produto = bobine_produto.bobinagem.perfil.produto
    bobine_posicao = [None] * 61
    
    for x in bobines_array:
        id_b = int(x)
        bobine = Bobine.objects.get(pk=id_b)
        pos = bobine.posicao_palete
        bobine_posicao[pos] = bobine.nome
        d = bobine.bobinagem.diam
        
        if d_min == 0 and d_max == 0: 
            d_min = d
            d_max = d
        elif d <= d_min:
            d_min = d
        elif d >= d_max:
            d_max = d
      

    e_p.bobine1 = bobine_posicao[1]
    e_p.bobine2 = bobine_posicao[2]
    e_p.bobine3 = bobine_posicao[3]
    e_p.bobine4 = bobine_posicao[4]
    e_p.bobine5 = bobine_posicao[5]
    e_p.bobine6 = bobine_posicao[6]
    e_p.bobine7 = bobine_posicao[7]
    e_p.bobine8 = bobine_posicao[8]
    e_p.bobine9 = bobine_posicao[9]
    e_p.bobine10 = bobine_posicao[10]
    e_p.bobine11 = bobine_posicao[11]
    e_p.bobine12 = bobine_posicao[12]
    e_p.bobine13 = bobine_posicao[13]
    e_p.bobine14 = bobine_posicao[14]
    e_p.bobine15 = bobine_posicao[15]
    e_p.bobine16 = bobine_posicao[16]
    e_p.bobine17 = bobine_posicao[17]
    e_p.bobine18 = bobine_posicao[18]
    e_p.bobine19 = bobine_posicao[19]
    e_p.bobine20 = bobine_posicao[20]
    e_p.bobine21 = bobine_posicao[21]
    e_p.bobine22 = bobine_posicao[22]
    e_p.bobine23 = bobine_posicao[23]
    e_p.bobine24 = bobine_posicao[24]
    e_p.bobine25 = bobine_posicao[25]
    e_p.bobine26 = bobine_posicao[26]
    e_p.bobine27 = bobine_posicao[27]
    e_p.bobine28 = bobine_posicao[28]
    e_p.bobine29 = bobine_posicao[29]
    e_p.bobine30 = bobine_posicao[30]
    e_p.bobine31 = bobine_posicao[31]
    e_p.bobine32 = bobine_posicao[32]
    e_p.bobine33 = bobine_posicao[33]
    e_p.bobine34 = bobine_posicao[34]
    e_p.bobine35 = bobine_posicao[35]
    e_p.bobine36 = bobine_posicao[36]
    e_p.bobine37 = bobine_posicao[37]
    e_p.bobine38 = bobine_posicao[38]
    e_p.bobine39 = bobine_posicao[39]
    e_p.bobine40 = bobine_posicao[40]
    e_p.bobine41 = bobine_posicao[41]
    e_p.bobine42 = bobine_posicao[42]
    e_p.bobine43 = bobine_posicao[43]
    e_p.bobine44 = bobine_posicao[44]
    e_p.bobine45 = bobine_posicao[45]
    e_p.bobine46 = bobine_posicao[46]
    e_p.bobine47 = bobine_posicao[47]
    e_p.bobine48 = bobine_posicao[48]
    e_p.bobine49 = bobine_posicao[49]
    e_p.bobine50 = bobine_posicao[50]
    e_p.bobine51 = bobine_posicao[51]
    e_p.bobine52 = bobine_posicao[52]
    e_p.bobine53 = bobine_posicao[53]
    e_p.bobine54 = bobine_posicao[54]
    e_p.bobine55 = bobine_posicao[55]
    e_p.bobine56 = bobine_posicao[56]
    e_p.bobine57 = bobine_posicao[57]
    e_p.bobine58 = bobine_posicao[58]
    e_p.bobine59 = bobine_posicao[59]
    e_p.bobine60 = bobine_posicao[60]
    e_p.diam_min = d_min
    e_p.diam_max = d_max
    e_p.save()

    
       
    return redirect('producao:addbobinepalete', pk=palete.pk)

@login_required
def retrabalho_dm(request, pk):
    bobinagem = Bobinagem.objects.get(pk=pk)

    template_name = 'retrabalho/retrabalho_dm.html'
    


    context = {
        "bobinagem": bobinagem,
        
    }

    return render(request, template_name, context)

@login_required
def validate_bobinagem_dm(request, pk, id_bobines, metros, recycle):

    bobinagem = Bobinagem.objects.get(pk=pk)
    bobines = Bobine.objects.filter(bobinagem=bobinagem)
    
    bobines_originais = id_bobines
    metros_bobines = metros
    recycle_bobines = recycle
    comp_total = 0
    emendas = 0
    cont = 0
    recycle_value = 0
    bobines_array = bobines_originais.split("--")
    metros_array = metros_bobines.split("-")
    recycle_array = recycle_bobines.split("-")  
    bobines_length = len(bobines_array)
    

    for x in bobines_array:
        bobine = Bobine.objects.get(nome=x)
        comp_actual = bobine.comp_actual 
        comp_actual -= Decimal(metros_array[cont])
        bobine.comp_actual = comp_actual
        comp_total += Decimal(metros_array[cont])
        bobine.recycle = recycle_array[recycle_value].capitalize() 
        bobine.save()
        recycle_value += 1 
        cont += 1
        emendas += 1
        emenda = Emenda.objects.create(bobinagem=bobinagem, bobine=bobine, metros=Decimal(metros_array[cont-1]), emenda=comp_total, num_emenda=cont)
        emenda.save()

      

    bobinagem.num_emendas = emendas - 1
    bobinagem.comp = comp_total
    bobinagem.comp_cli = comp_total
    bobinagem.estado = 'G'
    largura_bobinagem = bobinagem.perfil.largura_bobinagem / 1000
    bobinagem.area = bobinagem.comp_cli * largura_bobinagem
    bobinagem.save()
    print(emendas)

    for b in bobines:
        b.comp_actual = bobinagem.comp_cli
        b.estado = 'G'
        largura = b.largura.largura / 1000
        area = largura * b.bobinagem.comp_cli
        b.area = area
        b.save()
        if emendas == 1 or emendas == 0:
            pass
        elif emendas > 1:
            data = bobinagem.data
            data = data.strftime('%Y%m%d')
            map(int, data)
            if bobinagem.num_bobinagem < 10:
                bobinagem.nome = '3%s-0%s' % (data[1:], bobinagem.num_bobinagem)
                bobinagem_pk = bobinagem.pk
                bobine_nome(bobinagem_pk)
                bobinagem.save()
            else:
                bobinagem.nome = '3%s-%s' % (data[1:], bobinagem.num_bobinagem)
                bobinagem_pk = bobinagem.pk
                bobine_nome(bobinagem_pk)
                bobinagem.save()
    
    
    return redirect('producao:finalizar_retrabalho', pk=bobinagem.pk)

@login_required   
def refazer_bobinagem_dm(request, pk):
    bobinagem = Bobinagem.objects.get(pk=pk)
    bobines = Bobine.objects.filter(bobinagem=bobinagem)
    emendas = Emenda.objects.filter(bobinagem=bobinagem)

    data = bobinagem.data
    data = data.strftime('%Y%m%d')

    if bobinagem.num_bobinagem < 10:
        bobinagem.nome = '4%s-0%s' % (data[1:], bobinagem.num_bobinagem)
    else:
        bobinagem.nome = '4%s-%s' % (data[1:], bobinagem.num_bobinagem)
    
    num = 1
    for b in bobines:
        if num < 10:
            b.nome = '%s-0%s' % (bobinagem.nome, num)
        else:
            b.nome = '%s-%s' % (bobinagem.nome, num)
        num += 1
        b.area = 0
        b.comp_actual = 0 
        b.save()

    for e in emendas:
        bobine_original = Bobine.objects.get(pk=e.bobine.pk)
        bobine_original.comp_actual += e.metros
        if bobine_original.recycle == True:
            bobine_original.recycle = False
        bobine_original.save()
        e.delete() 

    bobinagem.num_emendas = 0
    bobinagem.comp = 0
    bobinagem.comp_par = 0
    bobinagem.comp_cli = 0
    bobinagem.diam = 0
    bobinagem.area = 0
    bobinagem.fim = None
    bobinagem.duracao = None
    bobinagem.area_g = 0
    bobinagem.area_dm = 0
    bobinagem.area_r = 0
    bobinagem.area_ind = 0
    bobinagem.area_ba = 0
    bobinagem.save()
    return redirect('producao:retrabalho_v2', pk=bobinagem.pk)

@login_required       
def delete_bobinagem_dm(request, pk):
    bobinagem = Bobinagem.objects.get(pk=pk)
    bobines = Bobines.objects.filter(bobinagem=bobinagem)
    emendas = Emenda.objects.filter(bobinagem=bobinagem)

    for b in bobines:
        b.delete()

    bobinagem.delete()
    pass

@login_required
def encomenda_list(request):
    enc = Encomenda.objects.all()

    template_name = 'encomenda/encomenda_list.html'

    context = {
        'enc': enc,
    }

    return render(request, template_name, context)


@login_required
def encomenda_create(request):

    template_name = 'encomenda/encomenda_create.html'
    form = EncomendaCreateForm(request.POST or None)
        
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
                    
        
        return redirect('producao:encomenda_list')

    context = {
        "form": form
    }

    return render(request, template_name, context)


@login_required
def encomenda_detail(request, pk):
    enc = get_object_or_404(Encomenda, pk=pk)

    template_name = 'encomenda/encomenda_detail.html'

    context = {
        "enc": enc
    }

    return render(request, template_name, context)

@login_required
def carga_list(request):
    carga = Carga.objects.all()

    template_name = 'carga/carga_list.html'

    context = {
        'carga': carga,
    }

    return render(request, template_name, context)

@login_required
def carga_list_completa(request):
    carga = Carga.objects.all()

    template_name = 'carga/carga_list_complete.html'

    context = {
        'carga': carga,
    }

    return render(request, template_name, context)


@login_required
def carga_create(request):

    template_name = 'carga/carga_create.html'
    form = CargaCreateForm(request.POST or None)
        
    if form.is_valid():
        instance = form.save(commit=False)
        instance.user = request.user
        instance.sqm = 0
        num_carga = form.cleaned_data['num_carga']
        tipo = form.cleaned_data['tipo']
        enc = str(form.cleaned_data['enc'])
        encomenda = get_object_or_404(Encomenda, eef=enc)
        cargas = Carga.objects.all()
        prf = encomenda.prf
        if num_carga > encomenda.num_cargas:
            return redirect('producao:carga_create')

        if num_carga < 10:
            if tipo == "CONTENTOR":
                num_carga = str(num_carga)
                carga = prf + "-CON00" + num_carga + "-" + str(encomenda.cliente.abv)
            else:
                num_carga = str(num_carga)
                carga = prf + "-CON00" + num_carga + "-" + str(encomenda.cliente.abv)
        elif num_carga < 100:
            if tipo == "CONTENTOR":
                num_carga = str(num_carga)
                carga = prf + "-CON0" + num_carga + "-" + str(encomenda.cliente.abv)
            else:
                num_carga = str(num_carga)
                carga = prf + "-CON0" + num_carga + "-" + str(encomenda.cliente.abv)
        elif num_carga < 1000:
            if tipo == "CONTENTOR":
                num_carga = str(num_carga)
                carga = prf + "-CON" + num_carga + "-" + str(encomenda.cliente.abv)
            else:
                num_carga = str(num_carga)
                carga = prf + "-CON" + num_carga + "-" + str(encomenda.cliente.abv)

        for c in cargas:
            if c.carga == carga:
                return redirect('producao:carga_create')
        
          

        instance.carga = carga    
        instance.save()

        encomenda.num_cargas_actual += 1
        if (encomenda.num_cargas_actual == encomenda.num_cargas):
            encomenda.estado = 'F'
        encomenda.save()

        
        
        return redirect('producao:carga_list')

    context = {
        "form": form
    }

    return render(request, template_name, context)

@login_required
def carga_detail(request, pk):
    carga = get_object_or_404(Carga, pk=pk)
    paletes = Palete.objects.filter(carga=carga)
    som = 0 
    som_comp = 0
    som_area = 0
    
    for p in paletes:
        som += (p.peso_liquido/(p.area/10))*100
        som_area += (p.peso_liquido * 1000) / 100 
        som_comp += (Decimal(som_area) / ((Decimal(p.num_bobines) * Decimal(p.largura_bobines)) * Decimal(0.001))) * (Decimal(p.num_bobines))
        print(som_comp)
        
    
    if len(paletes) == 0:
        som = 0
    else:
        som = som / len(paletes)
    
    som = round(som, 2)
    som_comp = round(som_comp, 2)
    som_area = round(som_area, 2)
      
    data_inicial = 0
    data_final = 0

    for p in paletes:
        bobines = Bobine.objects.filter(palete=p)
        
        for b in bobines:
            data = b.bobinagem.data 
            if data_inicial == 0 and data_final == 0:
                data_inicial = data
                data_final = data
            elif data <= data_inicial:
                data_inicial = data
            elif data >= data_final:
                data_final = data
         

            

    template_name = 'carga/carga_detail.html'
    context = {
        "carga": carga,
        "data_inicial": data_inicial,
        "data_final": data_final,
        "som": som,
        "som_comp": som_comp,
        "som_area": som_area
    }

    return render(request, template_name, context)

    

@login_required
def carga_edit(request, pk):
    pass


@login_required
def armazem_home(request):
    template_name = 'producao/armazem_home.html'
    context = {}

    return render(request, template_name, context)

@login_required
def palete_selecao(request):
    template_name = 'palete/palete_selecao.html'
    form = SelecaoPaleteForm(request.POST or None)
    
    if request.method == 'POST':
        form = SelecaoPaleteForm(request.POST or None)
        if form.is_valid:
            palete_nome = form['palete'].value()
            palete = get_object_or_404(Palete, nome=palete_nome)
            return redirect('producao:palete_pesagem', pk=palete.pk)

    context = {
        "form": form
    }

    return render(request, template_name, context)

@login_required
def palete_pesagem(request, pk=None):
    instance = get_object_or_404(Palete, pk=pk)
    template_name = 'palete/palete_pesagem.html'
    palete = get_object_or_404(Palete, pk=pk)
    form = PaletePesagemForm(request.POST or None, instance=instance)

    if form.is_valid():
        instance = form.save(commit=False)
        carga_nome = str(form.cleaned_data['carga'])
       
        if Carga.objects.filter(carga=carga_nome).exists():
            carga = get_object_or_404(Carga, carga=carga_nome)
            
            if carga.num_paletes > carga.num_paletes_actual and instance.stock == False:
                if palete.carga == None:
                    instance.carga = carga
                    instance.peso_liquido = instance.peso_bruto - int(instance.peso_palete)
                    # palete_carga_num(carga.pk, instance.pk)
                    paletes_carga_1 = Palete.objects.filter(carga=carga)
                    cont = 0
                    array_num_palete = []
                        
                    for p1 in paletes_carga_1:
                        array_num_palete.append(p1.num_palete_carga)
                        # array_num_palete[cont] = p1.num_palete_carga
                        # cont += 1

                    if len(array_num_palete) == 0:
                        instance.num_palete_carga = 1
                    else:
                        array_num_palete.sort()
                        cont2 = 0
                        for a in array_num_palete:
                            if a != cont2 + 1:
                                instance.num_palete_carga = cont2 + 1
                                break
                            elif len(array_num_palete) == cont2 + 1:
                                instance.num_palete_carga = cont2 + 2
                                break 
                            cont2 += 1

                    carga.num_paletes_actual += 1
                    if carga.num_paletes == carga.num_paletes_actual:
                        carga.estado = 'C'
                    
                    carga.sqm += instance.area 
                    carga.metros += instance.comp_total
                    carga.save()
                    instance.save()
                    gerar_etiqueta_final(instance.pk)
                else:
                    carga_antiga = get_object_or_404(Carga, pk=palete.carga.pk)    
                    if carga_antiga != carga:                                
                        if carga.num_paletes_actual < carga.num_paletes:
                            carga_antiga.num_paletes_actual -= 1
                            if carga_antiga.num_paletes_actual < carga_antiga.num_paletes:
                                carga_antiga.estado = 'I'
                            
                            carga.num_paletes_actual += 1
                            if carga.num_paletes_actual == carga.num_paletes:
                                carga.estado = "C"

                            carga_antiga.sqm -= palete.area
                            carga_antiga.metros -= palete.comp_total
                            instance.peso_liquido = instance.peso_bruto - int(instance.peso_palete)
                            
                            paletes_carga_1 = Palete.objects.filter(carga=carga)
                            cont = 0
                            array_num_palete = []
                                
                            for p1 in paletes_carga_1:
                                array_num_palete.append(p1.num_palete_carga)
                                
                            if len(array_num_palete) == 0:
                                instance.num_palete_carga = 1
                            else:
                                array_num_palete.sort()
                                cont2 = 0
                                for a in array_num_palete:
                                    if a != cont2 + 1:
                                        instance.num_palete_carga = cont2 + 1
                                        break
                                    elif len(array_num_palete) == cont2 + 1:
                                        instance.num_palete_carga = cont2 + 2
                                        break 
                                    cont2 += 1

                            
                            carga.sqm += instance.area 
                            carga.metros += instance.comp_total

                            carga.save()
                            carga_antiga.save()
                            instance.save()
                            gerar_etiqueta_final(instance.pk)
                        else:
                            return redirect('producao:palete_pesagem', pk=instance.pk)

                    elif carga_antiga == carga:
                        if carga.num_paletes_actual < carga.num_paletes:
                                               
                            carga.sqm -= palete.area
                            carga.metros -= palete.comp_total
                            instance.peso_liquido = instance.peso_bruto - int(instance.peso_palete)
                                                              
                            carga.sqm += instance.area 
                            carga.metros += instance.comp_total

                            carga.save()
                            instance.save()
                            gerar_etiqueta_final(instance.pk)

            elif carga.num_paletes == carga.num_paletes_actual and instance.stock == False:
                carga_antiga = get_object_or_404(Carga, pk=palete.carga.pk)
                if carga_antiga == carga:
                    carga.sqm -= palete.area
                    carga.metros -= palete.comp_total
                    instance.peso_liquido = instance.peso_bruto - int(instance.peso_palete)
                                                        
                    carga.sqm += instance.area 
                    carga.metros += instance.comp_total

                    carga.save()
                    instance.save()
                    gerar_etiqueta_final(instance.pk)
                
                elif carga_antiga != carga:
                    if carga.num_paletes_actual < carga.num_paletes:
                        carga_antiga.num_paletes_actual -= 1
                        if carga_antiga.num_paletes_actual < carga_antiga.num_paletes:
                            carga_antiga.estado = 'I'
                        
                        carga.num_paletes_actual += 1
                        if carga.num_paletes_actual == carga.num_paletes:
                            carga.estado = "C"

                        carga_antiga.sqm -= palete.area
                        carga_antiga.metros -= palete.comp_total
                        instance.peso_liquido = instance.peso_bruto - int(instance.peso_palete)
                        
                        paletes_carga_1 = Palete.objects.filter(carga=carga)
                        cont = 0
                        array_num_palete = []
                            
                        for p1 in paletes_carga_1:
                            array_num_palete.append(p1.num_palete_carga)
                            
                        if len(array_num_palete) == 0:
                            instance.num_palete_carga = 1
                        else:
                            array_num_palete.sort()
                            cont2 = 0
                            for a in array_num_palete:
                                if a != cont2 + 1:
                                    instance.num_palete_carga = cont2 + 1
                                    break
                                elif len(array_num_palete) == cont2 + 1:
                                    instance.num_palete_carga = cont2 + 2
                                    break 
                                cont2 += 1

                        
                        carga.sqm += instance.area 
                        carga.metros += instance.comp_total

                        carga.save()
                        carga_antiga.save()
                        instance.save()
                        gerar_etiqueta_final(instance.pk)
                else:
                    redirect('producao:palete_pesagem', pk=instance.pk)


            else:
                return redirect('producao:palete_pesagem', pk=instance.pk)

        elif instance.stock == True:
            if palete.carga == None:
                instance.peso_liquido = instance.peso_bruto - int(instance.peso_palete)
                instance.save()
            else:
                carga = get_object_or_404(Carga, pk=palete.carga.pk)
                carga.num_paletes_actual -= 1
                carga.sqm -= palete.area
                carga.metros -= palete.comp_total
                if carga.num_paletes_actual < carga.num_paletes:
                    carga.estado = 'I'
                carga.save()
                instance.num_palete_carga = None
                instance.peso_liquido = instance.peso_bruto - int(instance.peso_palete)
                instance.save()
        else:
            return redirect('producao:palete_pesagem', pk=instance.pk)
       
        
        
        return redirect('producao:palete_selecao')

    context = {
        "form": form,
        "instance": instance,
        
    }

    return render(request, template_name, context)


@login_required
def palete_details_armazem(request, pk):

    palete = get_object_or_404(Palete, pk=pk)
    template_name = 'palete/palete_details_armazem.html'


    context = {
        "palete": palete,
        
        
    }

    return render(request, template_name, context)

@login_required
def stock_list(request):

    paletes = Palete.objects.filter(stock=True)

    template_name = 'stock/stock_list.html'

    context = {
        'paletes': paletes,
    }

    return render(request, template_name, context)

@login_required
def stock_add_to_carga(request, pk=None):
    instance = get_object_or_404(Palete, pk=pk)
    template_name = 'stock/stock_add_carga.html'

    form = AddPalateStockForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.stock = False
        carga = Carga.objects.get(carga=instance.carga)
        carga.num_paletes_actual += 1

        paletes_carga_1 = Palete.objects.filter(carga=carga)
        cont = 0
        array_num_palete = []
            
        for p1 in paletes_carga_1:
            array_num_palete.append(p1.num_palete_carga)
            # array_num_palete[cont] = p1.num_palete_carga
            # cont += 1

        if len(array_num_palete) == 0:
            instance.num_palete_carga = 1
        else:
            array_num_palete.sort()
            cont2 = 0
            for a in array_num_palete:
                if a != cont2 + 1:
                    instance.num_palete_carga = cont2 + 1
                    break
                elif len(array_num_palete) == cont2 + 1:
                    instance.num_palete_carga = cont2 + 2
                    break 
                cont2 += 1

        carga.sqm += instance.area
        carga.metros += instance.comp_total
        if carga.num_paletes_actual == carga.num_paletes:
            carga.estado = 'C'
        
        carga.save()
        instance.save()
        gerar_etiqueta_final(instance.pk)
        
        return redirect('producao:palete_details_armazem', pk=instance.pk)

    context = {
        "form": form,
        "instance": instance,
    }

    return render(request, template_name, context)


@login_required
def acompanhamento_diario(request):
    

    form = AcompanhamentoDiarioSearchForm(request.POST or None)

    template_name = 'lab/acompanhamento_diario.html'
    
    if form.is_valid():
        instance = form.save(commit=False)
        
    
    context = {
        "form": form,
    }


    return render(request, template_name, context)

# @login_required
# def acompanhamento_diario_filter(request):
    

#     form = AcompanhamentoDiarioSearchForm(request.POST or None)

#     template_name = 'lab/acompanhamento_diario.html'
    
#     if form.is_valid():
#         instance = form.save(commit=False)
#         data_i = instance.data_inicio
#         hora_i = instance.hora_inicio
#         data_f = instance.data_fim
#         hora_f = instance.hora_fim
#         return redirect('producao:qualidade_home')
    
#     context = {
#         "form": form,
#     }


#     return render(request, template_name, context)



    
@login_required
def qualidade_home(request):
    template_name = 'lab/qualidade_home.html'
    context = {}

    return render(request, template_name, context)



@login_required
def retrabalho_v2(request, pk):
    instance = get_object_or_404(Bobinagem, pk=pk)
    form = RetrabalhoFormEmendas(request.POST or None)
    template_name = "retrabalho/retrabalho_create_v2.html"

    if form.is_valid():
        b_1 = form.cleaned_data['bobine_1']
        b_2 = form.cleaned_data['bobine_2']
        b_3 = form.cleaned_data['bobine_3']
        m_b_1 = form.cleaned_data['m_bobine_1']
        m_b_2 = form.cleaned_data['m_bobine_2']
        m_b_3 = form.cleaned_data['m_bobine_3']

        if b_1 and b_2 and b_3 and m_b_1 and m_b_2 and m_b_3:
            if Bobine.objects.filter(nome=b_1) and Bobine.objects.filter(nome=b_2) and Bobine.objects.filter(nome=b_3):
                b_1 = get_object_or_404(Bobine, nome=b_1)
                b_2 = get_object_or_404(Bobine, nome=b_2)
                b_3 = get_object_or_404(Bobine, nome=b_3)
                comp_actual_1 = b_1.comp_actual
                comp_actual_2 = b_2.comp_actual
                comp_actual_3 = b_3.comp_actual
               
                if comp_actual_1 >= m_b_1 and comp_actual_2 >= m_b_2 and comp_actual_3 >= m_b_3 and b_1.estado == 'DM' and b_2.estado == 'DM' and b_3.estado == 'DM':
                    if b_1 == b_2 == b_3:
                        comp_total = m_b_1 + m_b_2 + m_b_3
                        dif = comp_total - b_1.comp_actual
                        if comp_total > b_1.comp_actual:
                            messages.error(request, 'A bobine ' + b_1.nome + ' não tem metros suficentes para efectuar esta operação. O valor que introduziu excede o comprimento atual da bobine em ' + str(dif) + ' m.') 
                        else:
                            return redirect('producao:retrabalho_confirmacao', pk=pk, b1=b_1.pk, m1=m_b_1, b2=b_2.pk, m2=m_b_2, b3=b_3.pk, m3=m_b_3)

                    elif b_1 == b_2:
                        comp_total = m_b_1 + m_b_2
                        dif = comp_total - b_1.comp_actual
                        if comp_total > b_1.comp_actual:
                            messages.error(request, 'A bobine ' + b_1.nome + ' não tem metros suficentes para efectuar esta operação. O valor que introduziu excede o comprimento atual da bobine em ' + str(dif) + ' m.') 
                        else:
                            return redirect('producao:retrabalho_confirmacao', pk=pk, b1=b_1.pk, m1=m_b_1, b2=b_2.pk, m2=m_b_2, b3=b_3.pk, m3=m_b_3)
                    
                    elif b_1 == b_3:
                        comp_total = m_b_1 + m_b_3
                        dif = comp_total - b_1.comp_actual
                        if comp_total > b_1.comp_actual:
                            messages.error(request, 'A bobine ' + b_1.nome + ' não tem metros suficentes para efectuar esta operação. O valor que introduziu excede o comprimento atual da bobine em ' + str(dif) + ' m.') 
                        else:
                            return redirect('producao:retrabalho_confirmacao', pk=pk, b1=b_1.pk, m1=m_b_1, b2=b_2.pk, m2=m_b_2, b3=b_3.pk, m3=m_b_3)

                    elif b_2 == b_3:
                        comp_total = m_b_2 + m_b_3
                        dif = comp_total - b_2.comp_actual
                        if comp_total > b_2.comp_actual:
                            messages.error(request, 'A bobine ' + b_2.nome + ' não tem metros suficentes para efectuar esta operação. O valor que introduziu excede o comprimento atual da bobine em ' + str(dif) + ' m.') 
                        else:
                            return redirect('producao:retrabalho_confirmacao', pk=pk, b1=b_1.pk, m1=m_b_1, b2=b_2.pk, m2=m_b_2, b3=b_3.pk, m3=m_b_3)
                    else:
                        return redirect('producao:retrabalho_confirmacao', pk=pk, b1=b_1.pk, m1=m_b_1, b2=b_2.pk, m2=m_b_2, b3=b_3.pk, m3=m_b_3)
                        
                                                  

                    
                else:
                    if b_1.estado != 'DM':
                        messages.error(request, 'A bobine ' + b_1.nome + ' não pode ser usada para retrabalho porque o seu estado é ' + b_1.estado + '. Para poder ser retrabalhada o seu estado deverá ser DM.')

                    if b_2.estado != 'DM':
                        messages.error(request, 'A bobine ' + b_2.nome + ' não pode ser usada para retrabalho porque o seu estado é ' + b_2.estado + '. Para poder ser retrabalhada o seu estado deverá ser DM.')

                    if b_3.estado != 'DM':
                        messages.error(request, 'A bobine ' + b_3.nome + ' não pode ser usada para retrabalho porque o seu estado é ' + b_3.estado + '. Para poder ser retrabalhada o seu estado deverá ser DM.')

                    if comp_actual_1 < m_b_1:
                        dif = m_b_1 - comp_actual_1
                        messages.error(request, 'A bobine ' + b_1.nome + ' não tem metros suficentes para efectuar esta operação. O valor que introduziu excede o comprimento atual da bobine em ' + str(dif) + ' m.')
                    
                    if comp_actual_2 < m_b_2:
                        dif = m_b_2 - comp_actual_2 
                        messages.error(request, 'A bobine ' + b_2.nome + ' não tem metros suficentes para efectuar esta operação. O valor que introduziu excede o comprimento atual da bobine em ' + str(dif) + ' m.')

                    if comp_actual_3 < m_b_3:
                        dif = m_b_3 - comp_actual_3
                        messages.error(request, 'A bobine ' + b_3.nome + ' não tem metros suficentes para efectuar esta operação. O valor que introduziu excede o comprimento atual da bobine em ' + str(dif) + ' m.')

                    

                    
                    
            else:
                if not Bobine.objects.filter(nome=b_1):
                    messages.error(request, 'A bobine ' + b_1 + ' não existe.')
                if not Bobine.objects.filter(nome=b_2):
                    messages.error(request, 'A bobine ' + b_2 + ' não existe.')
                if not Bobine.objects.filter(nome=b_3):
                    messages.error(request, 'A bobine ' + b_2 + ' não existe.')
        
        elif b_1 and b_2 and m_b_1 and m_b_2:
            if Bobine.objects.filter(nome=b_1) and Bobine.objects.filter(nome=b_2):
                b_1 = get_object_or_404(Bobine, nome=b_1)
                b_2 = get_object_or_404(Bobine, nome=b_2)
               
                comp_actual_1 = b_1.comp_actual
                comp_actual_2 = b_2.comp_actual
                
               
                if comp_actual_1 >= m_b_1 and comp_actual_2 >= m_b_2 and b_1.estado == 'DM' and b_2.estado == 'DM':
                    if b_1 == b_2:
                        comp_total = m_b_1 + m_b_2
                        dif = comp_total - b_1.comp_actual
                        if comp_total > b_1.comp_actual:
                            messages.error(request, 'A bobine ' + b_1.nome + ' não tem metros suficentes para efectuar esta operação. O valor que introduziu excede o comprimento atual da bobine em ' + str(dif) + ' m.') 
                        else:
                            return redirect('producao:retrabalho_confirmacao', pk=pk, b1=b_1.pk, m1=m_b_1, b2=b_2.pk, m2=m_b_2, b3=None, m3=None)
                    else:
                        return redirect('producao:retrabalho_confirmacao', pk=pk, b1=b_1.pk, m1=m_b_1, b2=b_2.pk, m2=m_b_2, b3=None, m3=None)
                        
                    
                else:
                    if b_1.estado != 'DM':
                        messages.error(request, 'A bobine ' + b_1.nome + ' não pode ser usada para retrabalho porque o seu estado é ' + b_1.estado + '. Para poder ser retrabalhada o seu estado deverá ser DM.')

                    if b_2.estado != 'DM':
                        messages.error(request, 'A bobine ' + b_2.nome + ' não pode ser usada para retrabalho porque o seu estado é ' + b_2.estado + '. Para poder ser retrabalhada o seu estado deverá ser DM.')

                    if comp_actual_1 < m_b_1:
                        dif = m_b_1 - comp_actual_1
                        messages.error(request, 'A bobine ' + b_1.nome + ' não tem metros suficentes para efectuar esta operação. O valor que introduziu excede o comprimento atual da bobine em ' + str(dif) + ' m.')
                    
                    if comp_actual_2 < m_b_2:
                        dif = m_b_2 - comp_actual_2 
                        messages.error(request, 'A bobine ' + b_2.nome + ' não tem metros suficentes para efectuar esta operação. O valor que introduziu excede o comprimento atual da bobine em ' + str(dif) + ' m.')
            
                    
               
                
            else:
                if not Bobine.objects.filter(nome=b_1):
                    messages.error(request, 'A bobine ' + b_1 + ' não existe.')
                if not Bobine.objects.filter(nome=b_2):
                    messages.error(request, 'A bobine ' + b_2 + ' não existe.')
        
        elif b_1 and m_b_1:
            if Bobine.objects.filter(nome=b_1):
                b_1 = get_object_or_404(Bobine, nome=b_1)
                comp_actual_1 = b_1.comp_actual
                              
                if comp_actual_1 >= m_b_1 and b_1.estado == 'DM':
                    return redirect('producao:retrabalho_confirmacao', pk=pk, b1=b_1.pk, m1=m_b_1, b2=None, m2=None, b3=None, m3=None)
                                   
                else:
                    if b_1.estado != 'DM':
                        messages.error(request, 'A bobine ' + b_1.nome + ' não pode ser usada para retrabalho porque o seu estado é ' + b_1.estado + '. Para poder ser retrabalhada o seu estado deverá ser DM.')
                        
                    if comp_actual_1 < m_b_1:
                        dif = m_b_1 - comp_actual_1
                        messages.error(request, 'A bobine ' + b_1.nome + ' não tem metros suficentes para efectuar esta operação. O valor que introduziu excede o comprimento atual da bobine em ' + str(dif) + ' m.')

                    

                    
                               
            else:
                if not Bobine.objects.filter(nome=b_1):
                    messages.error(request, 'A bobine ' + b_1 + ' não existe.')
                
    context = {
        "form": form, 
        "instance": instance,
        }
    return render(request, template_name, context)

@login_required
def retrabalho_confirmacao(request, pk, b1, m1, b2=None, m2=None, b3=None, m3=None):
    bobinagem = get_object_or_404(Bobinagem, pk=pk)
    bobines = Bobine.objects.filter(bobinagem=bobinagem)
    form = ConfirmReciclarForm(request.POST or None)
    m_1 = m1
    m_2 = m2
    m_3 = m3
        
    try:
        b_3 = Bobine.objects.get(pk=b3)
    except:
        b_3 = "N/A"
        m_3 = "N/A"

    try:
        b_2 = Bobine.objects.get(pk=b2)
    except:
        b_2 = "N/A"
        m_2 = "N/A"
        
    b_1 = get_object_or_404(Bobine, pk=b1)

    comp_total = comp_dm(b_1, m_1, b_2, m_2, b_3, m_3)
    area_total = Decimal(comp_total) * (Decimal(bobinagem.perfil.largura_bobinagem) * Decimal(0.001))
    area_total = round(area_total,2)

    area_bobines = []
    for b in bobines:
        area_bobines.append(round(Decimal(comp_total) * (Decimal(b.largura.largura) * Decimal(0.001)), 2))


    if b_3 != "N/A" and b_2 != "N/A":
        e_1 = m_1
        e_2 = int(m_1) + int(m_2)
        e_3 = int(m_1) + int(m_2) + int(m_3)
        if b_1 == b_2 == b_3:
            mr_1 = int(b_1.comp_actual) - int(m_1) - int(m_2) - int(m_3)
            mr_2 = mr_1
            mr_3 = mr_1
        elif b_1 == b_2 != b_3:
            mr_1 = int(b_1.comp_actual) - int(m_1) - int(m_2)
            mr_2 = mr_1
            mr_3 = int(b_3.comp_actual) - int(m_3)
        elif b_1 == b_3 != b_2:
            mr_1 = int(b_1.comp_actual) - int(m_1) - int(m_3)
            mr_3 = mr_1
            mr_2 = int(b_2.comp_actual) - int(m_2)
        elif b_2 == b_3 != b_1:
            mr_1 =  int(b_1.comp_actual) - int(m_1)
            mr_2 =  int(b_2.comp_actual) - int(m_2) - int(m_3)
            mr_3 =  mr_2
        else:
            mr_1 =  int(b_1.comp_actual) - int(m_1)
            mr_2 =  int(b_2.comp_actual) - int(m_2)
            mr_3 =  int(b_3.comp_actual) - int(m_3)
    elif b_2 != "N/A" and b_3 == "N/A":
        e_1 = m_1
        e_2 = int(m_1) + int(m_2)
        e_3 = "N/A"
        if b_1 == b_2:
            mr_1 = int(b_1.comp_actual) - int(m_1) - int(m_2)
            mr_2 = mr_1
            mr_3 = "N/A"
        else:
            mr_1 = int(b_1.comp_actual) - int(m_1)
            mr_2 = int(b_2.comp_actual) - int(m_2)
            mr_3 = "N/A"

    else:
        e_1 = m_1
        mr_1 = int(b_1.comp_actual) - int(m_1)
        e_2 = "N/A"
        e_3 = "N/A"
        mr_2 = "N/A"
        mr_3 = "N/A"
    
    if form.is_valid():
        recycle_1 = form.cleaned_data['recycle_1']
        recycle_2 = form.cleaned_data['recycle_2']
        recycle_3 = form.cleaned_data['recycle_3']
        
        if b_1 != "N/A" and b_3 != "N/A" and b_2 != "N/A":
              
            emenda_1 = Emenda.objects.create(bobinagem=bobinagem, bobine=b_1, num_emenda=1, emenda=e_1, metros=m_1)
            emenda_2 = Emenda.objects.create(bobinagem=bobinagem, bobine=b_2, num_emenda=2, emenda=e_2, metros=m_2)
            emenda_3 = Emenda.objects.create(bobinagem=bobinagem, bobine=b_3, num_emenda=3, emenda=e_3, metros=m_3)

            bobinagem.num_emendas = 3
            bobinagem.comp = e_3
            bobinagem.comp_par = e_3
            bobinagem.comp_cli = e_3
            bobinagem.area = round(Decimal(e_3) * (Decimal(bobinagem.perfil.largura_bobinagem) * Decimal(0.001)), 2)
            bobinagem.area_g = bobinagem.area
            bobinagem.estado = 'G'
            bobinagem.save()
            b_1.comp_actual = mr_1
            b_2.comp_actual = mr_2
            b_3.comp_actual = mr_3
            b_1.save()
            b_2.save()
            b_3.save()
            # retrabalho_nome(bobinagem.pk, 3)
            data = bobinagem.data
            data = data.strftime('%Y%m%d')
            map(int, data)
            if bobinagem.num_bobinagem < 10:
                bobinagem.nome = '3%s-0%s' % (data[1:], bobinagem.num_bobinagem)
            else:
                bobinagem.nome = '3%s-%s' % (data[1:], bobinagem.num_bobinagem)
            bobinagem.save()    
            for b in bobines:
                if b.largura.num_bobine < 10:
                    b.nome = '%s-0%s' % (bobinagem.nome, b.largura.num_bobine)
                else:
                    b.nome = '%s-%s' % (bobinagem.nome, b.largura.num_bobine)
                b.save() 

        elif b_1 != "N/A" and b_2 != "N/A":
            emenda_1 = Emenda.objects.create(bobinagem=bobinagem, bobine=b_1, num_emenda=1, emenda=e_1, metros=m_1)
            emenda_2 = Emenda.objects.create(bobinagem=bobinagem, bobine=b_2, num_emenda=2, emenda=e_2, metros=m_2)
            bobinagem.num_emendas = 2
            bobinagem.comp = e_2
            bobinagem.comp_par = e_2
            bobinagem.comp_cli = e_2
            bobinagem.area = round(Decimal(e_2) * (Decimal(bobinagem.perfil.largura_bobinagem) * Decimal(0.001)), 2)
            bobinagem.area_g = bobinagem.area
            bobinagem.estado = 'G'
            bobinagem.save()
            b_1.comp_actual = mr_1
            b_2.comp_actual = mr_2
            b_1.save()
            b_2.save()
            
            # retrabalho_nome(bobinagem.pk, 2)
            data = bobinagem.data
            data = data.strftime('%Y%m%d')
            map(int, data)
            if bobinagem.num_bobinagem < 10:
                bobinagem.nome = '3%s-0%s' % (data[1:], bobinagem.num_bobinagem)
            else:
                bobinagem.nome = '3%s-%s' % (data[1:], bobinagem.num_bobinagem)
            bobinagem.save()    
            for b in bobines:
                if b.largura.num_bobine < 10:
                    b.nome = '%s-0%s' % (bobinagem.nome, b.largura.num_bobine)
                   
                else:
                    b.nome = '%s-%s' % (bobinagem.nome, b.largura.num_bobine)
                b.save()      

        elif b_1 != "N/A":
            emenda_1 = Emenda.objects.create(bobinagem=bobinagem, bobine=b_1, num_emenda=1, emenda=e_1, metros=m_1)
            bobinagem.num_emendas = 1
            bobinagem.comp = e_1
            bobinagem.comp_par = e_1
            bobinagem.comp_cli = e_1
            bobinagem.area = round(Decimal(e_1) * (Decimal(bobinagem.perfil.largura_bobinagem) * Decimal(0.001)), 2)
            bobinagem.area_g = bobinagem.area
            bobinagem.estado = 'G'
            bobinagem.save()
            b_1.comp_actual = mr_1
            b_1.save()
            
                        
        if recycle_1 == True and b_1 != "N/A":
            b_1.recycle = True
            # palete_1_id = b_1.palete.id
            # print(palete_1_id) 
            # palete1 = Palete.objects.get(id=palete_1_id)
            # print(palete1)
            # palete1.area -= b_1.area
            # palete1.comp_total -= b_1.bobinagem.comp_cli
            # palete1.num_bobines_act -= 1
            # palete1.num_bobines -= 1
            # palete1.save()
            # b_1.palete = None
            b_1.save()
          

        if recycle_2 == True and b_2 != "N/A":
            b_2.recycle = True
            b_2.save()

        if recycle_3 == True and b_3 != "N/A":
            b_3.recycle = True
            b_3.save()

        for bob in bobines:
            bob.comp_actual = bobinagem.comp_cli
            bob.area = round(Decimal(bobinagem.comp_cli) * (Decimal(bob.largura.largura) * Decimal(0.001)), 2)
            bob.estado = 'G'
            bob.save()
                   

        return redirect('producao:finalizar_retrabalho', pk=bobinagem.pk)
          
  

    
    template_name = "retrabalho/retrabalho_confirmacao.html"

    context = {
        "bobinagem": bobinagem,
        "bobines": bobines,
        "b_1": b_1,
        "b_2": b_2,
        "b_3": b_3,
        "m_1": m_1,
        "m_2": m_2,
        "m_3": m_3,
        "comp_total": comp_total,
        "area_total": area_total,
        "area_bobines": area_bobines,
        "e_1": e_1,
        "e_2": e_2,
        "e_3": e_3,
        "mr_1": mr_1,
        "mr_2": mr_2,
        "mr_3": mr_3,
        "form": form,
        
        }
    return render(request, template_name, context)

@login_required
def palete_picagem(request, pk):
    palete = get_object_or_404(Palete, pk=pk)
    cliente = palete.cliente
    template_name = 'palete/palete_picagem_v2.html'
    num_bobines = palete.num_bobines
    PicagemBobinesFormSet = formset_factory(PicagemBobines, extra=num_bobines)
    
    if request.method == 'POST':
        formset = PicagemBobinesFormSet(request.POST)
        if formset.is_valid():
            count = 0
            array_bobines = []
            array_cores = []
            array_larguras = []
            array_produtos = []
            validation = True

            #Validação individual
            for f in formset:
                count += 1
                cd = f.cleaned_data
                b = cd.get('bobine')
                
                if b is not None:
                    try:
                        bobine = get_object_or_404(Bobine, nome=b)
                        array_bobines.append(bobine)
                        array_cores.append(bobine.bobinagem.perfil.core)
                        array_larguras.append(bobine.largura.largura)
                        array_produtos.append(bobine.largura.designacao_prod)

                        if bobine.estado != 'G' and bobine.estado != 'LAB':
                            messages.error(request, '(' + str(count) + ') A bobine ' + bobine.nome + ' não está em estado GOOD ou LAB.')
                            validation = False

                        if bobine.palete:
                            p_b = get_object_or_404(Palete, pk = bobine.palete.pk)
                            if p_b.estado == 'G':
                                messages.error(request, '(' + str(count) + ') A bobine ' + bobine.nome + ' encontra-se noutra palete GOOD.')
                                validation = False
                            

                        if bobine.bobinagem.diam > cliente.limsup:
                            messages.error(request, '(' + str(count) + ') O diâmetro da bobine ' + bobine.nome + ' é superior ao limite máximo aceite pelo cliente ' + cliente.nome + '.') 
                            validation = False
                        elif bobine.bobinagem.diam > cliente.limsup:
                            messages.error(request, '(' + str(count) + ') O diâmetro da bobine ' + bobine.nome + ' é inferior ao limite mínimo aceite pelo cliente ' + cliente.nome + '.') 
                            validation = False

                        if bobine.largura.largura != palete.largura_bobines:
                            messages.error(request, '(' + str(count) + ') A largura de ' + bobine.nome +  ' (' + str(bobine.largura.largura) + ' mm) não corresponde a largura definida na palete de ' + str(palete.largura_bobines) + ' mm.') 
                            validation = False

                        if bobine.bobinagem.perfil.core != palete.core_bobines:
                            messages.error(request, '(' + str(count) + ') O core da ' + bobine.nome +  ' (' + str(bobine.bobinagem.perfil.core) + '") não corresponde ao core definido na palete de ' + str(palete.core_bobines) + '".') 
                            validation = False
                
                    except:
                        messages.error(request, '(' + str(count) + ') A bobine ' + b + ' não existe.')
                        validation = False
                        
                else:
                    messages.error(request, '(' + str(count) + ') Por favor preencha a campo nº ' + str(count) + '.')
                    validation = False
            
            #Validação global -> remover validação global de core e largura
            
            if len(array_bobines) == palete.num_bobines and validation == True:
                if len(array_bobines) > len(set(array_bobines)):
                    messages.error(request, 'A picagem contem bobines repetidas.')
                elif len(set(array_produtos))!=1:
                    messages.error(request, 'As bobines picadas são produtos diferentes. Para que a palete seja válida todas as bobines têm de ser o mesmo produto.')
                else:
                    c = 0
                    area_sum = 0
                    comp_total = 0

                    for y in array_bobines:
                        y_b = get_object_or_404(Bobine, nome=y)
                        if y_b.palete:
                            y_p = get_object_or_404(Palete, pk = y_b.palete.pk)
                            if y_p.estado == 'DM':
                                y_p.area -= Decimal(y_b.area) 
                                y_p.comp_total -= Decimal(y_b.bobinagem.comp_cli)
                                y_p.num_bobines -= 1
                                y_p.num_bobines_act -= 1
                                y_p.save()

                    for ab in array_bobines:
                        c += 1
                        bob = get_object_or_404(Bobine, nome=ab)
                        bob.palete = palete
                        bob.posicao_palete = c
                        area_sum += bob.area
                        comp_total += bob.bobinagem.comp_cli 
                        bob.save()

                    e_p = EtiquetaPalete.objects.get(palete=palete)       
                    for x in array_bobines:
                        bobine = Bobine.objects.get(nome=x)
                        if bobine.bobinagem.perfil.retrabalho == True:
                            ano = palete.data_pal
                            ano = ano.strftime('%Y')
                            num = palete.num
                            if num < 10:    
                                palete.nome = 'R000%s-%s' % (num, ano)  
                            elif num < 100:
                                palete.nome = 'R00%s-%s' % (num, ano)
                            elif num < 1000: 
                                palete.nome = 'R0%s-%s' % (num, ano)
                            else: 
                                palete.nome = 'R%s-%s' % (num, ano)
                            palete.save()
                            e_p.palete_nome = palete.nome
                            break

                    


                    palete.num_bobines_act = c
                    palete.area = area_sum
                    palete.comp_total = comp_total
                    palete.save()

                    
                    bobines = Bobine.objects.filter(palete=palete)
                    bobines_nome = []
                    d_min = 0
                    d_max = 0
                    bobine_posicao = [None] * 61
                                        
                    for bn in bobines:
                        bobines_nome.append(bn.nome)
                        d = bn.bobinagem.diam
                        pos = bn.posicao_palete
                        bobine_posicao[pos] = bn.nome
                        if d_min == 0 and d_max == 0: 
                            d_min = d
                            d_max = d
                        elif d <= d_min:
                            d_min = d
                        elif d >= d_max:
                            d_max = d

                    bobine_produto = Bobine.objects.get(nome=bobines_nome[0])
                    e_p.produto = bobine_produto.largura.designacao_prod
                    
                    e_p.bobine1 = bobine_posicao[1]
                    e_p.bobine2 = bobine_posicao[2]
                    e_p.bobine3 = bobine_posicao[3]
                    e_p.bobine4 = bobine_posicao[4]
                    e_p.bobine5 = bobine_posicao[5]
                    e_p.bobine6 = bobine_posicao[6]
                    e_p.bobine7 = bobine_posicao[7]
                    e_p.bobine8 = bobine_posicao[8]
                    e_p.bobine9 = bobine_posicao[9]
                    e_p.bobine10 = bobine_posicao[10]
                    e_p.bobine11 = bobine_posicao[11]
                    e_p.bobine12 = bobine_posicao[12]
                    e_p.bobine13 = bobine_posicao[13]
                    e_p.bobine14 = bobine_posicao[14]
                    e_p.bobine15 = bobine_posicao[15]
                    e_p.bobine16 = bobine_posicao[16]
                    e_p.bobine17 = bobine_posicao[17]
                    e_p.bobine18 = bobine_posicao[18]
                    e_p.bobine19 = bobine_posicao[19]
                    e_p.bobine20 = bobine_posicao[20]
                    e_p.bobine21 = bobine_posicao[21]
                    e_p.bobine22 = bobine_posicao[22]
                    e_p.bobine23 = bobine_posicao[23]
                    e_p.bobine24 = bobine_posicao[24]
                    e_p.bobine25 = bobine_posicao[25]
                    e_p.bobine26 = bobine_posicao[26]
                    e_p.bobine27 = bobine_posicao[27]
                    e_p.bobine28 = bobine_posicao[28]
                    e_p.bobine29 = bobine_posicao[29]
                    e_p.bobine30 = bobine_posicao[30]
                    e_p.bobine31 = bobine_posicao[31]
                    e_p.bobine32 = bobine_posicao[32]
                    e_p.bobine33 = bobine_posicao[33]
                    e_p.bobine34 = bobine_posicao[34]
                    e_p.bobine35 = bobine_posicao[35]
                    e_p.bobine36 = bobine_posicao[36]
                    e_p.bobine37 = bobine_posicao[37]
                    e_p.bobine38 = bobine_posicao[38]
                    e_p.bobine39 = bobine_posicao[39]
                    e_p.bobine40 = bobine_posicao[40]
                    e_p.bobine41 = bobine_posicao[41]
                    e_p.bobine42 = bobine_posicao[42]
                    e_p.bobine43 = bobine_posicao[43]
                    e_p.bobine44 = bobine_posicao[44]
                    e_p.bobine45 = bobine_posicao[45]
                    e_p.bobine46 = bobine_posicao[46]
                    e_p.bobine47 = bobine_posicao[47]
                    e_p.bobine48 = bobine_posicao[48]
                    e_p.bobine49 = bobine_posicao[49]
                    e_p.bobine50 = bobine_posicao[50]
                    e_p.bobine51 = bobine_posicao[51]
                    e_p.bobine52 = bobine_posicao[52]
                    e_p.bobine53 = bobine_posicao[53]
                    e_p.bobine54 = bobine_posicao[54]
                    e_p.bobine55 = bobine_posicao[55]
                    e_p.bobine56 = bobine_posicao[56]
                    e_p.bobine57 = bobine_posicao[57]
                    e_p.bobine58 = bobine_posicao[58]
                    e_p.bobine59 = bobine_posicao[59]
                    e_p.bobine60 = bobine_posicao[60]
                    e_p.diam_min = d_min
                    e_p.diam_max = d_max
                    e_p.save()

                    add_artigo_to_bobine(pk)

                    return redirect('producao:addbobinepalete', pk=palete.pk)




                    # if(len(set(array_larguras))==1):
                    #     if(len(set(array_cores))==1):
                    #         messages.error(request, 'As larguras e os cores condizem')
                    #     else:
                    #         messages.error(request, 'Os cores das bobines picadas não condizem.')
                    # else:
                    #     messages.error(request, 'As larguras das bobines picadas não condizem.')
               
    else:
        formset = PicagemBobinesFormSet()
    
    
    context = {
        "palete": palete,
        "formset": formset
        }
    return render(request, template_name, context)



@login_required    
def classificacao_bobines_v2(request, pk):
    bobinagem = get_object_or_404(Bobinagem, pk=pk)
    bobines = Bobine.objects.filter(bobinagem=bobinagem)
    template_name = 'producao/classificacao_bobines_v2.html'
    

    # ClassificacaoBobinesFormSet = modelformset_factory(Bobine, fields=('estado', ))
    ClassificacaoBobinesFormSet = inlineformset_factory(Bobinagem, Bobine, fields=('nome', 'estado', 'con', 'descen', 'presa', 'diam_insuf', 'furos', 'estado', 'buraco', 'esp', 'troca_nw', 'outros', 'obs', 'l_real', ), extra=0, can_delete=False)
    
    
    if request.method == 'POST':
        # formset = ClassificacaoBobinesFormSet(request.POST, queryset=Bobine.objects.filter(bobinagem=bobinagem),)
        formset = ClassificacaoBobinesFormSet(request.POST, instance=bobinagem)
        if formset.is_valid():
        #    instances = formset.save(commit=False)
        #    for instance in instances:
        #        instance.save()
            formset.save()
           
    
    formset = ClassificacaoBobinesFormSet(instance=bobinagem)       
    
    
    
    context = {
        "bobinagem": bobinagem,
        "bobines":bobines,
        "formset": formset
        }
    return render(request, template_name, context)


@login_required
def bobinagem_list_v2(request):
    bobinagens = Bobinagem.objects.filter(perfil__retrabalho=0, data__gt='2018-12-31')
    bobine = Bobine.objects.filter(bobinagem__perfil__retrabalho=0)
    template_name = 'producao/bobinagem_list_v2.html'
    query = request.GET.get("q")
    if query:
        bobinagens = bobinagens.filter(nome__icontains=query)
    context = {
        "bobinagens": bobinagens,
        "bobine": bobine
        
        }
    return render(request, template_name, context)