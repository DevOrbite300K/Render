from django.apps import AppConfig


class AvocatConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Avocat'
    
    def ready(self):
        import Avocat.signals  # Assure-toi que le chemin est correct
