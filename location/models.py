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

    def _vefify_ano(self, ano):
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

    def _create_hora(self, hora, loc):
        h = HoraLocalizacao(value=hora)
        h.localizacoes[loc.minutos] = loc
        return h

    def _create_dia(self, dia, hora, loc):
        d = DiaLocalizacao(value=dia)
        h = self._create_hora(hora, loc)
        d.horas[h.value] = h
        return d

    def _create_mes(self, mes, dia, hora, loc):
        m = MesLocalizacao(value=mes)
        d = self._create_dia(dia, hora, loc)
        m.dias[d.value] = d
        return m

    def _create_ano(self, ano, mes, dia, hora, loc):
        a = AnoLocalizacao(value=ano)
        m = self._create_mes(mes, dia, hora, loc)
        a.meses[m.value] = m
        return a

    def add_location(self, ano, mes, dia, hora, loc):
        if self._vefify_ano(ano):
            print('has ano')
            if self._verify_mes(ano, mes):
                print('has mes')
                if self._verify_dia(ano, mes, dia):
                    print('has dia')
                    if self._verify_hora(ano, mes, dia, hora):
                        print('has hora')
                        self.anos[ano].meses[mes].dias[dia].horas[hora].localizacoes[loc.minutos] = loc
                    else:
                        print('create hora')
                        self.anos[ano].meses[mes].dias[dia].horas[hora] = self._create_hora(hora, loc)
                else:
                    print('create dia')
                    self.anos[ano].meses[mes].dias[dia] = self._create_dia(dia, hora, loc)
            else:
                print('create mes')
                self.anos[ano].meses[mes] = self._create_mes(mes, dia, hora, loc)
        else:
            print('create ano')
            self.anos[ano] = self._create_ano(ano, mes, dia, hora, loc)
