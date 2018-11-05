from django.conf.urls import url, include
from django.contrib import admin
from producao.api.views import PaleteListAPIView, BobineListAPIView, PaleteDetailAPIView, BobineList, EmendaListAPIView, EmendaCreateAPIView

app_name="producao" 

urlpatterns = [
    
    url(r'^palete/$', PaleteListAPIView.as_view(), name='palete-list'),
    url(r'^bobine/$', BobineListAPIView.as_view(), name='bobine-list'),
    url(r'^emenda/$', EmendaListAPIView.as_view(), name='emenda-list'),
    url(r'^emenda/create/$', EmendaCreateAPIView.as_view(), name='emenda-create'),
    url(r'^palete/(?P<pk>\d+)/$', PaleteDetailAPIView.as_view(), name='palete-detail'),
    url(r'^bobine/(?P<pk>\d+)/$', BobineList.as_view(), name='bobine-list2'),
    
    
    
]