from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Familia, Usuario


class FamiliaSerializer(serializers.ModelSerializer):
    nome = serializers.CharField()
    participantes = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Familia
        # fields = ('url', 'nome', 'participantes')
        fields = '__all__'


class UsuarioSerializer(serializers.ModelSerializer):
    familia_nome = serializers.PrimaryKeyRelatedField(source='familia.nome', many=False, read_only=True)
    familia = serializers.PrimaryKeyRelatedField(many=False, queryset=Familia.objects.all())
    username = serializers.CharField(source='perfil_user.username')
    email = serializers.EmailField(source='perfil_user.email')
    password = serializers.CharField(source='perfil_user.password')
    # foto = serializers.ImageField()
    cpf = serializers.CharField()
    telefone = serializers.CharField()

    class Meta:
        model = Usuario
        # fields = ('url', 'username', 'email', 'password', 'foto', 'cpf', 'telefone', 'familia', 'familia_nome')
        fields = '__all__'