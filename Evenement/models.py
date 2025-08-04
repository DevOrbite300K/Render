from django.db import models
from Dossier.models import Dossier
from cabinet.models import CustomUser

# Create your models here.
class Evenement(models.Model):
    TYPES = [
        ('audience', 'Audience'),
        ('convocation', 'Convocation'),
        ('réunion', 'Réunion'),
        ('autre', 'Autre'),
    ]
    titre = models.CharField(max_length=200)
    description = models.TextField()
    date_evenement = models.DateTimeField()
    type_evenement = models.CharField(max_length=20, choices=TYPES)
    dossier = models.ForeignKey(Dossier, on_delete=models.CASCADE)
    utilisateur = models.ForeignKey(CustomUser, on_delete=models.CASCADE)