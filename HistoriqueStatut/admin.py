from django.contrib import admin

from .models import HistoriqueStatut

# en une seule ligne, sans créer de nouvelle classe ni utiliser de décorateur
admin.site.register(HistoriqueStatut, admin.ModelAdmin)