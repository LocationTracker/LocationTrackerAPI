from django.db.models import Model, CharField, ImageField, OneToOneField, ForeignKey, PROTECT, SET_NULL
from django.contrib.auth.models import User
from .utils import get_usuario_upload_path


class Familia(Model):
    nome = CharField(max_length=30, unique=True, null=True, blank=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'família'
        verbose_name_plural = 'famílias'

class Usuario(Model):
    perfil_user = OneToOneField(User, unique=True, on_delete=PROTECT)
    foto = ImageField(upload_to=get_usuario_upload_path, null=True, blank=True)
    cpf = CharField(max_length=16, null=True, blank=True)
    telefone = CharField(max_length=18, null=True, blank=True)

    familia = ForeignKey(Familia, null=True, blank=True, on_delete=SET_NULL, related_name='participantes')

    def __str__(self):
        assert isinstance(self.perfil_user, User)
        return self.perfil_user.username

    class Meta:
        verbose_name = 'usuário'
        verbose_name_plural = 'usuários'