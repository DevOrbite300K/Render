from django.contrib import admin
from .models import Evenement

@admin.register(Evenement)
class EvenementAdmin(admin.ModelAdmin):
    list_display = (
        'titre', 'date_evenement', 'type_evenement', 'dossier', 'utilisateur'
    )
    list_filter = ('type_evenement', 'date_evenement')
    search_fields = ('titre', 'description')
    date_hierarchy = 'date_evenement'
