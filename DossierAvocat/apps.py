from django.apps import AppConfig


class DossieravocatConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'DossierAvocat'
    
    def ready(self):
        # Import the signals module to ensure the signal handlers are registered
        import DossierAvocat.signals
        # You can also import other modules or perform other initialization tasks here if needed
