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
