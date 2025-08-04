from django.contrib import admin

# Register your models here.

## enregistrer le modele dans admin

from .models import Audience
@admin.register(Audience)
class AudienceAdmin(admin.ModelAdmin):
    list_display = ('date', 'lieu', 'dossier')
    search_fields = ('date', 'lieu', 'dossier__titre')
    list_filter = ('dossier',)
    
    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.select_related('dossier')
