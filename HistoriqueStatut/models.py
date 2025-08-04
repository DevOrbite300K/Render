from django.db import models
from Dossier.models import Dossier
from StatutDossier.models import StatutDossier
from cabinet.models import CustomUser

class HistoriqueStatut(models.Model):
    dossier = models.ForeignKey(Dossier, on_delete=models.CASCADE)
    statut = models.ForeignKey(StatutDossier, on_delete=models.CASCADE)
    date_changement = models.DateTimeField(auto_now_add=True)
    commentaire = models.TextField(blank=True, null=True)
    modifié_par = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)