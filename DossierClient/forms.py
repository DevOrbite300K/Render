from django import forms
from .models import DossierClient

class DossierClientForm(forms.ModelForm):
    class Meta:
        model = DossierClient
        fields = ['dossier', 'client', 'rôle_client']
        widgets = {
            'dossier': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': 'Sélectionner le dossier',
                'required': True
            }),
            'client': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': 'Choisir un client',
                'required': True
            }),
            'rôle_client': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': 'Indiquer le rôle du client',
                'required': True
            }),
        }

        

