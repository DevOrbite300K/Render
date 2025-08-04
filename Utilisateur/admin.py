from django.contrib import admin



# Register your models here.

### enregistrer les models dans l'admin
from .models import Profile
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('utilsateur', 'bio', 'profile')
    search_fields = ('utilsateur__username', 'bio')
    list_filter = ('utilsateur__is_active',)
    
    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.select_related('utilsateur')