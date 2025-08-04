"""
WSGI config for MIPProjet project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os
from pathlib import Path
from dotenv import load_dotenv  # <--- importe load_dotenv

# Définit la racine du projet
BASE_DIR = Path(__file__).resolve().parent.parent

# Charge le fichier .env depuis la racine du projet
load_dotenv(BASE_DIR / '.env')  # <--- charge le .env ici

# Définit le module de configuration Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MIPProjet.settings')

# Initialise l'application Django
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
