from django.db import models
from Dossier.models import Dossier
from Client.models import Client
from Avocat.models import Avocat

class RendezVous(models.Model):
    STATUTS = [
        ('prevu', 'Prévu'),
        ('reporte', 'Reporté'),
        ('réalise', 'Réalisé'),
    ]
    objet = models.CharField(max_length=200)
    date_rdv = models.DateField()
    heure_rdv = models.TimeField()
    lieu = models.CharField(max_length=255)
    statut_rdv = models.CharField(max_length=20, choices=STATUTS)
    dossier = models.ForeignKey(Dossier, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True)
    avocat = models.ForeignKey(Avocat, on_delete=models.SET_NULL, null=True)
