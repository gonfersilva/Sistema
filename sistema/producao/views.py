from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy, resolve
from django.forms.models import modelformset_factory
from django import forms
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, redirect, reverse, HttpResponse
from django.views.generic import CreateView
from django.views.generic import ListView, DetailView, CreateView, TemplateView, View, FormView, UpdateView
from .forms import PerfilCreateForm, LarguraForm, BobinagemCreateForm, BobineStatus, PaleteCreateForm, RetrabalhoCreateForm, EmendasCreateForm, ClienteCreateForm, UpdateBobineForm, PaleteRetrabalhoForm, OrdenarBobines, ClassificacaoBobines, RetrabalhoForm
from .models import Largura, Perfil, Bobinagem, Bobine, Palete, Emenda, Cliente, EtiquetaRetrabalho
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

# @login_required
# def perfil_create(request):3
#     template_name = 'perfil/perfil_create.html'
#     context = {}
 
#     return render(request, template_name, context)

class CreatePerfil(LoginRequiredMixin, CreateView):
    template_name = 'perfil/perfil_create.html'
    form_class = PerfilCreateForm
    success_url = '/producao/perfil/{id}/'
     
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

# class BobinagemCreateView(LoginRequiredMixin, CreateView):
#     form_class = BobinagemCreateForm
#     template_name = 'producao/bobinagem_create.html'
#     # success_url = "/producao/bobinagem/"
#     success_url = '/producao/etiqueta/retrabalho/{id}/'

#     def form_valid(self, form):
#         form.instance.user = self.request.user
#         return super().form_valid(form)

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
    bobinagem = Bobinagem.objects.filter(data=now)
    s = request.GET.get("s")
    
    if s:
        bobinagem = Bobinagem.objects.filter(Q(nome__icontains=s) | Q(data__icontains=s))

    # paginator = Paginator(bobinagem, 17)
    # page = request.GET.get('page')
    template_name = 'producao/bobinagem_home.html'
    bobine = Bobine.objects.all()
  

    # try:
    #     bobinagem = paginator.page(page)
    # except PageNotAnInteger:
    #     bobinagem = paginator.page(1)
    # except EmptyPage:
    #     bobinagem = paginator.page(paginator.num_pages)

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
    fields = ['largura', 'designacao_prod']
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
        instance.save()
        
        if EtiquetaPalete.objects.filter(palete=instance).exists():
            return redirect('producao:palete_details', pk=instance.pk)
        else:
            e_p = EtiquetaPalete.objects.create(palete=instance, palete_nome=instance.nome, largura_bobine=instance.largura_bobines)
            e_p.cliente = instance.cliente.nome
            e_p.save()
                
        return redirect('producao:palete_details', pk=instance.pk)

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
        instance.retrabalho = True
        instance.estado = 'DM'
        instance.save()

        if EtiquetaPalete.objects.filter(palete=instance).exists():
            return redirect('producao:addbobinepalete', pk=instance.pk)
        else:
            e_p = EtiquetaPalete.objects.create(palete=instance, palete_nome=instance.nome, largura_bobine=instance.largura_bobines)
            e_p.save()
            return redirect('producao:addbobinepalete', pk=instance.pk)
                
        return redirect('producao:addbobinepalete', pk=instance.pk)

        
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
    # e_p = EtiquetaPalete.objects.get(palete=palete)
    ultima_pos = 0
    for b in bobines:
        ultima_pos += 1
     
    context = {"palete": palete, 
               "bobine": bobine,
               "bobinagem": bobinagem,
            #    "e_p": e_p,
               "ultima_pos": ultima_pos,
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
        data = form['data'].value()
        num_bobinagem = int(form['num_bobinagem'].value())        
        perfil_pk = int(form['perfil'].value())
        perfil = Perfil.objects.get(pk=perfil_pk)
        print(data)
        print(num_bobinagem)
        # print(perfil_pk)
        # print(perfil)
        if Bobinagem.objects.filter(data=data, num_bobinagem=num_bobinagem).exists():
            bobinagem = Bobinagem.objects.filter(data=data, num_bobinagem=num_bobinagem)
            for b in bobinagem:
                if b.perfil.retrabalho == True:
                   messages.error(request, 'A bobinagem que deseja criar já existe. Verifique o nº da bobinagem.')     
                elif not Bobinagem.objects.filter(nome=b.nome).exists():     
                    instance = form.save(commit=False)
                    instance.user = request.user
                    instance.save()
                    bobinagem_create(instance.pk)
                    if not instance.estado == 'LAB' or instance.estado == 'HOLD':
                        areas(instance.pk)
                
                    return redirect('producao:retrabalho_filter', pk=instance.pk)     
        else:
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            bobinagem_create(instance.pk)
            if not instance.estado == 'LAB' or instance.estado == 'HOLD':
                areas(instance.pk)
        
            return redirect('producao:retrabalho_filter', pk=instance.pk)

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
    if request.method == "POST":
        # try:
        #     emenda = Emenda.objects.filter(bobinagem=obj)
        # except Emenda.DoesNotExist:
        #     obj.delete()
        #     if obj.perfil.retrabalho == False:
        #         return redirect('producao:bobinagens')
        #     else:
        #         return redirect('producao:retrabalho_home')

        # obj.delete()
        # if obj.perfil.retrabalho == False:
        #     return redirect('producao:bobinagens')
        # else:
        #     return redirect('producao:retrabalho_home')

        if Emenda.objects.filter(bobinagem=obj).exists():
            emenda = Emenda.objects.filter(bobinagem=obj)
            for e in emenda:
                e.bobine.comp_actual += e.metros
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
        
            
    context = {
        "object": obj,
        "bobine": bobine
    }
    return render(request, "producao/bobinagem_delete.html", context)


@login_required
def palete_delete(request, pk):
    obj = get_object_or_404(Palete, pk=pk)
    bobine = Bobine.objects.filter(palete=obj)
    e_p = EtiquetaPalete.objects.get(palete=obj)
    if request.method == "POST":
        obj.delete()
        e_p.delete()
        if obj.estado == 'G':
            return redirect('producao:paletes')
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
            if bobine.estado == 'LAB':
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
            if bobine.estado == 'LAB':
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
            if bobine.estado == 'LAB':
                bobine.estado = 'DM'
                bobine.save()
            num += 1
        areas(pk)

       
            
    return redirect('producao:bobinagem_list_all')


@login_required
def palete_retrabalho(request):
    palete = Palete.objects.filter(estado='DM')
    paginator = Paginator(palete, 15)
    page = request.GET.get('page')
    template_name = 'palete/palete_retrabalho.html'
    
    try:
        palete = paginator.page(page)
    except PageNotAnInteger:
        palete = paginator.page(1)
    except EmptyPage:
        palete = paginator.page(paginator.num_pages)

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
    paginator = Paginator(bobinagem, 20)
    page = request.GET.get('page')

    try:
        bobinagem = paginator.page(page)
    except PageNotAnInteger:
        bobinagem = paginator.page(1)
    except EmptyPage:
        bobinagem = paginator.page(paginator.num_pages)

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

        b.comp_cli = b.comp
        bobine = Bobine.objects.filter(bobinagem=b.pk)
        for bob in bobine:
            largura = bob.largura.largura
            bob.comp_actual = b.comp_cli
            largura = b.perfil.largura_bobinagem / 1000
            bob.area = largura * b.comp_cli
            cont = 0
            cont += largura
            bob.save()

        b.area = b.comp_cli * cont

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
def palete_list_all(request):
    
    palete = Palete.objects.all()
   
        
    template_name = 'palete/palete_list_all.html'
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
def palete_rabrir(request, pk):
    palete = Palete.objects.get(pk=pk)
    
    bobines = Bobine.objects.filter(palete=palete)
    e_p = EtiquetaPalete.objects.get(palete=palete)
    e_p.diam_min = 0  
    e_p.diam_max = 0  
    
    palete.num_bobines_act = 0
    
    palete.save()
    e_p.save()
    for b in bobines:
        b.palete = None
        b.save()

    return redirect('producao:palete_details', pk=palete.pk)