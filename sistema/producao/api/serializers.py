from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField
from producao.models import Palete, Bobine, Largura, Perfil, Emenda, Bobinagem, Cliente


class PerfilSerializer(ModelSerializer):
       
    class Meta:
        model = Perfil
        fields = [
            'produto',
            'num_bobines',
            'core',
            'retrabalho'
                       
        ]
        
class BobinagemSerializer(ModelSerializer):
    perfil = PerfilSerializer()
    class Meta:
        model = Bobinagem
        fields = "__all__"

class ClienteSerializer(ModelSerializer):
    class Meta:
        model = Cliente
        fields = "__all__"

class PaleteListSerializer(ModelSerializer):
    cliente = ClienteSerializer()
    class Meta:
        model = Palete
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
            "num_emendas",
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
        
class PaleteDmSerializer(ModelSerializer):
    class Meta:
        model = Palete
        fields = [
            "id",
            "nome",
            "num",
            "data_pal",
            "estado",
            "num_bobines_act",
            "num_bobines",
            "area",
            "comp_total",
            "largura_bobines"
        ]

class BobinesPaleteDmSerializer(ModelSerializer):
    bobinagem = BobinagemSerializer()
    class Meta:
        model = Bobine
        fields = [
            "id",
            "nome", 
            "estado",
            "largura",
            "bobinagem",
            "palete"

        ]

class BobinagemCompSerializer(ModelSerializer):
    class Meta:
        model = Bobinagem
        fields = [
            "comp"
        ]

class BobinesDmSerializer(ModelSerializer):
    bobinagem = BobinagemCompSerializer()
    largura = LarguraSerializer()
    class Meta:
        model = Bobine
        fields = [
            "id",
            "nome",
            "estado",
            "largura",
            "comp_actual",
            "bobinagem"

        ]

class BobinagemCreateSerializer(ModelSerializer):
    class Meta:
        model = Bobinagem
        fields = [
            "data",
            "perfil",
            "inico",
            "fim",
            "diam",
            "num_bobinagem",
            "obs"
        ]