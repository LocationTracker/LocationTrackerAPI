from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import FamiliaSerializer, UsuarioSerializer
from .models import Familia, PerfilUsuario
from location.models import UsuarioLocalizacao
from location.serializers import UsuarioLocalizacaoSerializer, AnoSerializer, MesSerializer, DiaSerializer, HoraSerializer, LocalizacaoSerializer, FilterLocalizacaoSerializer


class FamiliaViewSet(viewsets.ModelViewSet):
    """
    retrieve:
        Retorna uma família
    list:
        Retorna todas as famílias
    create:
        Cria uma nova família
    delete:
        Remove uma família existente
    partial_update:
        Atualiza um ou mais campos de uma família existente
    update:
        Atualiza uma família
    """
    queryset = Familia.objects.all()
    serializer_class = FamiliaSerializer
    # permission_classes = [
    #     IsAuthenticated,
    # ]
    http_method_names = ['get', 'post', 'put', 'patch']


class UsuarioViewSet(viewsets.ModelViewSet):
    """
    retrieve:
        Retorna um usuário
    list:
        Retorna todos os usuários
    create:
        Cria um novo usuário
    delete:
        Remove um usuário existente
    partial_update:
        Atualiza um ou mais campos de um usuário existente
    update:
        Atualiza um usuário
    """
    # permission_classes = [
    #     IsAuthenticated,
    # ]
    queryset = PerfilUsuario.objects.all()
    serializer_class = UsuarioSerializer
    http_method_names = ['get', 'post', 'put', 'patch']

    @action(methods=['get'], detail=True)
    def get_family_members(self, request, pk=None):
        """
        Retorna os membros familiares de um usuário existente
        """
        usuario = self.get_object()
        membros = PerfilUsuario.objects.filter(familia=usuario.familia)
        serializer = UsuarioSerializer(membros, many=True)
        return Response(serializer.data)

    # @action(methods=['get'], detail=True, serializer_class=LocalizacaoSerializer)
    # def get_family_locations(self, request, pk=None):
    #     """
    #     Retorna as localizações do membros familiares de um usuário existente
    #     """
    #     usuario = self.get_object()
    #     membros = PerfilUsuario.objects.filter(familia=usuario.familia)
    #     locations = Localizacao.objects
    #     for membro in membros:
    #         locations.filter(id_usuario=membro.id)
    #     serializer = LocalizacaoSerializer(locations, many=True)
    #     return Response(serializer.data)

    @action(methods=['get'], detail=True, serializer_class=UsuarioLocalizacaoSerializer)
    def get_locations(self, request, pk=None):
        """
        Retorna a lista de localizações de um usuário existente
        """
        usuario = self.get_object()
        usuario_locations = UsuarioLocalizacao.objects.get(id_usuario=usuario.id)
        serializer = UsuarioLocalizacaoSerializer(usuario_locations)
        return Response(serializer.data)

    @action(methods=['post'], detail=True, serializer_class=FilterLocalizacaoSerializer)
    def filter_locations(self, request, pk=None):
        """
        Retorna a lista de localizações de um usuário existente de acordo com os filtros passados
        """
        usuario = self.get_object()
        usuario_locations = UsuarioLocalizacao.objects.get(id_usuario=usuario.id)
        # @TODO FAZER REMOCAO DE ITENS
        serializer = UsuarioLocalizacaoSerializer(usuario_locations)
        return Response(serializer.data)

    # @action(methods=['post'], detail=True, serializer_class=LocalizacaoSerializerPost)
    # def send_location(self, request, pk=None):
    #     """
    #     Registra uma nova localização de um usuário existente
    #     """
    #     request.data['id_usuario'] = pk
    #     serializer = LocalizacaoSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     else:
    #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
