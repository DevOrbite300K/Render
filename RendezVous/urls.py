from django.urls import path
from .views import (
    CreerRendezVousView,
    ListeRendezVousView,
    ModifierRendezVousView,
    SupprimerRendezVousView,
    DetailRendezVousView,
)

urlpatterns = [
    path('rendezvous/', ListeRendezVousView.as_view(), name='rendezvousliste'),
    path('rendezvous/nouveau/', CreerRendezVousView.as_view(), name='creerrendezvous'),
    path('rendezvous/<int:pk>/', DetailRendezVousView.as_view(), name='detailrendezvous'),
    path('rendezvous/<int:pk>/modifier/', ModifierRendezVousView.as_view(), name='modifierendezvous'),
    path('rendezvous/<int:pk>/supprimer/', SupprimerRendezVousView.as_view(), name='supprimerrendezvous'),
]
