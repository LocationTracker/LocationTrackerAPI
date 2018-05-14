from djongo.models import Model as Document, CharField as StringField, IntegerField as IntField, DateField


class Localizacao(Document):
    id_usuario = IntField()
    data = DateField()
    lat = StringField(max_length=30)
    long = StringField(max_length=30)
