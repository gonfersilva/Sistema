from .models import Perfil, Largura, Bobinagem, Bobine, Palete, Emenda, Cliente,EtiquetaRetrabalho
from django.contrib import admin

admin.site.register(Palete)
admin.site.register(Perfil)
admin.site.register(Largura)
admin.site.register(Bobinagem)
admin.site.register(Bobine)
admin.site.register(Emenda)
admin.site.register(Cliente)
admin.site.register(EtiquetaRetrabalho)

