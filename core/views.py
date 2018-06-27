from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.response import Response
from .serializers import UsuarioSerializer
from .models import PerfilUsuario
from location.serializers import UsuarioLocalizacaoSerializer, \
    SendLocalizacaoSerializer, UltimaLocalizacaoSerializer


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
    authentication_classes = [SessionAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = PerfilUsuario.objects.all()
    serializer_class = UsuarioSerializer
    http_method_names = ['get', 'post', 'put', 'patch']

    @action(detail=False)
    def get_family_members(self, request):
        """
        Retorna os membros familiares de um usuário existente
        """
        usuario = request.auth.user.perfil
        membros = PerfilUsuario.objects.filter(familia=usuario.familia)
        serializer = UsuarioSerializer(membros, many=True)
        return Response(serializer.data)

    @action(methods=['get'], detail=False, serializer_class=UsuarioLocalizacaoSerializer)
    def get_family_locations(self, request):
        """
        Retorna as TODAS localizações do membros familiares de um usuário existente
        """
        usuario = request.auth.user.perfil
        membros = PerfilUsuario.objects.filter(familia=usuario.familia)
        locations = []
        for membro in membros:
            locations.append(membro.location)
        serializer = UsuarioLocalizacaoSerializer(locations, many=True)
        return Response(serializer.data)

    @action(methods=['get'], detail=False, serializer_class=UltimaLocalizacaoSerializer)
    def get_family_last_location(self, request):
        """
        Retorna a última localização dos membros familiares de um usuário existente
        """
        usuario = request.auth.user.perfil
        membros = PerfilUsuario.objects.filter(familia=usuario.familia)
        locations = []
        for membro in membros:
            locations.append(membro.location.ultima_localizacao)

        serializer = UltimaLocalizacaoSerializer(locations, many=True)
        return Response(serializer.data)

    @action(methods=['get'], detail=False, serializer_class=UsuarioLocalizacaoSerializer)
    def get_locations(self, request):
        """
        Retorna TODA a lista de localizações de um usuário existente
        """
        usuario = request.auth.user.perfil
        serializer = UsuarioLocalizacaoSerializer(usuario.location)
        return Response(serializer.data)

    @action(methods=['get'], detail=False, serializer_class=UltimaLocalizacaoSerializer)
    def get_last_location(self, request):
        """
        Retorna a última localização de um usuário existente
        """
        usuario = request.auth.user.perfil
        serializer = UltimaLocalizacaoSerializer(usuario.location.ultima_localizacao)
        return Response(serializer.data)

    #@TODO filter de localizações
    # @action(methods=['post'], detail=True, serializer_class=FilterLocalizacaoSerializer)
    # def filter_locations(self, request, pk=None):
    #     """
    #     Retorna a lista de localizações de um usuário existente de acordo com os filtros passados
    #     """
    #     usuario = self.get_object()
    #     usuario_locations = UsuarioLocalizacao.objects.get(id_usuario=usuario.id)
    #     #
    #     serializer = UsuarioLocalizacaoSerializer(usuario_locations)
    #     return Response(serializer.data)

    @action(methods=['post'], detail=False, serializer_class=SendLocalizacaoSerializer)
    def send_location(self, request):
        """
        Registra uma nova localização de um usuário existente
        """
        usuario = request.auth.user.perfil
        serializer = SendLocalizacaoSerializer(data=request.data)
        if serializer.is_valid():
            usuario.add_location_json(request.data)
            return Response(UltimaLocalizacaoSerializer(usuario.location.ultima_localizacao).data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
