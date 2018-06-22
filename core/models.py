from django.db.models import Model, CharField, ImageField, OneToOneField, ForeignKey, PROTECT, SET_NULL, CASCADE
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from location.models import UsuarioLocalizacao
from .utils import get_usuario_upload_path


class Familia(Model):
    nome = CharField(max_length=30, unique=True, null=True, blank=True)

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'família'
        verbose_name_plural = 'famílias'


class PerfilUsuario(Model):
    user = OneToOneField(User, unique=True, on_delete=CASCADE, related_name='perfil')
    foto = ImageField(upload_to=get_usuario_upload_path, null=True, blank=True)
    cpf = CharField(max_length=16, null=True, blank=True)
    telefone = CharField(max_length=18, null=True, blank=True)

    familia = ForeignKey(Familia, null=True, blank=True, on_delete=SET_NULL, related_name='participantes')

    def __str__(self):
        assert isinstance(self.user, User)
        return self.user.username

    def save(self, *args, **kwargs):
        if not self.pk:
            try:
                p = PerfilUsuario.objects.get(user=self.user)
                self.pk = p.pk
            except PerfilUsuario.DoesNotExist:
                pass

        super(PerfilUsuario, self).save(*args, **kwargs)

    @property
    def location(self):
        return UsuarioLocalizacao.objects.get(id_usuario=self.user.id)

    def add_location(self, ano, mes, dia, hora, minuto, lat, long):
        loc = self.location
        loc.add_location(ano, mes, dia, hora, minuto, lat, long)
        loc.save()

    class Meta:
        verbose_name = 'perfil usuário'
        verbose_name_plural = 'perfis usuários'


def create_usuario(sender, **kwargs):
    user = kwargs["instance"]
    if kwargs["created"]:
        usuario = PerfilUsuario(user=user)
        usuario.save()
        u_loc = UsuarioLocalizacao(id_usuario=user.id)
        u_loc.save()
post_save.connect(create_usuario, sender=User)
