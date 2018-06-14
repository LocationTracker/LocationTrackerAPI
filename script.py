import django
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LocationTrackerAPI.settings")
django.setup()

from django.contrib.auth.models import User
from django.db import IntegrityError
from mongoengine.errors import NotUniqueError
from core.models import PerfilUsuario, Familia
from location.models import Localizacao, DiaLocalizacao, MesLocalizacao, AnoLocalizacao, UsuarioLocalizacao
from datetime import date, datetime


# users = User.objects.all()
# for user in users:
#     print(user)

ANO_LOCAL = '2018'
MES_LOCAL = '05'
DIA_LOCAL = '29'

HORA_LOCAL = '19'
MINUTOS_LOCAL = '05'

LAT_LOCAL = 'lat'
LONG_LOCAL = 'long'

ul1 = UsuarioLocalizacao(id_usuario=1)
try:
    ul1.save()
except NotUniqueError as e:
    ul1 = UsuarioLocalizacao.objects.get(id_usuario=1)
    # print(e)

ul1.add_location(ANO_LOCAL, MES_LOCAL, DIA_LOCAL, HORA_LOCAL, MINUTOS_LOCAL, LAT_LOCAL, LONG_LOCAL)
ul1.add_location('2018', '03', '15', '18', '05', LAT_LOCAL, LONG_LOCAL)
ul1.add_location('2018', '03', '15', '18', '10', LAT_LOCAL, LONG_LOCAL)
ul1.add_location('2018', '03', '15', '19', '05', LAT_LOCAL, LONG_LOCAL)
ul1.add_location('2018', '03', '15', '19', '10', LAT_LOCAL, LONG_LOCAL)
ul1.add_location('2018', '03', '16', '19', '05', LAT_LOCAL, LONG_LOCAL)
ul1.add_location('2018', '03', '16', '19', '10', LAT_LOCAL, LONG_LOCAL)
ul1.add_location('2018', '04', '16', '19', '05', LAT_LOCAL, LONG_LOCAL)
ul1.add_location('2018', '04', '16', '19', '10', LAT_LOCAL, LONG_LOCAL)
ul1.save()

ul2 = UsuarioLocalizacao(id_usuario=2)
try:
    ul2.save()
except NotUniqueError as e:
    ul2 = UsuarioLocalizacao.objects.get(id_usuario=2)
    # print(e)

ul2.add_location(ANO_LOCAL, MES_LOCAL, DIA_LOCAL, HORA_LOCAL, MINUTOS_LOCAL, LAT_LOCAL, LONG_LOCAL)
ul2.add_location('2018', '03', '15', '18', '05', LAT_LOCAL, LONG_LOCAL)
ul2.add_location('2018', '03', '15', '18', '10', LAT_LOCAL, LONG_LOCAL)
ul2.add_location('2018', '03', '15', '19', '05', LAT_LOCAL, LONG_LOCAL)
ul2.add_location('2018', '03', '15', '19', '10', LAT_LOCAL, LONG_LOCAL)
ul2.add_location('2018', '03', '16', '19', '05', LAT_LOCAL, LONG_LOCAL)
ul2.add_location('2018', '03', '16', '19', '10', LAT_LOCAL, LONG_LOCAL)
ul2.add_location('2018', '04', '16', '19', '05', LAT_LOCAL, LONG_LOCAL)
ul2.add_location('2018', '04', '16', '19', '10', LAT_LOCAL, LONG_LOCAL)
ul2.save()

familia = Familia(nome='Familia teste')
try:
    familia.save()
except IntegrityError as e:
    familia = Familia.objects.get(nome='Familia teste')
    # print(e)




rodrigo = User(username='rodrigondec', email='rodrigondec@gmail.com',
                password='pbkdf2_sha256$100000$fQgW32ScWiVI$n3psZOWZvSqL8154DXXEBlRxpr1r57f6ANQSnF+qPU8=',
                is_staff=True, is_superuser=True)
try:
    rodrigo.save()
except IntegrityError as e:
    rodrigo = User.objects.get(username='rodrigondec')
    # print(e)

rodrigo.perfil.familia = familia
rodrigo.perfil.save()


wesley = User(username='wreuel', email='wreuel@gmail.com',
                password='pbkdf2_sha256$100000$qLFj32fUzB19$IvReZO0pOWCtsxYMk4j/0yUKqvkIHBzqGjpXHPhHzp8=',
                is_staff=True, is_superuser=True)
try:
    wesley.save()
except IntegrityError as e:
    wesley = User.objects.get(username='wreuel')
    # print(e)

wesley.perfil.familia = familia
wesley.perfil.save()