from django.contrib import admin
from .models import DossierAvocat

@admin.register(DossierAvocat)
class DossierAvocatAdmin(admin.ModelAdmin):
    list_display = ('dossier', 'avocat', 'rôle_avocat')
    search_fields = ('dossier__titre', 'avocat__nom')
    list_filter = ('rôle_avocat',)