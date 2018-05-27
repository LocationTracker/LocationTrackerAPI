from rest_framework import serializers
from drf_compound_fields.fields import DictField
from django.contrib.auth.models import User
from .models import UsuarioLocalizacao, AnoLocalizacao


class LocalizacSerializer(serializers.Serializer):
    hora = serializers.IntegerField()
    minutos = serializers.IntegerField()
    lat = serializers.CharField()
    long = serializers.CharField()


class DiaLocalizacSerializer(serializers.Serializer):
    value = serializers.IntegerField()
    localizacoes = LocalizacSerializer(many=True)


class MesLocalizacSerializer(serializers.Serializer):
    value = serializers.IntegerField()
    dias = DiaLocalizacSerializer(many=True)


class AnoLocalizacSerializer(serializers.Serializer):
    value = serializers.IntegerField()
    meses = MesLocalizacSerializer(many=True)


class UsuarioLocalizacaoSerializer(serializers.ModelSerializer):
    anos = AnoLocalizacSerializer(many=True)
    id_usuario = serializers.IntegerField()

    class Meta:
        model = UsuarioLocalizacao
        fields = ('id', 'id_usuario', 'anos')


class FilterLocalizacaoSerializer(serializers.Serializer):
    filter_ano_do = serializers.BooleanField()
    filter_ano_value = serializers.IntegerField(required=False)
    filter_mes_do = serializers.BooleanField()
    filter_mes_value = serializers.IntegerField(required=False)
    filter_dia_do = serializers.BooleanField()
    filter_dia_value = serializers.IntegerField(required=False)
    filter_hora_do = serializers.BooleanField()
    filter_hora_value = serializers.IntegerField(required=False)
    filter_minute_do = serializers.BooleanField()
    filter_minute_value = serializers.IntegerField(required=False)
