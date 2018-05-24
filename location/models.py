from djongo.models import Model as Document, CharField as StringField, IntegerField as IntField, DateTimeField, DateField

class LocalizacaoUsuario(Document):
    id_usuario = IntField()
    # DataLocalizacao

class DataLocalizacao(Document):
    data = DateField()
    # Localizacao

class Localizacao(Document):
    data = DateTimeField()
    
    lat = StringField(max_length=30)
    long = StringField(max_length=30)

    def __str__(self):
        return "Localização do usuario {} na data {}".format(self.id_usuario, self.data)

    class Meta:
        verbose_name = 'localização'
        verbose_name_plural = 'localizações'
