"""
URL configuration for MIPProjet project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('app.urls')),
    path('admin/', admin.site.urls),
    path('cabinet/', include('cabinet.urls')),
    path('client/', include('Client.urls')),
    #path('avocat/', include('Avocat.urls')),
    path('partenaire/', include('Partenaire.urls')),
    path('avocat/', include('Avocat.urls')),
    path('dossier/', include('Dossier.urls')),
    path("document/", include("Document.urls")),
    path('Utilisateur/', include('Utilisateur.urls')),
    path('statutdossier/', include('StatutDossier.urls')),
    path('TypeAffaire/', include('TypeAffaire.urls')),
    path("dossierclient/", include("DossierClient.urls")),
    path("dossieravocat/", include("DossierAvocat.urls")),
    path('evenement/', include('Evenement.urls')),
    path("rendezvous/", include("RendezVous.urls")),
    path("paiement/", include("Paiement.urls")),
    path("message/", include("Message.urls")),
    path("HistoriqueStatut/", include("HistoriqueStatut.urls")),
    path("journalactivite/", include("JournalActivite.urls")),
    path("realisation/", include("Realisation.urls")),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)