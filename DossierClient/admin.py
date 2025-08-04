from django.contrib import admin
from .models import DossierClient
# Register your models here.

admin.site.register(DossierClient, admin.ModelAdmin)
