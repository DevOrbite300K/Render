from django.contrib import admin

# Register your models here.

from .models import Document
@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('nom_fichier', 'fichier', 'type_document', 'date_ajout', 'dossier', 'utilisateur')
    search_fields = ('nom_fichier', 'fichier', 'type_document', 'date_ajout', 'dossier__titre')
    list_filter = ('dossier', 'utilisateur')
    
    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.select_related('dossier')


