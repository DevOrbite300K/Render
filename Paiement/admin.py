from django.contrib import admin
from .models import Paiement

@admin.register(Paiement)
class PaiementAdmin(admin.ModelAdmin):
    list_display = (
        'client', 'montant', 'date_paiement', 'moyen_paiement'
    )
    list_filter = ('moyen_paiement',)
    search_fields = ('client__nom',)
    readonly_fields = ('date_paiement',)
