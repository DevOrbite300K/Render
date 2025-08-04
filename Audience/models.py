from django.db import models
from Dossier.models import Dossier
from Avocat.models import Avocat

class Audience(models.Model):
    date = models.DateTimeField()
    lieu = models.CharField(max_length=255)
    dossier = models.ForeignKey(Dossier, on_delete=models.CASCADE, related_name='audiences')
    
    def __str__(self):
        return f"{self.lieu}"
