import email
from django.contrib import admin

from .models import Formacao, Participante, FormacaoParticipantes

class ParticipanteAdmin(admin.ModelAdmin):
    list_display = ('nome_completo', 'email')


admin.site.register(Participante, ParticipanteAdmin)
admin.site.register(Formacao)
admin.site.register(FormacaoParticipantes)
