from django.db import models

# 

class Participante(models.Model):
    nome_completo = models.CharField('Nome completo', max_length=100)
    email = models.CharField('E-mail', max_length=70)
    




