from django.contrib import admin
from .models import RendezVous

@admin.register(RendezVous)
class RendezVousAdmin(admin.ModelAdmin):
    list_display = (
        'objet', 'date_rdv', 'heure_rdv', 'statut_rdv',
        'dossier', 'client', 'avocat'
    )
    list_filter = ('statut_rdv', 'date_rdv')
    search_fields = ('objet', 'lieu')
    ordering = ('-date_rdv', 'heure_rdv')
