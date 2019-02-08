from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from rest_framework.views import APIView
from django.http import Http404
from rest_framework.response import Response
from producao.models import Palete, Bobine, Emenda, Bobinagem, Cliente
from .serializers import PaleteListSerializer, PaleteDetailSerializer, BobineSerializer, EmendaSerializer, EmendaCreateSerializer, BobinagemListSerializer, BobineListAllSerializer,ClienteSerializer
from django.contrib.auth.mixins import LoginRequiredMixin

class PaleteListAPIView(LoginRequiredMixin, ListAPIView):
    queryset = Palete.objects.all().order_by('-data_pal', '-num')
    serializer_class = PaleteListSerializer


class PaleteDetailAPIView(LoginRequiredMixin, RetrieveAPIView):
    queryset = Palete.objects.all()
    serializer_class = PaleteDetailSerializer

class ClienteDetailAPIView(LoginRequiredMixin, RetrieveAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class BobineDetailAPIView(LoginRequiredMixin, RetrieveAPIView):
    queryset = Bobine.objects.all()
    serializer_class = BobineSerializer

class BobineListAPIView(LoginRequiredMixin, ListAPIView):
    queryset = Bobine.objects.filter()
    serializer_class = BobineSerializer

class BobineListAllAPIView(LoginRequiredMixin, ListAPIView):
    queryset = Bobine.objects.filter()
    serializer_class = BobineListAllSerializer

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

class BobinagemListAPIView(LoginRequiredMixin, ListAPIView):
    queryset = Bobinagem.objects.all().order_by('-data', '-fim')
    serializer_class = BobinagemListSerializer
