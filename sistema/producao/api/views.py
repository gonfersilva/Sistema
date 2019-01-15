from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from rest_framework.views import APIView
from django.http import Http404
from rest_framework.response import Response
from producao.models import Palete, Bobine, Emenda, Bobinagem
from .serializers import PaleteListSerializer, PaleteDetailSerializer, BobineSerializer, EmendaSerializer, EmendaCreateSerializer, BobinagemListSerializer
from django.contrib.auth.mixins import LoginRequiredMixin

class PaleteListAPIView(ListAPIView):
    queryset = Palete.objects.all()
    serializer_class = PaleteListSerializer


class PaleteDetailAPIView(RetrieveAPIView):
    queryset = Palete.objects.all()
    serializer_class = PaleteDetailSerializer

class BobineListAPIView(ListAPIView):
    queryset = Bobine.objects.filter()
    serializer_class = BobineSerializer

class BobineList(LoginRequiredMixin, APIView):
    
    def get(self, request, pk, format=None):
        bobine = Bobine.objects.filter(palete=pk)
        serializer = BobineSerializer(bobine, many=True)
        return Response(serializer.data)
        

class EmendaListAPIView(LoginRequiredMixin, ListAPIView):
    queryset = Emenda.objects.all()
    serializer_class = EmendaSerializer


class EmendaCreateAPIView(LoginRequiredMixin, CreateAPIView):
    queryset = Emenda.objects.all()
    serializer_class = EmendaCreateSerializer

class BobinagemListAPIView(ListAPIView):
    queryset = Bobinagem.objects.all().order_by('-data', '-fim')[:50]
    serializer_class = BobinagemListSerializer
