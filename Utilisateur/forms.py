from django.forms import ModelForm
from cabinet.models import CustomUser
from django import forms


## formulaire de creation d'un utilisateur

from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser  # adapte selon ton projet

class UtilisateurCreationForm(UserCreationForm):
    
    password1 = forms.CharField(
        label="Mot de passe",
        strip=False,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control password-field',
            'placeholder': '••••••••',
            'autocomplete': 'new-password',
            'data-toggle': 'password'
        }),
        help_text="Entrez un mot de passe fort.",
    )
    password2 = forms.CharField(
        label="Confirmer le mot de passe",
        strip=False,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control password-field',
            'placeholder': '••••••••',
            'autocomplete': 'new-password',
            'data-toggle': 'password'
        }),
        help_text="Confirmez le mot de passe.",
    )

    
    class Meta:
        model = CustomUser
        fields = [
            'username', 'email', 'first_name', 'last_name', 'role', 
            'is_active', 'is_staff', 'is_superuser'
        ]
        help_texts = {
            'username': "Entrez un nom d'utilisateur unique.",
            'email': "Entrez une adresse email valide.",
        }
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Entrez un nom d'utilisateur unique",
                'autocomplete': 'username',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'exemple@domaine.com',
                'autocomplete': 'email',
            }),
            'first_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Prénom',
                'autocomplete': 'given-name',
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nom',
                'autocomplete': 'family-name',
            }),
            'role': forms.Select(attrs={
                'class': 'form-control select-field',
                'data-style': 'btn-dark',
            }),
            'is_active': forms.CheckboxInput(attrs={
                'class': 'form-check-input switch',
                'data-onstyle': 'success',
                'data-offstyle': 'danger',
                'data-toggle': 'toggle',
                'data-size': 'sm',
            }),
            'is_staff': forms.CheckboxInput(attrs={
                'class': 'form-check-input switch',
                'data-onstyle': 'primary',
                'data-offstyle': 'secondary',
                'data-toggle': 'toggle',
                'data-size': 'sm',
            }),
            'is_superuser': forms.CheckboxInput(attrs={
                'class': 'form-check-input switch',
                'data-onstyle': 'warning',
                'data-offstyle': 'dark',
                'data-toggle': 'toggle',
                'data-size': 'sm',
            }),
        }
        labels = {
            'username': "Nom d'utilisateur",
            'email': "Email",
            'first_name': "Prénom",
            'last_name': "Nom",
            'role': "Rôle",
            'is_active': "Compte actif",
            'is_staff': "Accès administration",
            'is_superuser': "Super administrateur",
        }

## formulaire de modification d'un utilisateur

class UtilisateurModificationForm(ModelForm):
    
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'first_name', 'last_name', 'role', 'is_active', 'is_staff', 'is_superuser']
        help_texts = {
            'username': 'Entrez un nom d\'utilisateur unique.',
            'email': 'Entrez une adresse email valide.',
        }
        ## styliser les champs
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'role': forms.Select(attrs={'class': 'form-control'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'is_staff': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'is_superuser': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
        

from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'profile']
        widgets = {
            'bio': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Écrivez votre bio...',
                'rows': 4,
                'style': 'resize: none;'
            }),
            'profile': forms.ClearableFileInput(attrs={
                'class': 'form-control-file',
                'accept': 'image/*',
                'style': 'background-color: rgba(255,255,255,0.1); color: white;'
            }),
        }
        labels = {
            'bio': 'Biographie',
            'profile': 'Photo de profil',
        }


class CompteUtilisateurForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'first_name', 'last_name', 'role']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'role': forms.Select(attrs={'class': 'form-control'}),
        }