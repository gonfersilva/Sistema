from producao.models import *

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
    desperdicio(instance.pk) 
    if not instance.perfil.retrabalho == True:
        tempo_duracao(instance.pk)
    area_bobinagem(instance.pk) 
    create_bobine(instance.pk)  
    
     
       

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
    instance.area = largura * instance.bobinagem.comp_cli
    instance.save()

def etiqueta_add_bobine(pk_palete, pk_bobine):
    palete = Palete.objects.get(pk=pk_palete)
    bobine = Bobine.objects.get(pk=pk_bobine)
    e_p = EtiquetaPalete.objects.get(palete=palete)
    bob = [None] * 61
    
    posicao = bobine.posicao_palete
    bob[posicao] = bobine.nome
    if e_p.bobine1 == None or posicao == 1:
        e_p.bobine1 = bob[1]
    elif e_p.bobine2 == None or posicao == 2:    
        e_p.bobine2 = bob[2]
    elif e_p.bobine3 == None or posicao == 3:    
        e_p.bobine3 = bob[3]
    elif e_p.bobine4 == None or posicao == 4:    
        e_p.bobine4 = bob[4]
    elif e_p.bobine5 == None or posicao == 5:    
        e_p.bobine5 = bob[5]
    elif e_p.bobine6 == None or posicao == 6:  
        e_p.bobine6 = bob[6]
    elif e_p.bobine7 == None or posicao == 7:  
        e_p.bobine7 = bob[7]
    elif e_p.bobine8 == None or posicao == 8:  
        e_p.bobine8 = bob[8]
    elif e_p.bobine9 == None or posicao == 9:      
        e_p.bobine9 = bob[9]
    elif e_p.bobine10 == None or posicao == 10:  
        e_p.bobine10 = bob[10]
    elif e_p.bobine11 == None or posicao == 11: 
        e_p.bobine11 = bob[11]
    elif e_p.bobine12 == None or posicao == 12: 
        e_p.bobine12 = bob[12]
    elif e_p.bobine13 == None or posicao == 13: 
        e_p.bobine13 = bob[13]
    elif e_p.bobine14 == None or posicao == 14:     
        e_p.bobine14 = bob[14]
    elif e_p.bobine15 == None or posicao == 15: 
        e_p.bobine15 = bob[15]
    elif e_p.bobine16 == None or posicao == 16: 
        e_p.bobine16 = bob[16]
    elif e_p.bobine17 == None or posicao == 17: 
        e_p.bobine17 = bob[17]
    elif e_p.bobine18 == None or posicao == 18: 
        e_p.bobine18 = bob[18]
    elif e_p.bobine19 == None or posicao == 19: 
        e_p.bobine19 = bob[19]
    elif e_p.bobine20 == None or posicao == 20: 
        e_p.bobine20 = bob[20]
    elif e_p.bobine21 == None or posicao == 21: 
        e_p.bobine21 = bob[21]
    elif e_p.bobine22 == None or posicao == 22: 
        e_p.bobine22 = bob[22]
    elif e_p.bobine23 == None or posicao == 23: 
        e_p.bobine23 = bob[23]
    elif e_p.bobine24 == None or posicao == 24: 
        e_p.bobine24 = bob[24]
    elif e_p.bobine25 == None or posicao == 25: 
        e_p.bobine25 = bob[25]
    elif e_p.bobine26 == None or posicao == 26: 
        e_p.bobine26 = bob[26]
    elif e_p.bobine27 == None or posicao == 27: 
        e_p.bobine27 = bob[27]
    elif e_p.bobine28 == None or posicao == 28: 
        e_p.bobine28 = bob[28]
    elif e_p.bobine29 == None or posicao == 29: 
        e_p.bobine29 = bob[29]
    elif e_p.bobine30 == None or posicao == 30: 
        e_p.bobine30 = bob[30]
    elif e_p.bobine31 == None or posicao == 31: 
        e_p.bobine31 = bob[31]
    elif e_p.bobine32 == None or posicao == 32: 
        e_p.bobine32 = bob[32]
    elif e_p.bobine33 == None or posicao == 33: 
        e_p.bobine33 = bob[33]
    elif e_p.bobine34 == None or posicao == 34:
        e_p.bobine34 = bob[34]
    elif e_p.bobine35 == None or posicao == 35:
        e_p.bobine35 = bob[35]
    elif e_p.bobine36 == None or posicao == 36:
        e_p.bobine36 = bob[36]
    elif e_p.bobine37 == None or posicao == 37:
        e_p.bobine37 = bob[37]
    elif e_p.bobine38 == None or posicao == 38:
        e_p.bobine38 = bob[38]
    elif e_p.bobine39 == None or posicao == 39:
        e_p.bobine39 = bob[39]
    elif e_p.bobine40 == None or posicao == 40:
        e_p.bobine40 = bob[40]
    elif e_p.bobine41 == None or posicao == 41:
        e_p.bobine41 = bob[41]
    elif e_p.bobine42 == None or posicao == 42:
        e_p.bobine42 = bob[42]
    elif e_p.bobine43 == None or posicao == 43:
        e_p.bobine43 = bob[43]
    elif e_p.bobine44 == None or posicao == 44:
        e_p.bobine44 = bob[44]
    elif e_p.bobine45 == None or posicao == 45:
        e_p.bobine45 = bob[45]
    elif e_p.bobine46 == None or posicao == 46:
        e_p.bobine46 = bob[46]
    elif e_p.bobine47 == None or posicao == 47:
        e_p.bobine47 = bob[47]
    elif e_p.bobine48 == None or posicao == 48:
        e_p.bobine48 = bob[48]
    elif e_p.bobine49 == None or posicao == 49:
        e_p.bobine49 = bob[49]
    elif e_p.bobine50 == None or posicao == 50:
        e_p.bobine50 = bob[50]
    elif e_p.bobine51 == None or posicao == 51:
        e_p.bobine51 = bob[51]
    elif e_p.bobine52 == None or posicao == 52:
        e_p.bobine52 = bob[52]
    elif e_p.bobine53 == None or posicao == 53:
        e_p.bobine53 = bob[53]
    elif e_p.bobine54 == None or posicao == 54:
        e_p.bobine54 = bob[54]
    elif e_p.bobine55 == None or posicao == 55:
        e_p.bobine55 = bob[55]
    elif e_p.bobine56 == None or posicao == 56:
        e_p.bobine56 = bob[56]
    elif e_p.bobine57 == None or posicao == 57:
        e_p.bobine57 = bob[57]
    elif e_p.bobine58 == None or posicao == 58:
        e_p.bobine58 = bob[58]
    elif e_p.bobine59 == None or posicao == 59:
        e_p.bobine59 = bob[59]
    elif e_p.bobine60 == None or posicao == 60:
        e_p.bobine60 = bob[60]
    
    e_p.save()

