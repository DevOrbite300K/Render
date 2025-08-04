from django.urls import path
from .views import (
    CreerDossierAvocatView,
    ListeDossierAvocatView,
    ModifierDossierAvocatView,
    SupprimerDossierAvocatView,
    DetailDossierAvocatView,
)

urlpatterns = [
    path('dossieravocat/creer/', CreerDossierAvocatView.as_view(), name='creerdossieravocat'),
    path('dossieravocat/', ListeDossierAvocatView.as_view(), name='dossieravocatliste'),
    path('dossieravocat/<int:pk>/modifier/', ModifierDossierAvocatView.as_view(), name='modifierdossieravocat'),
    path('dossieravocat/<int:pk>/supprimer/', SupprimerDossierAvocatView.as_view(), name='supprimerdossieravocat'),
    path('dossieravocat/<int:pk>/', DetailDossierAvocatView.as_view(), name='detaildossieravocat'),
]
