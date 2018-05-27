from djongo.models import Model as Document, CharField as StringField, IntegerField as IntField, ArrayModelField


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
        default=[]
    )

    class Meta:
        abstract = True


class MesLocalizacao(Document):
    value = IntField()
    dias = ArrayModelField(
        model_container=DiaLocalizacao,
        default=[]
    )

    class Meta:
        abstract = True


class AnoLocalizacao(Document):
    value = IntField()
    meses = ArrayModelField(
        model_container=MesLocalizacao,
        default=[]
    )

    class Meta:
        abstract = True


class UsuarioLocalizacao(Document):
    id_usuario = IntField(unique=True)
    anos = ArrayModelField(
        model_container=AnoLocalizacao,
        default=[]
    )

    def __str__(self):
        return "Localizações de {}".format(self.id_usuario)

    def get_ano_status(self, ano):
        for index in range(0, len(self.anos)):
            if self.anos[index].value == ano:
                return {'has': True, 'index': index}
        return {'has': False}

    def get_mes_status(self, ano_index, mes):
        for index in range(0, len(self.anos[ano_index].meses)):
            if self.anos[ano_index].meses[index].value == mes:
                return {'has': True, 'index': index}
        return {'has': False}

    def get_dia_status(self, ano_index, mes_index, dia):
        for index in range(0, len(self.anos[ano_index].meses[mes_index].dias)):
            if self.anos[ano_index].meses[mes_index].dias[index].value == dia:
                return {'has': True, 'index': index}
        return {'has': False}

    def get_time_status(self, ano_index, mes_index, dia_index, hora, minutos):
        for index in range(0, len(self.anos[ano_index].meses[mes_index].dias[dia_index].localizacoes)):
            if self.anos[ano_index].meses[mes_index].dias[dia_index].localizacoes[index].hora == hora \
                    and self.anos[ano_index].meses[mes_index].dias[dia_index].localizacoes[index].minutos == minutos:
                return {'has': True, 'index': index}
        return {'has': False}

    def get_data_status(self, ano, mes, dia, hora, minutos):
        msg = {'ano': self.get_ano_status(ano)}
        if msg['ano']['has']:
            msg['mes'] = self.get_mes_status(msg['ano']['index'], mes)
            if msg['mes']['has']:
                msg['dia'] = self.get_dia_status(msg['ano']['index'], msg['mes']['index'], dia)
                if msg['dia']['has']:
                    msg['time'] = self.get_time_status(msg['ano']['index'], msg['mes']['index'],
                                                       msg['dia']['index'], hora, minutos)
        return msg

    def add_localizacao(self, ano, mes, dia, localizacao):
        msg = {
            'ano': {'value': ano},
            'mes': {'value': mes},
            'dia': {'value': dia},
            'localizacao': {'value': localizacao}
        }
        data_status = self.get_data_status(ano, mes, dia, localizacao.hora, localizacao.minutos)
        msg['data_status'] = data_status

        if data_status['ano']['has']:
            ANO_INDEX = data_status['ano']['index']

            if data_status['mes']['has']:
                MES_INDEX = data_status['mes']['index']

                if data_status['dia']['has']:
                    DIA_INDEX = data_status['dia']['index']

                    if data_status['time']['has']:
                        TIME_INDEX = data_status['time']['index']

                        msg['localizacao']['old'] = self.anos[ANO_INDEX].meses[MES_INDEX]. \
                            dias[DIA_INDEX].localizacoes[TIME_INDEX]

                        self.anos[ANO_INDEX].meses[MES_INDEX].dias[DIA_INDEX].localizacoes[TIME_INDEX] = localizacao
                    else:
                        self.anos[ANO_INDEX].meses[MES_INDEX].dias[DIA_INDEX].localizacoes.append(localizacao)
                else:
                    self.anos[ANO_INDEX].meses[MES_INDEX].dias.append(
                        DiaLocalizacao(value=dia, localizacoes=[localizacao])
                    )
            else:
                self.anos[ANO_INDEX].meses.append(
                    MesLocalizacao(value=mes, dias=[
                        DiaLocalizacao(value=dia, localizacoes=[localizacao])
                    ])
                )
        else:
            self.anos.append(
                AnoLocalizacao(value=ano, meses=[
                    MesLocalizacao(value=mes, dias=[
                        DiaLocalizacao(value=dia, localizacoes=[localizacao])
                    ])
                ])
            )

        return msg

    class Meta:
        verbose_name = 'localizações usuário'
        verbose_name_plural = 'localizações usuários'
