from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from core.serializers import FamiliaSerializer, UsuarioSerializer
from core.models import Familia, Usuario


class FamiliaViewSet(viewsets.ModelViewSet):
    """
    retrieve:
        Return a user instance.
    list:
        Return all users, ordered by most recently joined.
    create:
        Create a new user.
    delete:
        Remove an existing user.
    partial_update:
        Update one or more fields on an existing user.
    update:
        Update a user.
    """
    queryset = Familia.objects.all()
    serializer_class = FamiliaSerializer
    # permission_classes = [
    #     IsAuthenticated,
    # ]
    # http_method_names = ['get', 'post', 'put', 'delete']

class UsuarioViewSet(viewsets.ModelViewSet):
    """
    retrieve:
        Return a user instance.
    list:
        Return all users, ordered by most recently joined.
    create:
        Create a new user.
    delete:
        Remove an existing user.
    partial_update:
        Update one or more fields on an existing user.
    update:
        Update a user.
    """
    # permission_classes = [
    #     IsAuthenticated,
    # ]
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer


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
