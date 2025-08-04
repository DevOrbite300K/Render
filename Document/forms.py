from django import forms
from .models import Document

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = [
            'dossier',
            'utilisateur',
            'nom_fichier',
            'fichier',
            'type_document',
        ]
        widgets = {
            'dossier': forms.Select(attrs={'class': 'form-control'}),
            'utilisateur': forms.Select(attrs={'class': 'form-control'}),
            'nom_fichier': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Nom du document…'
            }),
            'fichier': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'type_document': forms.Select(attrs={'class': 'form-control'}),
        }
        labels = {
            'nom_fichier': 'Nom du fichier',
            'type_document': 'Type de document',
        }

    def clean_fichier(self):
        fichier = self.cleaned_data.get('fichier')
        if fichier:
            # Taille maximale 5 MB
            max_size = 5 * 1024 * 1024
            if fichier.size > max_size:
                raise forms.ValidationError("La taille du fichier ne doit pas dépasser 5 Mo.")
            # Extensions autorisées
            ext = fichier.name.rsplit('.', 1)[-1].lower()
            valid_exts = ['pdf', 'doc', 'docx', 'jpg', 'jpeg', 'png']
            if ext not in valid_exts:
                raise forms.ValidationError(
                    "Extension non autorisée. Formats autorisés : pdf, doc, docx, jpg, jpeg, png."
                )
        return fichier




class DocumentUploadForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['nom_fichier', 'type_document', 'fichier', 'dossier']  # ✅ pas de 'utilisateur'
        widgets = {
            'nom_fichier': forms.TextInput(attrs={'class': 'form-control'}),
            'type_document': forms.Select(attrs={'class': 'form-select'}),
            'fichier': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'dossier': forms.Select(attrs={'class': 'form-select'}),
        }
