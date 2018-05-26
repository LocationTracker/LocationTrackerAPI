import django
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LocationTrackerAPI.settings")
django.setup()

from django.contrib.auth.models import User
from django.db import IntegrityError
from djongo.sql2mongo import SQLDecodeError
from core.models import PerfilUsuario, Familia
from location.models import Localizacao, DiaLocalizacao, MesLocalizacao, AnoLocalizacao, UsuarioLocalizacao
from datetime import date, datetime


# users = User.objects.all()
# for user in users:
#     print(user)

ANO_LOCAL = 2018
MES_LOCAL = 5
DIA_LOCAL = 26

HORA_LOCAL = 18
MINUTOS_LOCAL = 1

l = Localizacao(hora=HORA_LOCAL, minutos=MINUTOS_LOCAL, lat='lat1', long='long1')
dl = DiaLocalizacao(value=DIA_LOCAL, localizacoes=[l])
ml = MesLocalizacao(value=MES_LOCAL, dias=[dl])
al = AnoLocalizacao(value=ANO_LOCAL, meses=[ml])

ul1 = UsuarioLocalizacao(id_usuario=1, anos=[al])
try:
    ul1.save()
except SQLDecodeError as e:
    ul1 = UsuarioLocalizacao.objects.get(id_usuario=1)
    print(e)

ul2 = UsuarioLocalizacao(id_usuario=2, anos=[al])
try:
    ul2.save()
except SQLDecodeError as e:
    ul2 = UsuarioLocalizacao.objects.get(id_usuario=2)
    print(e)


familia = Familia(nome='Familia teste')
try:
    familia.save()
except IntegrityError as e:
    familia = Familia.objects.get(nome='Familia teste')
    print(e)




rodrigo = User(username='rodrigondec', email='rodrigondec@gmail.com',
                password='pbkdf2_sha256$100000$fQgW32ScWiVI$n3psZOWZvSqL8154DXXEBlRxpr1r57f6ANQSnF+qPU8=',
                is_staff=True, is_superuser=True)
try:
    rodrigo.save()
except IntegrityError as e:
    rodrigo = User.objects.get(username='rodrigondec')
    print(e)

rodrigo.perfil.familia = familia
rodrigo.perfil.save()


wesley = User(username='wreuel', email='wreuel@gmail.com',
                password='pbkdf2_sha256$100000$qLFj32fUzB19$IvReZO0pOWCtsxYMk4j/0yUKqvkIHBzqGjpXHPhHzp8=',
                is_staff=True, is_superuser=True)
try:
    wesley.save()
except IntegrityError as e:
    wesley = User.objects.get(username='wreuel')
    print(e)

wesley.perfil.familia = familia
wesley.perfil.save()