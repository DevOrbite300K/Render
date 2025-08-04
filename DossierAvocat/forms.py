from django import forms
from .models import DossierAvocat

class DossierAvocatForm(forms.ModelForm):
    class Meta:
        model = DossierAvocat
        fields = ['dossier', 'avocat', 'rôle_avocat']
        widgets = {
            'dossier': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': 'Sélectionne le dossier'
            }),
            'avocat': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': 'Choisis un avocat'
            }),
            'rôle_avocat': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': 'Rôle de l’avocat'
            }),
        }
