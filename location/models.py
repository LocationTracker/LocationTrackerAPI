from djongo.models import Model as Document, CharField as StringField, IntegerField as IntField, ArrayModelField
from dateutil.parser import parse as DateParse


class Localizacao(Document):
    hora = IntField()
    minutos = IntField()
    lat = StringField(max_length=30)
    long = StringField(max_length=30)

    def __str__(self):
        return "{}:{} - {} e {}".format(self.hora, self.minutos, self.lat, self.long)

    class Meta:
        unique_together = ('hora', 'minutos')
        abstract = True


class DiaLocalizacao(Document):
    value = IntField()
    localizacoes = ArrayModelField(
        model_container=Localizacao,
    )

    class Meta:
        abstract = True


class MesLocalizacao(Document):
    value = IntField()
    dias = ArrayModelField(
        model_container=DiaLocalizacao,
    )

    class Meta:
        abstract = True


class AnoLocalizacao(Document):
    value = IntField()
    meses = ArrayModelField(
        model_container=DiaLocalizacao,
    )

    class Meta:
        abstract = True


class UsuarioLocalizacao(Document):
    id_usuario = IntField(unique=True)
    anos = ArrayModelField(
        model_container=AnoLocalizacao,
    )

    def __str__(self):
        return "Localizações de {}".format(self.id_usuario)

    def get_data_index(self, data):
        for index in range(0, len(self.datas)):
            data_self = self.datas[index].data
            bool = self.datas[index].data == data
            if self.datas[index].data == data:
                return {'has': True, 'index': index}
        return {'has': False}

    def get_time_index(self, index_data, hora, minutos):
        for index in range(0, len(self.datas[index_data].localizacoes)):
            if self.datas[index_data].localizacoes[index].hora == hora and \
               self.datas[index_data].localizacoes[index].minutos == minutos:
                return {'has': True, 'index': index}
        return {'has': False}

    def get_ano_index(self, ano):
        for index in range(0, len(self.anos)):
            if self.anos[index].value == ano:
                return {'has': True, 'index': index}
        return {'has': False}

    def get_mes_index(self, ano_index, mes):
        for index in range(0, len(self.anos[ano_index])):
            if self.anos[ano_index].meses[index].value == mes:
                return {'has': True, 'index': index}
        return {'has': False}

    def get_dia_index(self, ano_index, mes_index, dia):
        for index in range(0, len(self.anos[ano_index].meses[mes_index])):
            if self.anos[ano_index].meses[index].value == mes:
                return {'has': True, 'index': index}
        return {'has': False}

    def add_localizacao(self, ano, mes, dia, localizacao):
        msg = {
            'ano': {'value': ano},
            'mes': {'value': mes},
            'dia': {'value': dia},
            'localizacao': {
                'value': localizacao
            }
        }
        data_status = self.get_data_index(data)
        msg['data']['data_status'] = data_status

        if data_status['has']:
            time_status = self.get_time_index(data_status['index'], localizacao.hora, localizacao.minutos)
            msg['localizacao']['time_status'] = time_status

            if time_status['has']:
                msg['localizacao']['old'] = self.datas[data_status['index']].localizacoes[time_status['index']]
                self.datas[data_status['index']].localizacoes[time_status['index']] = localizacao
            else:
                self.datas[data_status['index']].localizacoes.append(localizacao)
        else:
            self.datas.append(DataLocalizacao(data=data, localizacoes=[localizacao]))

        return msg

    class Meta:
        verbose_name = 'localizações usuário'
        verbose_name_plural = 'localizações usuários'
