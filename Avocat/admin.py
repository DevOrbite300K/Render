from django.contrib import admin

# Register your models here.
# enregistrer les models dans l'admin en utilisant register
from .models import Avocat
@admin.register(Avocat)
class AvocatAdmin(admin.ModelAdmin):
    list_display = ('telephone', 'adresse', 'photo', 'utilisateur')
    search_fields = ('telephone', 'adresse', 'photo')
    list_filter = ('utilisateur',)
    
    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.select_related('utilisateur')