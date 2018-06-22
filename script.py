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

rodrigo.perfil.add_location('2018', '03', '15', '18', '05', 'lat', 'long')
rodrigo.perfil.add_location('2018', '03', '15', '18', '10', 'lat', 'long')
rodrigo.perfil.add_location('2018', '03', '15', '19', '05', 'lat', 'long')
rodrigo.perfil.add_location('2018', '03', '15', '19', '10', 'lat', 'long')
rodrigo.perfil.add_location('2018', '03', '16', '19', '05', 'lat', 'long')
rodrigo.perfil.add_location('2018', '03', '16', '19', '10', 'lat', 'long')
rodrigo.perfil.add_location('2018', '04', '16', '19', '05', 'lat', 'long')
rodrigo.perfil.add_location('2018', '04', '16', '19', '10', 'lat', 'long')
rodrigo.perfil.add_location('2018', '05', '29', '19', '10', 'lat', 'long')
rodrigo.perfil.add_location('2018', '06', '21', '23', '05', 'lat', 'long')

wesley = User(username='wreuel', email='wreuel@gmail.com',
                password='pbkdf2_sha256$100000$7lSwbqrzEtVE$MZQaFjFVC6LFSyuecwo4FwlNej3+H0V2oDB+QYmJYyo=',
                is_staff=True, is_superuser=True)
try:
    wesley.save()
except IntegrityError as e:
    wesley = User.objects.get(username='wreuel')
    # print(e)

wesley.perfil.familia = familia
wesley.perfil.save()

wesley.perfil.add_location('2018', '03', '15', '18', '05', 'lat', 'long')
wesley.perfil.add_location('2018', '03', '15', '18', '10', 'lat', 'long')
wesley.perfil.add_location('2018', '03', '15', '19', '05', 'lat', 'long')
wesley.perfil.add_location('2018', '03', '15', '19', '10', 'lat', 'long')
wesley.perfil.add_location('2018', '03', '16', '19', '05', 'lat', 'long')
wesley.perfil.add_location('2018', '03', '16', '19', '10', 'lat', 'long')
wesley.perfil.add_location('2018', '04', '16', '19', '05', 'lat', 'long')
wesley.perfil.add_location('2018', '04', '16', '19', '10', 'lat', 'long')
wesley.perfil.add_location('2018', '05', '29', '19', '10', 'lat', 'long')
wesley.perfil.add_location('2018', '06', '21', '23', '05', 'lat', 'long')
