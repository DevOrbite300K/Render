from django import forms
from django.forms import ModelForm
from .models import EntrepriseCreer, Etude, Formation

class EntrepriseCreerForm(ModelForm):
    class Meta:
        model = EntrepriseCreer
        fields = [
            'denomination',
            'numeroRCCM',
            'numeroNIF',
            'siege',
            'nomGerant',
            'adresseGerant',
            'emailGerant',
            'telephoneGerant',
            'date_creation',
            'documentation'
        ]
        widgets = {
            'date_creation': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'documentation': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'denomination': forms.TextInput(attrs={'class': 'form-control'}),
            'numeroRCCM': forms.TextInput(attrs={'class': 'form-control'}),
            'numeroNIF': forms.TextInput(attrs={'class': 'form-control'}),
            'siege': forms.TextInput(attrs={'class': 'form-control'}),
            'nomGerant': forms.TextInput(attrs={'class': 'form-control'}),
            'adresseGerant': forms.TextInput(attrs={'class': 'form-control'}),
            'emailGerant': forms.EmailInput(attrs={'class': 'form-control'}),
            'telephoneGerant': forms.TextInput(attrs={'class': 'form-control'}),
        }
        
        

class EtudeForm(ModelForm):
    class Meta:
        model = Etude
        fields = [
            'intitule',
            'date_debut',
            'date_fin',
            'lieu',
            'commanditaire',
            'document'
        ]
        widgets = {
            'date_debut': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'date_fin': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'document': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'intitule': forms.TextInput(attrs={'class': 'form-control'}),
            'lieu': forms.TextInput(attrs={'class': 'form-control'}),
            'commanditaire': forms.TextInput(attrs={'class': 'form-control'}),
        }
        
        
class FormationForm(ModelForm):
    class Meta:
        model = Formation
        fields = [
            'type',
            'theme',
            'nombre_participants',
            'date_debut',
            'date_fin',
            'lieu',
            'document'
        ]
        widgets = {
            'date_debut': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'date_fin': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'document': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'theme': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre_participants': forms.NumberInput(attrs={'class': 'form-control'}),
            'lieu': forms.TextInput(attrs={'class': 'form-control'}),
            'type': forms.Select(attrs={'class': 'form-control'}),
        }