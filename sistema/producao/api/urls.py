from django.conf.urls import url, include
from django.contrib import admin
from producao.api.views import PaleteListAPIView, BobineListDmAPIView, BobinagemCreateDmAPIView, BobineListAPIView, PaleteDetailAPIView, BobineList, EmendaListAPIView, EmendaCreateAPIView, PaleteDmBobinesAPIView, BobinagemListAPIView, BobineDetailAPIView, BobineListAllAPIView,ClienteDetailAPIView,BobinesBobinagemAPIView,PaleteDmAPIView

app_name="producao" 

urlpatterns = [
    
    url(r'^palete/$', PaleteListAPIView.as_view(), name='palete-list'),
    url(r'^bobine/$', BobineListAPIView.as_view(), name='bobine-list'),
    url(r'^bobinelist/$', BobineListAllAPIView.as_view(), name='bobine-list2'),
    url(r'^bobinagem/$', BobinagemListAPIView.as_view(), name='bobinagem-list'),
    url(r'^emenda/$', EmendaListAPIView.as_view(), name='emenda-list'),
    url(r'^emenda/create/$', EmendaCreateAPIView.as_view(), name='emenda-create'),
    url(r'^palete/(?P<pk>\d+)/$', PaleteDetailAPIView.as_view(), name='palete-detail'),
    url(r'^bobine/(?P<pk>\d+)/$', BobineDetailAPIView.as_view(), name='bobine-list2'),
    url(r'^cliente/(?P<pk>\d+)/$', ClienteDetailAPIView.as_view(), name='cliente'),
    url(r'^bobinagem/(?P<pk>\d+)/$', BobinesBobinagemAPIView.as_view(), name='cliente'),
    url(r'^palete/dm/$', PaleteDmAPIView.as_view(), name='paletes_dm'),
    url(r'^palete/dm/(?P<pk>\d+)$', PaleteDmBobinesAPIView.as_view(), name='paletes_dm_bobines'),
    url(r'^bobine/dm/$', BobineListDmAPIView.as_view(), name='bobines-dm'),
    url(r'^bobinagem/dm/$', BobinagemCreateDmAPIView.as_view(), name='bobineagem-create-dm'),
    
    
    
    
    
    
    
]