from django.contrib import admin
from .models import TypeAffaire

@admin.register(TypeAffaire)
class TypeAffaireAdmin(admin.ModelAdmin):
    list_display    = ('libelle',)
    search_fields   = ('libelle',)
    ordering        = ('libelle',)
    list_per_page   = 25
