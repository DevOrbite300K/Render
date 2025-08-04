
from .models import Publication, Expert, MembreDirectoire, Contact
from django.contrib import admin
    
@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    list_display = ('titre', 'auteur', 'date_publication')
    search_fields = ('titre', 'auteur')
    
    
@admin.register(Expert)
class ExpertAdmin(admin.ModelAdmin):
    list_display = ('nom', 'titre')
    search_fields = ('nom', 'titre')
    


@admin.register(MembreDirectoire)
class MembreDirectoireAdmin(admin.ModelAdmin):
    list_display = ('nom', 'fonction')
    search_fields = ('nom', 'fonction')
    
    

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('nom', 'email', 'sujet', 'date_envoi')
    search_fields = ('nom', 'email', 'sujet')



