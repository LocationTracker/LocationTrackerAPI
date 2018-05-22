from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Localizacao


class LocalizacaoSerializer(serializers.ModelSerializer):
    id_usuario = serializers.IntegerField()
    data = serializers.DateTimeField()
    lat = serializers.CharField()
    long = serializers.CharField()

    class Meta:
        model = Localizacao
        # fields = ('url', 'id_usuario', 'data', 'lat', 'long')
        fields = '__all__'


class LocalizacaoSerializerPost(serializers.ModelSerializer):
    data = serializers.DateTimeField()
    lat = serializers.CharField()
    long = serializers.CharField()

    class Meta:
        model = Localizacao
        fields = ('data', 'lat', 'long')
        # fields = '__all__'
