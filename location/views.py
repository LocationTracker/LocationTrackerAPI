from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import LocalizacaoSerializer
from .models import Localizacao


class LocalizacaoViewSet(viewsets.ModelViewSet):
    """
    retrieve:
        Retorna uma localização
    list:
        Retorna todas as localizações
    create:
        Cria uma nova localização
    delete:
        Remove uma localização existente
    partial_update:
        Atualiza um ou mais campos de uma localização existente
    update:
        Atualiza uma localização
    """
    queryset = Localizacao.objects.all()
    serializer_class = LocalizacaoSerializer
    # permission_classes = [
    #     IsAuthenticated,
    # ]
    http_method_names = ['get', 'post']
