from django.db import models
from Client.models import Client
from Avocat.models import Avocat
from TypeAffaire.models import TypeAffaire
from StatutDossier.models import StatutDossier

class Dossier(models.Model):
    titre = models.CharField(max_length=255)
    description = models.TextField()
    date_ouverture = models.DateField()
    date_cloture = models.DateField(null=True, blank=True)
    type_affaire = models.ForeignKey(TypeAffaire, on_delete=models.SET_NULL, null=True)
    statut_actuel = models.ForeignKey(StatutDossier, on_delete=models.SET_NULL, null=True)
    clients = models.ManyToManyField(Client, through='DossierClient.DossierClient', related_name='dossiers')
    avocats = models.ManyToManyField(Avocat, through='DossierAvocat.DossierAvocat', related_name='dossiers')
    
    def __str__(self):
        return self.titre
    
    
    
    def has_paiements(self):
        return self.paiement_set.exists()
