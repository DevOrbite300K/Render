from django import forms
from .models import Dossier
from Avocat.models import Avocat
from DossierAvocat.models import DossierAvocat

from django import forms
from .models import Dossier, Avocat
from DossierAvocat.models import DossierAvocat

# DossierForm (dans forms.py)
from django import forms
from .models import Dossier, Avocat
from DossierAvocat.models import DossierAvocat

from django import forms
from .models import Dossier, Avocat
from DossierAvocat.models import DossierAvocat

class DossierForm(forms.ModelForm):
    avocats = forms.ModelMultipleChoiceField(
        queryset=Avocat.objects.all(),
        required=False,
        widget=forms.SelectMultiple(attrs={
            'class': 'select2',
            'data-placeholder': 'Sélectionner des experts métier'
        }),
        label='Experts métier / Personnel administratif'
    )

    # personnels_admin = forms.ModelMultipleChoiceField(
    #     queryset=Avocat.objects.all(),
    #     required=False,
    #     widget=forms.SelectMultiple(attrs={
    #         'class': 'form-control select2',
    #         'data-placeholder': 'Choisir un ou plusieurs personnels administratifs'
    #     }),
    #     label="Personnels administratifs"
    # )

    class Meta:
        model = Dossier
        fields = [
            'titre', 'description', 'date_ouverture', 'date_cloture',
            'type_affaire', 'statut_actuel', 'clients'
        ]

        widgets = {
            'titre': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'date_ouverture': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'date_cloture': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'type_affaire': forms.Select(attrs={'class': 'form-control'}),
            'statut_actuel': forms.Select(attrs={'class': 'form-control'}),
            'clients': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['avocats'].queryset = Avocat.objects.all()
        # self.fields['personnels_admin'].queryset = Avocat.objects.all()

        # Personnalisation des labels
        self.fields['avocats'].label_from_instance = self.get_label_with_role
        # self.fields['personnels_admin'].label_from_instance = self.get_label_with_role
        
        self.fields['avocats'].widget.attrs.update({
            'class': 'form-control select2',
            'data-placeholder': 'Choisir un ou plusieurs experts métier'
        })
        
        


    def get_label_with_role(self, avocat):
        role = getattr(avocat.utilisateur, 'role', 'Sans rôle')
        role_display = {
            'expert_metier': 'Expert Métier',
            'personnel_administratif': 'Personnel Administratif',
            'avocat': 'Avocat',
            'admin': 'Admin',
            'client': 'Client',
            'autre': 'Autre',
        }
        role_str = role_display.get(role, role.capitalize())
        return f"[{role_str}] {avocat}"

    def save(self, commit=True):
        dossier = super().save(commit=commit)
        DossierAvocat.objects.filter(dossier=dossier).delete()

        for avocat in self.cleaned_data.get('avocats', []):
            DossierAvocat.objects.create(dossier=dossier, avocat=avocat, rôle_avocat='expert')

        # for avocat in self.cleaned_data.get('personnels_admin', []):
        #     DossierAvocat.objects.create(dossier=dossier, avocat=avocat, rôle_avocat='personnel_administratif')

        return dossier
