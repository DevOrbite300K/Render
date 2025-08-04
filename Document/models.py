from django.db import models
from Dossier.models import Dossier
from cabinet.models import CustomUser

# Create your models here.
class Document(models.Model):
    TYPES = [
        ('preuve', 'Preuve'),
        ('contrat', 'Contrat'),
        ('autre', 'Autre'),
        ('piece_du_client', 'Pièce du client'),
        ('offre_technique', 'Offre technique'),
        ('offre_financiere', 'Offre financière'),
        ('cv_expert', 'CV Expert'),
        ('profil_cabinet', 'Profil Cabinet'),
        ('fiche_de_paiement', 'Fiche de paiement'),
        ('facture', 'Facture'),
        ('fiche_de_travail', 'Fiche de travail'),
        ('diplome_expert', 'Diplôme Expert'),
        ('attestation_de_bon_fin', 'Attestation de bon fin'),
        ('tdr', 'TDR'),
    ]
    dossier = models.ForeignKey(Dossier, on_delete=models.CASCADE)
    utilisateur = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)
    nom_fichier = models.CharField(max_length=255, default='', null=True, blank=True)
    fichier = models.FileField(upload_to='documents/')
    type_document = models.CharField(max_length=50, choices=TYPES, default='plainte')
    date_ajout = models.DateTimeField(auto_now_add=True)