from django.db import models
from Dossier.models import Dossier
from Avocat.models import Avocat

# Create your models here.
class DossierAvocat(models.Model):
    ROLES = [
        ('expert_metier', 'Expert métier'),
        ('personnel_administratif', 'Personnel administratif'),
    ]

    dossier = models.ForeignKey(Dossier, on_delete=models.CASCADE)
    avocat = models.ForeignKey(Avocat, on_delete=models.CASCADE)
    rôle_avocat = models.CharField(max_length=30, choices=ROLES)

    def __str__(self):
        return f"{self.avocat} - {self.dossier} ({self.rôle_avocat})"
