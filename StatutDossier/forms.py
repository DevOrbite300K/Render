from django import forms
from django.forms import ModelForm

from .models import StatutDossier

class StatutDossierForm(ModelForm):
    class Meta:
        model = StatutDossier
        fields = ['libelle']
        widgets = {
            'libelle': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Libellé du statut'}),
        }
        
