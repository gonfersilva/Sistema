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

        
    

