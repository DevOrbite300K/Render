from django import forms
from .models import TypeAffaire


class TypeAffaireForm(forms.ModelForm):
    class Meta:
        model = TypeAffaire
        fields = ['libelle']
        labels = {
            'libelle': 'Libellé de l’affaire',
        }
        widgets = {
            'libelle': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Entrez le libellé ici',
                'style': 'max-width: 850px;'
            }),
        }

        
        
