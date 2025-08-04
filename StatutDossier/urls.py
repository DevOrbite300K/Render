from django.urls import path
from .views import (
    CreerStatutDossierView,
    ListeStatutDossierView,
    ModifierStatutDossierView,
    SupprimerStatutDossierView,
    DetailStatutDossierView,
)

urlpatterns = [
    path('statutdossier/creer/', CreerStatutDossierView.as_view(), name='creerstatutdossier'),
    path('statutdossier/', ListeStatutDossierView.as_view(), name='statutdossierliste'),
    path('statutdossier/<int:pk>/modifier/', ModifierStatutDossierView.as_view(), name='modifierstatutdossier'),
    path('statutdossier/<int:pk>/supprimer/', SupprimerStatutDossierView.as_view(), name='supprimerstatutdossier'),
    path('statutdossier/<int:pk>/', DetailStatutDossierView.as_view(), name='detailstatutdossier'),
]
