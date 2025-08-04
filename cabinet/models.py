from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('avocat', 'Avocat'),
        ('client', 'Client'),
        ('autre', 'Autre'),
        ('expert_metier', 'Expert Metier'),
        ('personnel_administratif', 'Personnel Administratif')
    )
    role = models.CharField(max_length=50, choices=ROLE_CHOICES, default='autre')

    def is_admin(self):
        return self.role == 'admin'

    def is_avocat(self):
        return self.role == 'avocat'

    def is_client(self):
        return self.role == 'client'
    
    def is_autre(self):
        return self.role == 'autre'
    
    def is_expert(self):
        return self.role=='expert_metier'
    
    def is_personnelAdministratif(self):
        return self.role=='personnel_administratif'

    
