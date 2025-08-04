from django.db import models
from cabinet.models import CustomUser

SPECIALITES = [
    ('penal', 'Droit pénal'),
    ('civil', 'Droit civil'),
    ('affaires', 'Droit des affaires'),
    ('travail', 'Droit du travail'),
    ('familial', 'Droit de la famille'),
    ('fiscal', 'Droit fiscal'),
    ('international', 'Droit international'),
    ('autre', 'Autre'),
]


class Avocat(models.Model):
    utilisateur = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='avocat_profile')
    specialite = models.CharField(max_length=50, choices=SPECIALITES, default='civil', blank=True, null=True)
    telephone = models.CharField(max_length=20, blank=True, null=True)
    adresse = models.CharField(max_length=255, blank=True, null=True)
    photo= models.ImageField(upload_to='avocat_photos/', blank=True, null=True)
    numero_barreau = models.CharField(max_length=50, blank=True, null=True)
    date_inscription = models.DateField(auto_now_add=True)

    def __str__(self):
        return f" {self.utilisateur.get_full_name() or self.utilisateur.email}"