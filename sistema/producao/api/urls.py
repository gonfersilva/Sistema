from django.conf.urls import url, include
from django.contrib import admin
from producao.api.views import PaleteListAPIView, BobineListAPIView, PaleteDetailAPIView, BobineList, EmendaListAPIView, EmendaCreateAPIView, BobinagemListAPIView, BobineDetailAPIView, BobineListAllAPIView,ClienteDetailAPIView,BobinesBobinagemAPIView

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
    
    
    
    
    
]