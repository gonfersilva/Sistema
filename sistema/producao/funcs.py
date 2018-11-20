from .models import *

def areas(pk):
    bobinagem = Bobinagem.objects.get(pk=pk)
    bobine = Bobine.objects.filter(bobinagem=bobinagem)

    area_g = bobinagem.area_g
    area_r = bobinagem.area_r
    area_dm = bobinagem.area_dm
    area_ind = bobinagem.area_ind
    area_ba = bobinagem.area_ba

    for b in bobine:
        estado = b.estado

        if estado == 'G':
            area_g += b.area
        
        elif estado == 'R':
            area_r += b.area
        
        elif estado == 'DM':
            area_dm += b.area

        elif estado == 'IND':
            area_dm += b.area

        elif estado == 'BA':
            area_dm += b.area
    
    bobinagem.area_g = area_g
    bobinagem.area_r = area_r
    bobinagem.area_dm = area_dm
    bobinagem.area_ind = area_ind
    bobinagem.area_ba = area_ba
    bobinagem.save()

def update_areas_bobine(pk, estado):
    bobine = Bobine.objects.get(pk=pk)
    bobinagem = bobine.bobinagem
    estado_anterior = estado
    estado_actual = bobine.estado

    if estado_actual == estado_anterior:
        pass
    elif estado_anterior == 'LAB' or estado_anterior == 'HOLD':
        if estado_actual == 'G':
            bobinagem.area_g += bobine.area
        elif estado_actual == 'DM':
            bobinagem.area_dm += bobine.area
        elif estado_actual == 'R':
            bobinagem.area_r += bobine.area
        elif estado_actual == 'IND':
            bobinagem.area_ind += bobine.area
        elif  estado_actual == 'BA':
            bobinagem.area_ba += bobine.area
    elif estado_anterior == 'G':
        if estado_actual == 'DM':
            bobinagem.area_g -= bobine.area
            bobinagem.area_dm += bobine.area
        elif estado_actual == 'R':
            bobinagem.area_g -= bobine.area
            bobinagem.area_r += bobine.area
        elif estado_actual == 'IND':
            bobinagem.area_g -= bobine.area
            bobinagem.area_ind += bobine.area
        elif estado_actual == 'BA':
            bobinagem.area_g -= bobine.area
            bobinagem.area_ba += bobine.area
    elif estado_anterior == 'DM':
        if estado_actual == 'G':
            bobinagem.area_dm -= bobine.area
            bobinagem.area_g += bobine.area
        elif estado_actual == 'R':
            bobinagem.area_dm -= bobine.area
            bobinagem.area_r += bobine.area
        elif estado_actual == 'IND':
            bobinagem.area_dm -= bobine.area
            bobinagem.area_ind += bobine.area
        elif estado_actual == 'BA':
            bobinagem.area_dm -= bobine.area
            bobinagem.area_ba += bobine.area
    elif estado_anterior == 'R':
        if estado_actual == 'G':
            bobinagem.area_r -= bobine.area
            bobinagem.area_g += bobine.area
        elif estado_actual == 'DM':
            bobinagem.area_r -= bobine.area
            bobinagem.area_dm += bobine.area
        elif estado_actual == 'IND':
            bobinagem.area_r -= bobine.area
            bobinagem.area_ind += bobine.area
        elif estado_actual == 'BA':
            bobinagem.area_r -= bobine.area
            bobinagem.area_ba += bobine.area
    elif estado_anterior == 'IND':
        if estado_actual == 'G':
            bobinagem.area_ind -= bobine.area
            bobinagem.area_g += bobine.area
        elif estado_actual == 'DM':
            bobinagem.area_ind -= bobine.area
            bobinagem.area_dm += bobine.area
        elif estado_actual == 'R':
            bobinagem.area_ind -= bobine.area
            bobinagem.area_r += bobine.area
        elif estado_actual == 'BA':
            bobinagem.area_ind -= bobine.area
            bobinagem.area_ba += bobine.area
    elif estado_anterior == 'BA':
        if estado_actual == 'G':
            bobinagem.area_ba -= bobine.area
            bobinagem.area_g += bobine.area
        elif estado_actual == 'DM':
            bobinagem.area_ba -= bobine.area
            bobinagem.area_dm += bobine.area
        elif estado_actual == 'R':
            bobinagem.area_ba -= bobine.area
            bobinagem.area_r += bobine.area
        elif estado_actual == 'IND':
            bobinagem.area_ba -= bobine.area
            bobinagem.area_ind += bobine.area
    elif estado_actual == 'HOLD' or estado_actual == 'LAB':
        if estado_anterior == 'G':
            bobinagem.area_g += bobine.area
        elif estado_anterior == 'DM':
            bobinagem.area_dm += bobine.area
        elif estado_anterior == 'R':
            bobinagem.area_r += bobine.area
        elif estado_anterior == 'IND':
            bobinagem.area_ind += bobine.area
        
    bobinagem.save()       

        
    
def bobinagem_create(pk):
    instance = Bobinagem.objects.get(pk=pk)
    if not instance.nome:
        data = instance.data
        data = data.strftime('%Y%m%d')
        map(int, data)
        if instance.perfil.retrabalho == True and instance.num_emendas > 0:
            if instance.num_bobinagem < 10:
                # instance.nome = '3%s-0%s' % (data, instance.num_bobinagem)
                instance.nome = '3%s-0%s' % (data[1:], instance.num_bobinagem)

            else:
                instance.nome = '3%s-%s' % (data[1:], instance.num_bobinagem)
        elif instance.perfil.retrabalho == True and instance.num_emendas == 0:
            if instance.num_bobinagem < 10:
                instance.nome = '4%s-0%s' % (data[1:], instance.num_bobinagem)
            else:
                instance.nome = '4%s-%s' % (data[1:], instance.num_bobinagem)
        else:
            if instance.num_bobinagem < 10:
                instance.nome = '%s-0%s' % (data, instance.num_bobinagem)
            else:
                instance.nome = '%s-%s' % (data, instance.num_bobinagem)
     
    instance.save()
    create_bobine(instance.pk)  
    tempo_duracao(instance.pk)
    desperdicio(instance.pk)  
    area_bobinagem(instance.pk)    

def create_bobine(pk):
    instance = Bobinagem.objects.get(pk=pk)
    num = 1
    for i in range(instance.perfil.num_bobines):
        lar = Largura.objects.get(perfil=instance.perfil, num_bobine=num)
        bob = Bobine.objects.filter(bobinagem=instance, largura=lar)
        if not bob:
            bob = Bobine.objects.create(bobinagem=instance, largura=lar, comp_actual=instance.comp)
            if num < 10:
                bob.nome = '%s-0%s' % (instance.nome, num)
            else:
                bob.nome = '%s-%s' % (instance.nome, num)
            if bob.bobinagem.estado == 'R':
                bob.estado = 'R'    
            elif bob.bobinagem.estado == 'DM':
                bob.estado = 'DM'
            elif bob.bobinagem.estado == 'G':
                bob.estado = 'G'
            elif bob.bobinagem.estado == 'BA':
                bob.estado = 'BA'
            elif bob.bobinagem.estado == 'IND':
                bob.estado = 'IND'
            else:
                bob.estado = 'LAB'
            bob.save() 
            area_bobine(bob.pk)
        num += 1
  
    
def tempo_duracao(pk):
    instance = Bobinagem.objects.get(pk=pk)
    if instance.inico or instance.fim:
        if not instance.duracao:
            fim = instance.fim
            fim = fim.strftime('%H:%M')
            inico = instance.inico
            inico = inico.strftime('%H:%M')
            (hf, mf) = fim.split(':')
            (hi, mi) = inico.split(':')
            if hf < hi: 
                result = (int(hf) * 3600 + int(mf) * 60) - (int(hi) * 3600 + int(mi) * 60) + 86400
            else:
                result = (int(hf) * 3600 + int(mf) * 60) - (int(hi) * 3600 + int(mi) * 60) 
            
            result_str = strftime("%H:%M", gmtime(result))
            instance.duracao = result_str
            instance.save()

def area_bobinagem(pk):
    instance = Bobinagem.objects.get(pk=pk)
    largura = instance.perfil.largura_bobinagem / 1000
    instance.area = instance.comp_cli * largura
    instance.save()

def desperdicio(pk):
    instance = Bobinagem.objects.get(pk=pk)
    if instance.comp_par > 0:
        desp = instance.comp - instance.comp_par
        x = instance.comp_par * Decimal('0.05')
        if desp <= x:
            instance.comp_cli = instance.comp
        else:        
            instance.comp_cli = instance.comp_par * Decimal('1.05')
            instance.desper = (instance.comp - instance.comp_cli) / 1000 * instance.perfil.largura_bobinagem
    elif instance.comp_par == 0:
        instance.comp_cli = instance.comp
        instance.desper = 0
    instance.save()

def area_bobine(pk):
    instance = Bobine.objects.get(pk=pk)
    largura = instance.largura.largura / 1000
    instance.area = largura * instance.comp_actual
    instance.save()