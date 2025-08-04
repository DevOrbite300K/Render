from django.db import models
from django.utils import timezone
from Dossier.models import Dossier
from Client.models import Client
from Avocat.models import Avocat
from cabinet.models import CustomUser

class Message(models.Model):
    dossier = models.ForeignKey(Dossier, on_delete=models.CASCADE, related_name='messages')
    utilisateur = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True, related_name='messages')
    message = models.TextField()
    date_creation = models.DateTimeField(default=timezone.now)
    lu = models.BooleanField(default=False)
    def __str__(self):
        return f"Message de {'Client' if self.client else 'Avocat'} sur {self.dossier.titre}"
