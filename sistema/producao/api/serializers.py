from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField
from producao.models import Palete, Bobine, Largura, Perfil, Emenda, Bobinagem, Cliente


class PerfilSerializer(ModelSerializer):
       
    class Meta:
        model = Perfil
        fields = [
            'produto',
            'core',
            'retrabalho'
                       
        ]
        
class BobinagemSerializer(ModelSerializer):
    perfil = PerfilSerializer()
    class Meta:
        model = Bobinagem
        fields = "__all__"
        
class PaleteListSerializer(ModelSerializer):
    class Meta:
        model = Palete
        fields = "__all__"

class ClienteSerializer(ModelSerializer):
    class Meta:
        model = Cliente
        fields = "__all__"

class PaleteDetailSerializer(ModelSerializer):
    cliente = ClienteSerializer()
    class Meta:
        model = Palete
        fields = [
            'id',
            'nome',
            'estado',
            'comp_total',
            'num_bobines',
            'largura_bobines',
            'cliente',
            'core_bobines'
        ]


class LarguraSerializer(ModelSerializer):
    perfil = PerfilSerializer()
    class Meta:
        model = Largura
        fields = [
            'perfil',
            'num_bobine',
            'largura',
            
        ]
            

class BobineSerializer(ModelSerializer):
    largura = LarguraSerializer()
    bobinagem = BobinagemSerializer()
    palete = PaleteDetailSerializer()
    
       
    class Meta:
        model = Bobine
        fields = [
            'id',
            'bobinagem',
            'nome',
            'posicao_palete',
            'estado',
            'area',
            'largura',
            'palete',
            'comp_actual',
            'obs',
            'con',
            'descen',
            'presa',
            'diam_insuf',
            'furos',
            'esp',
            'troca_nw',
            'outros',          

        ]

class EmendaSerializer(ModelSerializer):
    bobine = BobineSerializer()
    bobinagem = BobinagemSerializer()
    class Meta:
        model = Emenda
        fields = [
            "bobinagem",
            "bobine", 
            "num_emenda", 
            "emenda", 
            "metros", 
            
        ]

class EmendaCreateSerializer(ModelSerializer):

    class Meta:
        model = Emenda
        fields = [
            
            "bobine", 
            "num_emenda", 
            "emenda", 
            "metros", 
            
        ]

class BobinagemListSerializer(ModelSerializer):
    perfil = PerfilSerializer()
    
    
    class Meta:
        model = Bobinagem
        fields = [
            "id",
            "nome",
            "perfil",
            "data",
            "inico",
            "fim",
            "duracao",
            "comp",
            "comp_par",
            "comp_cli",
            "area",
            "estado"
        ]

class BobineListAllSerializer(ModelSerializer):

    class Meta:
        model = Bobine
        fields = [
            "id",
            "nome",
            "palete"
        ]

class BobinagemBobinesSerializer(ModelSerializer):
    class Meta:
        model = Bobine
        fields = [

            "estado"
        ]
        