import email
from django.contrib import admin

from .models import Participante

class ParticipanteAdmin(admin.ModelAdmin):
    list_display = ('nome_completo', 'email')


admin.site.register(Participante, ParticipanteAdmin)
