
from django.contrib import admin
from .models import StatutDossier

@admin.register(StatutDossier)
class StatutDossierAdmin(admin.ModelAdmin):
    list_display   = ('libelle',)
    search_fields  = ('libelle',)
    ordering       = ('libelle',)
    list_per_page  = 25
