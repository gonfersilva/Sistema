from .models import Perfil, Largura, Bobinagem, Bobine, Palete, Emenda, Cliente, EtiquetaRetrabalho, EtiquetaPalete, Encomenda, Carga, EtiquetaFinal
from django.contrib import admin


admin.site.register(Perfil)
admin.site.register(Largura)


admin.site.register(Emenda)
admin.site.register(Cliente)
admin.site.register(EtiquetaRetrabalho)
admin.site.register(EtiquetaPalete)
admin.site.register(Encomenda)
admin.site.register(Carga)
admin.site.register(EtiquetaFinal)

class BobinagemAdmin(admin.ModelAdmin):
    search_fields = ['nome']

class BobineAdmin(admin.ModelAdmin):
    search_fields = ['nome']

class PaleteAdmin(admin.ModelAdmin):
    search_fields = ['nome']

admin.site.register(Bobinagem, BobinagemAdmin)
admin.site.register(Bobine, BobineAdmin)
admin.site.register(Palete, PaleteAdmin)