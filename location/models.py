from mongoengine import Document, EmbeddedDocument, StringField, IntField, EmbeddedDocumentField, EmbeddedDocumentListField, MapField


class Localizacao(EmbeddedDocument):
    minutos = StringField()
    lat = StringField()
    long = StringField()

    def __str__(self):
        return "{} - {} e {}".format(self.minutos, self.lat, self.long)


class HoraLocalizacao(EmbeddedDocument):
    value = StringField()
    localizacoes = MapField(EmbeddedDocumentField(Localizacao))

    def __str__(self):
        return 'Hora {}'.format(self.value)


class DiaLocalizacao(EmbeddedDocument):
    value = StringField()
    horas = MapField(EmbeddedDocumentField(HoraLocalizacao))

    def __str__(self):
        return 'Dia {}'.format(self.value)


class MesLocalizacao(EmbeddedDocument):
    value = StringField()
    dias = MapField(EmbeddedDocumentField(DiaLocalizacao))

    def __str__(self):
        return 'Mes {}'.format(self.value)


class AnoLocalizacao(EmbeddedDocument):
    value = StringField()
    meses = MapField(EmbeddedDocumentField(MesLocalizacao))

    def __str__(self):
        return 'Ano {}'.format(self.value)


class UsuarioLocalizacao(Document):
    id_usuario = IntField(unique=True)
    anos = MapField(EmbeddedDocumentField(AnoLocalizacao))

    def __str__(self):
        return "Localizações de {}".format(self.id_usuario)

    def _verify_ano(self, ano):
        if ano in self.anos:
            return True
        return False

    def _verify_mes(self, ano, mes):
        if mes in self.anos[ano].meses:
            return True
        return False

    def _verify_dia(self, ano, mes, dia):
        if dia in self.anos[ano].meses[mes].dias:
            return True
        return False

    def _verify_hora(self, ano, mes, dia, hora):
        if hora in self.anos[ano].meses[mes].dias[dia].horas:
            return True
        return False

    def _verify_minutos(self, ano, mes, dia, hora, minutos):
        if minutos in self.anos[ano].meses[mes].dias[dia].horas[hora].localizacoes[minutos]:
            return True
        return False

    def _create_localizacao(self, minutos, lat, long):
        return Localizacao(minutos=minutos, lat=lat, long=long)

    def _create_hora(self, hora, minutos, lat, long):
        h = HoraLocalizacao(value=hora)
        h.localizacoes[minutos] = self._create_localizacao(minutos, lat, long)
        return h

    def _create_dia(self, dia, hora, minutos, lat, long):
        d = DiaLocalizacao(value=dia)
        h = self._create_hora(hora, minutos, lat, long)
        d.horas[h.value] = h
        return d

    def _create_mes(self, mes, dia, hora, minutos, lat, long):
        m = MesLocalizacao(value=mes)
        d = self._create_dia(dia, hora, minutos, lat, long)
        m.dias[d.value] = d
        return m

    def _create_ano(self, ano, mes, dia, hora, minutos, lat, long):
        a = AnoLocalizacao(value=ano)
        m = self._create_mes(mes, dia, hora, minutos, lat, long)
        a.meses[m.value] = m
        return a

    def get_ano(self, ano):
        if self._verify_ano(ano):
            return self.anos[ano]
        return None

    def get_mes(self, ano, mes):
        if self._verify_mes(ano, mes):
            return self.anos[ano].meses[mes]
        return None

    def get_dia(self, ano, mes, dia):
        if self._verify_dia(ano, mes, dia):
            return self.anos[ano].meses[mes].dias[dia]
        return None

    def get_hora(self, ano, mes, dia, hora):
        if self._verify_hora(ano, mes, dia, hora):
            return self.anos[ano].meses[mes].dias[dia].horas[hora]
        return None

    def get_minutos(self, ano, mes, dia, hora, minutos):
        if self._verify_minutos(ano, mes, dia, hora, minutos):
            return self.anos[ano].meses[mes].dias[dia].horas[hora].localizacoes[minutos]
        return None

    def add_location(self, ano, mes, dia, hora, minutos, lat, long):
        if self._verify_ano(ano):
            print('has ano')
            if self._verify_mes(ano, mes):
                print('has mes')
                if self._verify_dia(ano, mes, dia):
                    print('has dia')
                    if self._verify_hora(ano, mes, dia, hora):
                        print('has hora')
                        self.anos[ano].meses[mes].dias[dia].horas[hora].localizacoes[minutos] = self._create_localizacao(minutos, lat, long)
                    else:
                        print('create hora')
                        self.anos[ano].meses[mes].dias[dia].horas[hora] = self._create_hora(hora, minutos, lat, long)
                else:
                    print('create dia')
                    self.anos[ano].meses[mes].dias[dia] = self._create_dia(dia, hora, minutos, lat, long)
            else:
                print('create mes')
                self.anos[ano].meses[mes] = self._create_mes(mes, dia, hora, minutos, lat, long)
        else:
            print('create ano')
            self.anos[ano] = self._create_ano(ano, mes, dia, hora, minutos, lat, long)

    def add_location_data(self, data):
        self.add_location(data['ano'], data['mes'], data['dia'], data['hora'], data['minutos'], data['lat'], data['long'])
