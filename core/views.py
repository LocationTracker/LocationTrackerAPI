from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import FamiliaSerializer, UsuarioSerializer
from .models import Familia, PerfilUsuario
from location.models import UsuarioLocalizacao, Localizacao
from location.serializers import UsuarioLocalizacaoSerializer, \
    AnoSerializer, MesSerializer, DiaSerializer, HoraSerializer, \
    LocalizacaoSerializer, SendLocalizacaoSerializer, LastLocalizacaoSerializer


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

    @action(methods=['get'], detail=True, serializer_class=UsuarioLocalizacaoSerializer)
    def get_family_locations(self, request, pk=None):
        """
        Retorna as TODAS localizações do membros familiares de um usuário existente
        """
        usuario = self.get_object()
        membros = PerfilUsuario.objects.filter(familia=usuario.familia)
        locations = UsuarioLocalizacao.objects
        for membro in membros:
            locations.filter(id_usuario=membro.id)
        serializer = UsuarioLocalizacaoSerializer(locations, many=True)
        return Response(serializer.data)

    @action(methods=['get'], detail=True, serializer_class=UsuarioLocalizacaoSerializer)
    def get_locations(self, request, pk=None):
        """
        Retorna TODA a lista de localizações de um usuário existente
        """
        usuario = self.get_object()
        usuario_locations = UsuarioLocalizacao.objects.get(id_usuario=usuario.id)
        serializer = UsuarioLocalizacaoSerializer(usuario_locations)
        return Response(serializer.data)

    @action(methods=['get'], detail=True, serializer_class=LastLocalizacaoSerializer)
    def get_last_location(self, request, pk=None):
        """
        Retorna a última localização de um usuário existente
        """
        usuario = self.get_object()
        u_loc = UsuarioLocalizacao.objects.get(id_usuario=usuario.id)
        last = u_loc.get_last_location()
        serializer = LastLocalizacaoSerializer(last)
        return Response(serializer.data)

    # @action(methods=['post'], detail=True, serializer_class=FilterLocalizacaoSerializer)
    # def filter_locations(self, request, pk=None):
    #     """
    #     Retorna a lista de localizações de um usuário existente de acordo com os filtros passados
    #     """
    #     usuario = self.get_object()
    #     usuario_locations = UsuarioLocalizacao.objects.get(id_usuario=usuario.id)
    #     # @TODO FAZER REMOCAO DE ITENS
    #     serializer = UsuarioLocalizacaoSerializer(usuario_locations)
    #     return Response(serializer.data)

    @action(methods=['post'], detail=True, serializer_class=SendLocalizacaoSerializer)
    def send_location(self, request, pk=None):
        """
        Registra uma nova localização de um usuário existente
        """
        usuario = self.get_object()
        serializer = SendLocalizacaoSerializer(data=request.data)
        if serializer.is_valid():
            u_loc = UsuarioLocalizacao.objects.get(id_usuario=usuario.id)
            assert isinstance(u_loc, UsuarioLocalizacao)
            u_loc.add_location_data(request.data)
            u_loc.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
