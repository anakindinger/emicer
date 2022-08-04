import email
from django.contrib import admin

from .models import Formacao, Participante

class ParticipanteAdmin(admin.ModelAdmin):
    list_display = ('nome_completo', 'email')


admin.site.register(Participante, ParticipanteAdmin)
admin.site.register(Formacao)
