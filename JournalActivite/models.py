from django.db import models
from cabinet.models import CustomUser
from Dossier.models import Dossier

class JournalActivite(models.Model):
    ACTIONS = [
        ('ajout', 'Ajout'),
        ('modification', 'Modification'),
        ('suppression', 'Suppression'),
        ('connexion', 'Connexion'),
        ('statut', 'Changement de statut'),
    ]
    utilisateur = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    type_action = models.CharField(max_length=50, choices=ACTIONS)
    date_action = models.DateTimeField(auto_now_add=True)
    détails = models.TextField()
    dossier = models.ForeignKey(Dossier, on_delete=models.SET_NULL, null=True, blank=True)
