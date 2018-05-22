from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import LocalizacaoSerializer
from .models import Localizacao


class LocalizacaoViewSet(viewsets.ModelViewSet):
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
    queryset = Localizacao.objects.all()
    serializer_class = LocalizacaoSerializer
    # permission_classes = [
    #     IsAuthenticated,
    # ]
    # http_method_names = ['get', 'post', 'put', 'delete']
