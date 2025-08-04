# logique signals si role == 'client'
from django.dispatch import receiver
from django.db.models.signals import post_save
from cabinet.models import CustomUser

from .models import Client
@receiver(post_save, sender=CustomUser)
def create_client_profile(sender, instance, created, **kwargs):
    if created and instance.role == 'client':
        Client.objects.create(utilisateur=instance)
        
    
