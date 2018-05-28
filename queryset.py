import django
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LocationTrackerAPI.settings")
django.setup()

from django.db import IntegrityError
from djongo.sql2mongo import SQLDecodeError
from location.models import UsuarioLocalizacao
from datetime import date, datetime

locs = UsuarioLocalizacao.objects.filter(anos=2018)
print(locs)
for loc in locs:
    print(loc)

print('end')