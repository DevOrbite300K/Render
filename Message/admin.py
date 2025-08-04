from django.contrib import admin
from .models import Message

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('utilisateur', 'dossier', 'date_creation', 'lu')
    list_filter = ('lu', 'date_creation')
    search_fields = ('message', 'utilisateur__username')
    date_hierarchy = 'date_creation'
    actions = ['mark_as_read']

    def mark_as_read(self, request, queryset):
        updated = queryset.update(lu=True)
        self.message_user(request, f"{updated} message(s) marqué(s) comme lu(s).")
    mark_as_read.short_description = "Marquer sélection comme lue"
