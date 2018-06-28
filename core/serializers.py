from rest_framework.serializers import Serializer, ModelSerializer, CharField, PrimaryKeyRelatedField, EmailField
from django.contrib.auth.models import User
from .models import Familia, PerfilUsuario


class LoginSerializer(Serializer):
    username = CharField()
    password = CharField()


class FamiliaSerializer(ModelSerializer):
    nome = CharField()
    participantes = PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Familia
        # fields = ('url', 'nome', 'participantes')
        fields = '__all__'


class UsuarioSerializer(ModelSerializer):
    familia_nome = PrimaryKeyRelatedField(source='familia.nome', many=False, read_only=True)
    familia = PrimaryKeyRelatedField(many=False, queryset=Familia.objects.all())
    username = CharField(source='user.username')
    email = EmailField(source='user.email')
    # foto = serializers.ImageField()
    cpf = CharField()
    telefone = CharField()

    class Meta:
        model = PerfilUsuario
        # fields = ('url', 'username', 'email', 'password', 'foto', 'cpf', 'telefone', 'familia', 'familia_nome')
        fields = '__all__'