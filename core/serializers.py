from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Familia, Usuario


class FamiliaSerializer(serializers.ModelSerializer):
    nome = serializers.CharField()

    class Meta:
        model = Familia
        fields = ('url', 'nome')


class UsuarioSerializer(serializers.ModelSerializer):
    familia = FamiliaSerializer()
    username = serializers.CharField(source='perfil_user.username')
    email = serializers.EmailField(source='perfil_user.email')
    password = serializers.CharField(source='perfil_user.password')
    # foto = serializers.ImageField()
    cpf = serializers.CharField()
    telefone = serializers.CharField()

    class Meta:
        model = Usuario
        fields = ('url', 'username', 'email', 'password', 'foto', 'cpf', 'telefone', 'familia')
