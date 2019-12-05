from django.conf.urls import url, include
from . import views
from .views import *
from .funcs import *

app_name="producao" 

urlpatterns = [
    
    url(r'^$', producao_home, name='producao_home'),
    url(r'^planeamento/$', planeamento_home, name='planeamento_home'),
    # url(r'^perfil/$', perfil_list, name='perfil'),
    # url(r'^perfil/(?P<pk>\d+)/', perfil_detail, name='perfil_details'),
    # url(r'^perfil/delete/(?P<pk>\d+)/', perfil_delete, name='perfil_delete'),
    # url(r'^perfil/update/(?P<pk>\d+)/', LarguraUpdate.as_view(), name='perfil_update_largura'),
    # url(r'^perfil/create/$', create_perfil, name='perfil_create'),
    url(r'^bobinagem/$', bobinagem_list, name='bobinagens'),
    url(r'^bobinagemlist/$', bobinagem_list_all, name='bobinagem_list_all'),
    url(r'^bobinagem/historico/$', bobinagem_list_all_historico, name='bobinagem_list_all_historico'),
    url(r'^bobinagem/create/$', create_bobinagem, name='bobinagem_create'),
    url(r'^bobinagem/(?P<pk>\d+)/$', bobinagem_status, name='bobinestatus'),
    url(r'^bobinagem/update/(?P<pk>\d+)/', BobinagemUpdate.as_view(), name='bobinagemupdate'),
    url(r'^bobinagem/delete/(?P<pk>\d+)/', bobinagem_delete, name='bobinagem_delete'),
    url(r'^bobinagem/(?P<operation>.+)/(?P<pk>\d+)/', status_bobinagem, name='bobinagem_status'),
    url(r'^bobine/(?P<pk>\d+)/', update_bobine, name='bobineupdate'),
    url(r'^bobine/details/(?P<pk>\d+)/', bobine_details, name='bobine_details'),
    url(r'^palete/$', pelete_list, name='paletes'),
    url(r'^paletelist/$', palete_list_all, name='palete_list_all'),
    url(r'^paletelist/historico/$', palete_list_all_historico, name='palete_list_all_historico'),
    url(r'^palete/retrabalho/$', palete_retrabalho, name='paletes_retrabalho'),
    url(r'^palete/create/$', create_palete, name='palete_create'),
    url(r'^palete/createretrabalho/$', create_palete_retrabalho, name='palete_create_retrabalho'),
    url(r'^palete/(?P<pk>\d+)/$', add_bobine_palete, name='addbobinepalete'),
    url(r'^palete/delete/(?P<pk>\d+)/$', palete_delete, name='palete_delete'),
    url(r'^palete/(?P<pk>\d+)/(?P<e>\d+)/$', add_bobine_palete_erro, name='addbobinepaleteerro'),
    url(r'^palete/(?P<pk>\d+)/picagem/$', picagem, name='picagem'),
    url(r'^palete/details/(?P<pk>\d+)/$', palete_details, name='palete_details'),
    url(r'^palete/(?P<operation>.+)/(?P<pk_bobine>\d+)/(?P<pk_palete>\d+)/$', palete_change, name='paletebobine'),
    url(r'^retrabalho/$', retrabalho_home, name='retrabalho_home'),
    url(r'^retrabalho/retrabalhar/$', retrabalho, name='retrabalho'),
    url(r'^retrabalho/filter/(?P<pk>\d+)/$', picagem_retrabalho, name='retrabalho_filter'),
    url(r'^retrabalho/filter/(?P<pk_bobinagem>\d+)/(?P<pk_bobine>\d+)/$', destruir_bobine, name='destruir_bobine'),
    url(r'^retrabalho/filter/picagem/(?P<pk>\d+)/$', picagem_retrabalho_add, name='picagem_retrabalho_add'),
    url(r'^retrabalho/filter/delete/(?P<pk>\d+)/', emenda_delete, name='emenda_delete'),
    url(r'^retrabalho/create/$', create_bobinagem_retrabalho, name='create_bobinagem_retrabalho'),
    url(r'^retrabalho/dm/(?P<pk>\d+)/$', retrabalho_dm, name='retrabalho_dm'),
    url(r'^retrabalho/validate/dm/(?P<pk>\d+)/(?P<id_bobines>[\w\-]+)/(?P<metros>[\w\-]+)/(?P<recycle>[\w\-]+)/$', validate_bobinagem_dm, name='validate_bobinagem_dm'),
    url(r'^retrabalho/filter/finalizar/(?P<pk>\d+)/$', BobinagemRetrabalhoFinalizar.as_view(), name='finalizar_retrabalho'),
    url(r'^retrabalho/refazer/(?P<pk>\d+)/$', refazer_bobinagem_dm, name='refazer_bobinagem_dm'),    
    url(r'^clientes/$', cliente_home, name='clientes'),
    url(r'^clientes/create/$', ClienteCreateView.as_view(), name='cliente_create'),
    url(r'^relatorio/linha/$', relatorio_diario, name='relatorio_diario'),
    url(r'^relatorio/$', relatorio_home, name='relatorio_home'),
    url(r'^relatorio/consumos/$', relatorio_consumos, name='relatorio_consumos'),
    url(r'^relatorio/paletes/$', relatorio_paletes, name='relatorio_paletes'),
    url(r'^etiqueta/retrabalho/(?P<pk>\d+)/$', etiqueta_retrabalho, name='etiqueta_retrabalho'),
    url(r'^etiqueta/palete/(?P<pk>\d+)/$', etiqueta_palete, name='etiqueta_palete'),
    url(r'^etiqueta/palete/(?P<pk>\d+)/reabrir/$', reabrir_palete, name='reabrir_palete'),
    url(r'^palete/(?P<pk>\d+)/ordenar/$', ordenar_bobines, name='ordenar_bobines'),
    url(r'^palete/(?P<pk>\d+)/(?P<operation>.+)/$', ordenar_bobines_op, name='ordenar_bobines_op'),
    url(r'^bobinagem/(?P<pk>\d+)/classificacao/$', c_bobines, name='classificacao_bobines'),
    url(r'^palete/validate/(?P<pk>\d+)/(?P<id_bobines>[\w\-]+)/$', palete_confirmation, name='palete_confirmation'),
    url(r'^palete/reabrir/(?P<pk>\d+)/$', palete_rabrir, name='palete_rabrir'),
    url(r'^palete/dm/(?P<pk>\d+)/$', palete_picagem_dm, name='palete_picagem_dm'),
    url(r'^palete/validate/dm/(?P<pk>\d+)/(?P<id_bobines>[\w\-]+)/$', validate_palete_dm, name='validate_palete_dm'),   
    url(r'^encomenda/$', encomenda_list, name='encomenda_list'),
    url(r'^encomenda/create/$', encomenda_create, name='encomenda_create'),
    url(r'^encomenda/(?P<pk>\d+)/', encomenda_detail, name='encomenda_detail'),
    url(r'^carga/$', carga_list, name='carga_list'),
    url(r'^carga/completa/$', carga_list_completa, name='carga_list_completa'),
    url(r'^carga/detail/(?P<pk>\d+)/$', carga_detail, name='carga_detail'),
    url(r'^carga/create/$', carga_create, name='carga_create'),
    url(r'^carga/imprimiretiquetapalete/(?P<pk>\d+)/$', carga_etiqueta_palete, name='carga_etiqueta_palete'),
    url(r'^armazem/$', armazem_home, name='armazem_home'),
    url(r'^palete/selecao/$', palete_selecao, name='palete_selecao'),
    url(r'^palete/pesagem/(?P<pk>\d+)/$', palete_pesagem, name='palete_pesagem'),
    url(r'^palete/armazem/(?P<pk>\d+)/$', palete_details_armazem, name='palete_details_armazem'),
    url(r'^stock/$', stock_list, name='stock_list'),
    url(r'^stock/palete/add/(?P<pk>\d+)/$', stock_add_to_carga, name='stock_add_to_carga'),
    url(r'^qualidade/$', qualidade_home, name='qualidade_home'),
    url(r'^qualidade/acd/$', acompanhamento_diario, name='acompanhamento_diario'),
    url(r'^retrabalho/(?P<pk>\d+)/$', retrabalho_v2, name='retrabalho_v2'),
    url(r'^retrabalho/confirmacao/(?P<pk>\d+)/(?P<b1>\d+)/(?P<m1>\d+)/(?P<b2>\w+)/(?P<m2>\w+)/(?P<b3>\w+)/(?P<m3>\w+)/$', retrabalho_confirmacao, name='retrabalho_confirmacao'),
    url(r'^palete/picagem/(?P<pk>\d+)/$', palete_picagem, name='palete_picagem'),    
    url(r'^listadebobines/(?P<pk>\d+)/$', classificacao_bobines_v2, name='classificacao_bobines_v2'),   
    url(r'^perfil/list/$', perfil_list_v2, name='perfil_list_v2'),    
    url(r'^perfil/details/(?P<pk>\d+)/$', perfil_details_v2, name='perfil_details_v2'),    
    url(r'^perfil/create/linha/$', perfil_create_linha_v2, name='perfil_create_linha_v2'),    
    url(r'^perfil/create/dm/$', perfil_create_dm_v2, name='perfil_create_dm_v2'),    
    url(r'^perfil/larguras/(?P<pk>\d+)/$', perfil_larguras_v2, name='perfil_larguras_v2'),
    url(r'^perfil/larguras/edit/(?P<pk>\d+)/$', perfil_edit_larguras_v2, name='perfil_edit_larguras_v2'),
    url(r'^perfil/larguras/cancel/(?P<pk>\d+)/$', cancel_insert_larguras, name='cancel_insert_larguras'),
    url(r'^perfil/delete/(?P<pk>\d+)/$', perfil_delete_v2, name='perfil_delete_v2'),

    # url(r'^teste/perfil/create/$', perfil_create_v2, name='perfil_create_v2'),    
    # url(r'^teste/perfil/largura/(?P<pk>\d+)/$', perfil_larguras_v2, name='perfil_larguras_v2'),    
    
]