from django import template
from producao.forms import PerfilCreateForm, BobinagemCreateForm, PaleteCreateForm, Picagem, RetrabalhoCreateForm, EmendasCreateForm, ClienteCreateForm, UpdateBobineForm, PaleteRetrabalhoForm, ClassificacaoBobines
from producao.models import Perfil, Bobinagem, Emenda, Palete

register = template.Library()

@register.inclusion_tag('perfil/perfil_form.html')
def perfil_form(self):
    form = PerfilCreateForm()
    return {'form': form }

@register.inclusion_tag('producao/bobinagem_form.html')
def bobinagem_form(self):
    form = BobinagemCreateForm()
    return {'form': form }

@register.inclusion_tag('palete/palete_form.html')
def palete_form(self):
    form = PaleteCreateForm()
    return {'form': form }

@register.inclusion_tag('retrabalho/retrabalho_form.html')
def retrabalho_form(self):
     form = RetrabalhoCreateForm()
     return {'form': form }

@register.inclusion_tag('retrabalho/emendas_form.html')
def emendas_form(self):
    form = EmendasCreateForm()
    return {
            'form': form,
            }

@register.inclusion_tag('retrabalho/final_form.html')
def final_form(self):
    form = BobinagemCreateForm()
    return {'form': form }

@register.inclusion_tag('cliente/cliente_form.html')
def cliente_form(self):
    form = ClienteCreateForm()
    return {'form': form }

@register.inclusion_tag('producao/bobine_update_form.html')
def bobine_update_form(self):
    form = UpdateBobineForm(instance=self.instance)
    return {'form': form, "instance": self.instance}


@register.inclusion_tag('retrabalho/palete_retrabalho_form.html')
def palete_retrabalho_form(self):
    form = PaleteRetrabalhoForm()
    return {'form': form }

# @register.inclusion_tag('palete/ordenar_bobines_form.html')
# def ordenar_bobines_form(self):
#     form = OrdenarBobines()
#     return {'form': form }
    
@register.inclusion_tag('producao/classificacao_bobines_form.html')
def classificacao_bobines(self):
    form = ClassificacaoBobines(instance=self.bobinagem)
    return {'form': form, "instance": self.bobinagem}