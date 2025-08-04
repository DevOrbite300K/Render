from django.urls import path
from .views import (
    CreerDossierClientView,
    ListeDossierClientView,
    ModifierDossierClientView,
    SupprimerDossierClientView,
    DetailDossierClientView,
)

urlpatterns = [
    path('dossierclient/creer/', CreerDossierClientView.as_view(), name='creerdossierclient'),
    path('dossierclient/', ListeDossierClientView.as_view(), name='dossierclientliste'),
    path('dossierclient/<int:pk>/modifier/', ModifierDossierClientView.as_view(), name='modifierdossierclient'),
    path('dossierclient/<int:pk>/supprimer/', SupprimerDossierClientView.as_view(), name='supprimerdossierclient'),
    path('dossierclient/<int:pk>/', DetailDossierClientView.as_view(), name='detaildossierclient'),
]
