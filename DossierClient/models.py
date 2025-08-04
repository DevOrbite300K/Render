from django.db import models
from Dossier.models import Dossier
from Client.models import Client

# Create your models here.
class DossierClient(models.Model):
    ROLES = [
        ('plaignant', 'Plaignant'),
        ('défendeur', 'Défendeur'),
        ('autre', 'Autre'),
    ]
    dossier = models.ForeignKey(Dossier, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    rôle_client = models.CharField(max_length=20, choices=ROLES)
    
