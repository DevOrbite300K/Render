from django import forms
from django.contrib.auth.models import User
from cabinet.models import CustomUser
from django.contrib.auth.forms import AuthenticationForm

class UtilisateurForm(forms.ModelForm):
    class Meta:
        model=CustomUser
        fields=['username', 'email', 'password', 'first_name', 'last_name', 'is_staff', 'is_superuser', 'role']
        
        widgets = {
            'password': forms.PasswordInput(),
        }
        
class ModifierUtilisateurForm(forms.ModelForm):
    
        class Meta:
            model=CustomUser
            fields=['username', 'email', 'first_name', 'last_name', 'is_staff', 'is_superuser', 'is_active', 'role']
            
            
            

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': "Nom d'utilisateur",
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': "Mot de passe",
    }))
