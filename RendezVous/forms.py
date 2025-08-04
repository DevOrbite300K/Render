# RendezVous/forms.py

from django import forms
from .models import RendezVous

class RendezVousForm(forms.ModelForm):
    class Meta:
        model = RendezVous
        fields = [
            'objet',
            'date_rdv',
            'heure_rdv',
            'lieu',
            'statut_rdv',
            'dossier',
            'client',
            'avocat',
        ]
        widgets = {
            'objet': forms.TextInput(attrs={'class': 'form-control'}),
            'date_rdv': forms.DateInput(
                attrs={'type': 'date', 'class': 'form-control'}
            ),
            'heure_rdv': forms.TimeInput(
                attrs={'type': 'time', 'class': 'form-control'}
            ),
            'lieu': forms.TextInput(attrs={'class': 'form-control'}),
            'statut_rdv': forms.Select(attrs={'class': 'form-control'}),
            'dossier': forms.Select(attrs={'class': 'form-control'}),
            'client': forms.Select(attrs={'class': 'form-control'}),
            'avocat': forms.Select(attrs={'class': 'form-control'}),
        }
        labels = {
            'date_rdv': "Date du rendez-vous",
            'heure_rdv': "Heure du rendez-vous",
        }
