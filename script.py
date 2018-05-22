import django
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LocationTrackerAPI.settings")
django.setup()

from django.contrib.auth.models import User
from django.db import IntegrityError
from core.models import Usuario, Familia
from location.models import Localizacao


# users = User.objects.all()
# for user in users:
#     print(user)

DATA_LOCAL = "2018-05-22T17:06:20.976000Z"

l1 = Localizacao(data=DATA_LOCAL, lat='lat1', long='long1', id_usuario=1)
l1.save()

l2 = Localizacao(data=DATA_LOCAL, lat='lat2', long='long2', id_usuario=2)
l2.save()


familia = Familia(nome='Familia teste')
try:
    familia.save()
except IntegrityError as e:
    familia = Familia.objects.get(nome='Familia teste')
    print(e)




rodrigo_perfil = User(username='rodrigondec', email='rodrigondec@gmail.com',
                password='pbkdf2_sha256$100000$fQgW32ScWiVI$n3psZOWZvSqL8154DXXEBlRxpr1r57f6ANQSnF+qPU8=',
                is_staff=True, is_superuser=True)
try:
    rodrigo_perfil.save()
except IntegrityError as e:
    rodrigo_perfil = User.objects.get(username='rodrigondec')
    print(e)

rodrigo = Usuario(perfil_user=rodrigo_perfil)
rodrigo.familia = familia
try:
    rodrigo.save()
except IntegrityError as e:
    rodrigo = Usuario.objects.get(perfil_user=rodrigo_perfil)
    print(e)



wesley_perfil = User(username='wreuel', email='wreuel@gmail.com',
                password='pbkdf2_sha256$100000$qLFj32fUzB19$IvReZO0pOWCtsxYMk4j/0yUKqvkIHBzqGjpXHPhHzp8=',
                is_staff=True, is_superuser=True)
try:
    wesley_perfil.save()
except IntegrityError as e:
    wesley_perfil = User.objects.get(username='wreuel')
    print(e)

wesley = Usuario(perfil_user=wesley_perfil)
wesley.familia = familia
try:
    wesley.save()
except IntegrityError as e:
    wesley = Usuario.objects.get(perfil_user=wesley_perfil)
    print(e)