from rest_framework.serializers import Serializer, CharField, IntegerField
from rest_framework_mongoengine.serializers import EmbeddedDocumentSerializer, DocumentSerializer
from rest_framework_mongoengine.fields import DictField
from .models import UsuarioLocalizacao, AnoLocalizacao, MesLocalizacao, DiaLocalizacao, HoraLocalizacao, Localizacao


class LocalizacaoSerializer(EmbeddedDocumentSerializer):
    class Meta:
        model = Localizacao
        fields = '__all__'


class HoraSerializer(EmbeddedDocumentSerializer):
    localizacoes = DictField(child=LocalizacaoSerializer(), required=False, )
    class Meta:
        model = HoraLocalizacao
        fields = '__all__'


class DiaSerializer(EmbeddedDocumentSerializer):
    horas = DictField(child=HoraSerializer(), required=False, )
    class Meta:
        model = DiaLocalizacao
        fields = '__all__'


class MesSerializer(EmbeddedDocumentSerializer):
    dias = DictField(child=DiaSerializer(), required=False, )
    class Meta:
        model = MesLocalizacao
        fields = '__all__'


class AnoSerializer(EmbeddedDocumentSerializer):
    meses = DictField(child=MesSerializer(), required=False, )
    class Meta:
        model = AnoLocalizacao
        fields = '__all__'


class UsuarioLocalizacaoSerializer(DocumentSerializer):
    anos = DictField(child=AnoSerializer(), required=False, )
    class Meta:
        model = UsuarioLocalizacao
        fields = '__all__'


class LastLocalizacaoSerializer(Serializer):
    id_usuario = IntegerField()
    ano = CharField()
    mes = CharField()
    dia = CharField()
    hora = CharField()
    minutos = CharField()
    lat = CharField()
    long = CharField()

class SendLocalizacaoSerializer(Serializer):
    ano = CharField(min_length=4, max_length=4)
    mes = CharField(min_length=2, max_length=2)
    dia = CharField(min_length=2, max_length=2)
    hora = CharField(min_length=2, max_length=2)
    minutos = CharField(min_length=2, max_length=2)
    lat = CharField()
    long = CharField()


# class FilterLocalizacaoSerializer(Serializer):
#     filter_ano_do = BooleanField()
#     filter_ano_value = serializers.IntegerField(required=False)
#     filter_mes_do = serializers.BooleanField()
#     filter_mes_value = serializers.IntegerField(required=False)
#     filter_dia_do = serializers.BooleanField()
#     filter_dia_value = serializers.IntegerField(required=False)
#     filter_hora_do = serializers.BooleanField()
#     filter_hora_value = serializers.IntegerField(required=False)
#     filter_minute_do = serializers.BooleanField()
#     filter_minute_value = serializers.IntegerField(required=False)
