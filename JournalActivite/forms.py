from django import forms
from .models import JournalActivite

class JournalActiviteForm(forms.ModelForm):
    class Meta:
        model = JournalActivite
        fields = ['type_action', 'détails', 'dossier']
        widgets = {
            'type_action': forms.Select(attrs={'class': 'form-control'}),
            'détails': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'dossier': forms.Select(attrs={'class': 'form-control'}),
        }
