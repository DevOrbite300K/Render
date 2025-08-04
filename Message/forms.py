from django import forms
from .models import Message

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = [
            'dossier',
            'utilisateur',
            'message',
            'lu',
        ]
        widgets = {
            'dossier': forms.Select(attrs={'class': 'form-control'}),
            'utilisateur': forms.Select(attrs={'class': 'form-control'}),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Écrire votre message…'
            }),
            'lu': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
        labels = {
            'lu': 'Lu ?',
        }

class MessageFormEnvoie(forms.ModelForm):
    class Meta:
        model = Message
        fields = [
            'dossier',
            'utilisateur',
            'message',
            
        ]
        widgets = {
            'dossier': forms.Select(attrs={'class': 'form-control'}),
            'utilisateur': forms.Select(attrs={'class': 'form-control'}),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Écrire votre message…'
            }),
        }
        


