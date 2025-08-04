from django.urls import path
from .views import (
    CreerPaiementView,
    ListePaiementView,
    ModifierPaiementView,
    SupprimerPaiementView,
    DetailPaiementView,
)
from .views import ImprimerPaiementView




urlpatterns = [
    path('paiements/', ListePaiementView.as_view(), name='paiementliste'),
    path('paiements/nouveau/', CreerPaiementView.as_view(), name='creerpaiement'),
    path('paiements/<int:pk>/', DetailPaiementView.as_view(), name='detailpaiement'),
    path('paiements/<int:pk>/modifier/', ModifierPaiementView.as_view(), name='modifierpaiement'),
    path('paiements/<int:pk>/supprimer/', SupprimerPaiementView.as_view(), name='supprimerpaiement'),
    path('imprimerpaiement/<int:pk>/', ImprimerPaiementView.as_view(), name='imprimerpaiement'),
]
