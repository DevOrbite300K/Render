from django.db import models
from Dossier.models import Dossier
from Client.models import Client

class Paiement(models.Model):
    MOYENS = [
        ('espèces', 'Espèces'),
        ('virement', 'Virement bancaire'),
        ('mobile_money', 'Mobile Money'),
    ]
    dossier = models.ForeignKey(Dossier, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True)
    montant = models.DecimalField(max_digits=10, decimal_places=2)
    date_paiement = models.DateTimeField(auto_now_add=True)
    moyen_paiement = models.CharField(max_length=20, choices=MOYENS)
    url_facture = models.URLField(blank=True, null=True)