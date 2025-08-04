from django.db.models.signals import post_save
from django.dispatch import receiver
from cabinet.models import CustomUser
from .models import Avocat

@receiver(post_save, sender=CustomUser)
def creer_avocat_automatiquement(sender, instance, created, **kwargs):
    if created and instance.role in ['expert_metier', 'personnel_administratif']:
        Avocat.objects.get_or_create(utilisateur=instance)

