from django.contrib import admin

from .models import JournalActivite

# en une seule ligne, sans créer de nouvelle classe ni utiliser de décorateur
admin.site.register(JournalActivite, admin.ModelAdmin)