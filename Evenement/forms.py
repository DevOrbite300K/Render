# Evenement/forms.py

from django import forms
from .models import Evenement

class EvenementForm(forms.ModelForm):
    class Meta:
        model = Evenement
        fields = [
            'titre',
            'description',
            'date_evenement',
            'type_evenement',
            'dossier',
            'utilisateur',
        ]
        widgets = {
            'titre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Titre de l’évènement'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Décrivez l’évènement…'
            }),
            'date_evenement': forms.DateTimeInput(attrs={
                'type': 'datetime-local',
                'class': 'form-control'
            }),
            'type_evenement': forms.Select(attrs={'class': 'form-control'}),
            'dossier': forms.Select(attrs={'class': 'form-control'}),
            'utilisateur': forms.Select(attrs={'class': 'form-control'}),
        }
        labels = {
            'date_evenement': "Date et heure",
            'type_evenement': "Type d’évènement",
        }

    def clean_date_evenement(self):
        dt = self.cleaned_data.get('date_evenement')
        if dt and dt < forms.fields.datetime.datetime.now():
            raise forms.ValidationError("La date de l’évènement doit être dans le futur.")
        return dt
