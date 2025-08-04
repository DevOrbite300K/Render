from django import forms
from .models import Paiement

class PaiementForm(forms.ModelForm):
    class Meta:
        model = Paiement
        fields = [
            'dossier',
            'client',
            'montant',
            'moyen_paiement',
        ]
        widgets = {
            'dossier': forms.Select(attrs={'class': 'form-control'}),
            'client': forms.Select(attrs={'class': 'form-control'}),
            'montant': forms.NumberInput(attrs={
                'class': 'form-control',
                'step': '0.01',
                'min': '0'
            }),
            'moyen_paiement': forms.Select(attrs={'class': 'form-control'}),
        }

    def clean_montant(self):
        montant = self.cleaned_data.get('montant')
        if montant is not None and montant <= 0:
            raise forms.ValidationError("Le montant doit être supérieur à zéro.")
        return montant
