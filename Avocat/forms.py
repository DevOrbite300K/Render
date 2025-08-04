from django import forms
from django.contrib.auth.forms import UserCreationForm
from cabinet.models import CustomUser
from .models import Avocat

class CustomUserCreationFormAvocat(UserCreationForm):
    
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'exemple@email.com'
        })
    )
    first_name = forms.CharField(
        max_length=30,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Votre prénom'
        })
    )
    last_name = forms.CharField(
        max_length=30,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Votre nom'
        })
    )
    
    ROLE_CHOICES = [
        
        ('expert_metier', 'Expert Metier'),
        ('personnel_administratif', 'Personnel Administratif'),
        
    ]
    
    role = forms.ChoiceField(
        choices=ROLE_CHOICES,
        required=True,
        widget=forms.Select(attrs={
            'class': 'form-control bg-dark'
        })
    )
    
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'first_name', 'last_name', 'role', 'password1', 'password2')
        
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nom d\'utilisateur'
            }),
        }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Personnaliser les widgets des mots de passe
        self.fields['password1'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Mot de passe'
        })
        self.fields['password2'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Confirmer le mot de passe'
        })
        
        # Personnaliser les labels
        self.fields['username'].label = 'Nom d\'utilisateur'
        self.fields['email'].label = 'Email'
        self.fields['first_name'].label = 'Prénom'
        self.fields['last_name'].label = 'Nom'
        self.fields['role'].label = 'Rôle'
        self.fields['password1'].label = 'Mot de passe'
        self.fields['password2'].label = 'Confirmer le mot de passe'



class AvocatForm(forms.ModelForm):
    class Meta:
        model = Avocat
        fields = ['specialite', 'telephone', 'adresse', 'photo', 'numero_barreau']
        # stylasation des champs du formulaire
        widgets = {
            'specialite': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Spécialité'
            }),
            'telephone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Téléphone'
            }),
            'adresse': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Adresse'
            }),
            'photo': forms.ClearableFileInput(attrs={
                'class': 'form-control-file'
            }),
            'numero_barreau': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Numero de barreau'
            })
            
        }
        

class AvocatUpdateForm(forms.ModelForm):
    class Meta:
        model = Avocat
        fields = ['telephone', 'adresse', 'photo']
        # stylasation des champs du formulaire
        widgets = {
            'telephone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Téléphone'
            }),
            'adresse': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Adresse'
            }),
            'photo': forms.ClearableFileInput(attrs={
                'class': 'form-control-file'
            })
            
        }