from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from .models import DossierAvocat

@receiver(post_save, sender=DossierAvocat)
def send_mail_on_dossier_avocat_create(sender, instance, created, **kwargs):
    if created:
        avocat = instance.avocat
        dossier = instance.dossier
        email = avocat.utilisateur.email  # récupère l'email du user lié à l'avocat

        if email:
            subject = f'Nouvelle affectation au dossier: {dossier.titre}'
            message = (
                f'Bonjour {avocat.utilisateur.get_full_name() or avocat.utilisateur.username},\n\n'
                f'Vous avez été affecté(e) au dossier "{dossier.titre}".\n'
                f'Description : {dossier.description}\n\n'
                f'Merci de consulter votre espace pour plus d\'informations.\n\n'
                'Cordialement,\nL\'équipe'
            )
            send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [email])
            

