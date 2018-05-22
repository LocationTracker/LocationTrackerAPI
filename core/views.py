from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import FamiliaSerializer, UsuarioSerializer
from .models import Familia, Usuario
from location.models import Localizacao
from location.serializers import LocalizacaoSerializer


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
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    http_method_names = ['get', 'post', 'put', 'patch']


class ListUsers(APIView):
    """
    View to list all users in the system.
    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    # authentication_classes = []
    queryset = Usuario.objects.all()
    permission_classes = [
        IsAuthenticated,
    ]

    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        usuarios = Usuario.objects.all()
        serializer = UsuarioSerializer(usuarios, context={'request': request})
        return Response(serializer.data)
