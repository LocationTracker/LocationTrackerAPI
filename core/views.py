from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from .serializers import UsuarioSerializer, LoginSerializer
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
    permission_classes = [IsAuthenticated, AllowAny]
    queryset = PerfilUsuario.objects.all()
    serializer_class = UsuarioSerializer
    http_method_names = ['get', 'post', 'put', 'patch']

    @action(methods=['post'], detail=False, serializer_class=LoginSerializer)
    def auth(self, request):
        """
        Retorna o usuario e seu token
        """
        usuario = get_object_or_404(PerfilUsuario, user__username=request.data['username'])
        if not usuario.user.check_password(request.data['password']):
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        serializer = UsuarioSerializer(usuario, many=False)
        return Response({'token': usuario.token.key, 'usuario': serializer.data})


    @action(methods=['get'], detail=True)
    def get_family_members(self, request, pk=None):
        """
        Retorna os membros familiares de um usuário existente
        """
        # usuario = request.auth.user.perfil
        usuario = self.get_object()
        membros = PerfilUsuario.objects.filter(familia=usuario.familia)
        serializer = UsuarioSerializer(membros, many=True)
        return Response(serializer.data)

    @action(methods=['get'], detail=True, serializer_class=UsuarioLocalizacaoSerializer)
    def get_family_locations(self, request, pk=None):
        """
        Retorna as TODAS localizações do membros familiares de um usuário existente
        """
        # usuario = request.auth.user.perfil
        usuario = self.get_object()
        membros = PerfilUsuario.objects.filter(familia=usuario.familia)
        locations = []
        for membro in membros:
            locations.append(membro.location)
        serializer = UsuarioLocalizacaoSerializer(locations, many=True)
        return Response(serializer.data)

    @action(methods=['get'], detail=True, serializer_class=UltimaLocalizacaoSerializer)
    def get_family_last_location(self, request, pk=None):
        """
        Retorna a última localização dos membros familiares de um usuário existente
        """
        # usuario = request.auth.user.perfil
        usuario = self.get_object()
        membros = PerfilUsuario.objects.filter(familia=usuario.familia)
        locations = []
        for membro in membros:
            locations.append(membro.location.ultima_localizacao)

        serializer = UltimaLocalizacaoSerializer(locations, many=True)
        return Response(serializer.data)

    @action(methods=['get'], detail=True, serializer_class=UsuarioLocalizacaoSerializer)
    def get_locations(self, request, pk=None):
        """
        Retorna TODA a lista de localizações de um usuário existente
        """
        # usuario = request.auth.user.perfil
        usuario = self.get_object()
        serializer = UsuarioLocalizacaoSerializer(usuario.location)
        return Response(serializer.data)

    @action(methods=['get'], detail=True, serializer_class=UltimaLocalizacaoSerializer)
    def get_last_location(self, request, pk=None):
        """
        Retorna a última localização de um usuário existente
        """
        # usuario = request.auth.user.perfil
        usuario = self.get_object()
        serializer = UltimaLocalizacaoSerializer(usuario.location.ultima_localizacao)
        return Response(serializer.data)


    @action(methods=['post'], detail=True, serializer_class=SendLocalizacaoSerializer)
    def send_location(self, request, pk=None):
        """
        Registra uma nova localização de um usuário existente
        """
        # usuario = request.auth.user.perfil
        usuario = self.get_object()
        serializer = SendLocalizacaoSerializer(data=request.data)
        if serializer.is_valid():
            usuario.add_location_json(request.data)
            return Response(UltimaLocalizacaoSerializer(usuario.location.ultima_localizacao).data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
