from django.db import models

# 

class Participante(models.Model):
    nome_completo = models.CharField('Nome completo', max_length=100)
    email = models.EmailField('E-mail', max_length=70)
    formacoes = models.ManyToManyField('Formacao', through = 'FormacaoParticipantes')

    def __str__(self):
        return f'Nome : {self.nome_completo}, E-mail: {self.email}'


class Formacao(models.Model):
    titulo = models.CharField('Titulo', max_length = 300)
    data = models.DateField('Data')
    duracao = models.DurationField('Duração')
    participantes = models.ManyToManyField(Participante, through = 'FormacaoParticipantes')

class FormacaoParticipantes(models.Model):
    formacao = models.ForeignKey('Formacao', on_delete = models.CASCADE)
    participantes = models.ForeignKey('Participante', on_delete = models.CASCADE)