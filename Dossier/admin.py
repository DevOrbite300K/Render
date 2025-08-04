# dossier/admin.py

from django.contrib import admin
from .models import Dossier

@admin.register(Dossier)
class DossierAdmin(admin.ModelAdmin):
    list_display = (
        'titre',
        'description',
        'date_ouverture',
        'date_cloture',
        'type_affaire',
        'statut_actuel',
        'clients_list',   # <-- méthode, pas le champ M2M
        'avocats_list',   # <-- méthode, pas le champ M2M
    )

    def clients_list(self, obj):
        # on récupère tous les clients liés et on les stringify
        return ", ".join(str(c) for c in obj.clients.all())
    clients_list.short_description = 'Clients'

    def avocats_list(self, obj):
        return ", ".join(str(a) for a in obj.avocats.all())
    avocats_list.short_description = 'Avocats'
