from django.db.models import Model, CharField, ImageField, OneToOneField, ForeignKey, PROTECT, SET_NULL
from django.contrib.auth.models import User
from .utils import get_usuario_upload_path


class Familia(Model):
    nome = CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return self.nome


