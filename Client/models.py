from django.db import models
from cabinet.models import CustomUser
from django.contrib.auth.models import User
from django.utils import timezone

TYPE_CLIENT = [
        ('particulier', 'Particulier'),
        ('entreprise', 'Entreprise'),
    ]
class Client(models.Model):
    utilisateur= models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='client_profile', blank=True, null=True)
    adresse = models.CharField(max_length=255, blank=True, null=True)
    telephone = models.CharField(max_length=20, blank=True, null=True)
    photo= models.ImageField(upload_to='client_photos/', blank=True, null=True)
    datenaissance = models.DateField(blank=True, null=True)
    type_client = models.CharField(max_length=25, choices=TYPE_CLIENT, default='particulier', blank=True, null=True)
    #date_inscription = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return f" {self.utilisateur.get_full_name() or self.utilisateur.email}"