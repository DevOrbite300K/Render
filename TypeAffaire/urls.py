from django.urls import path
from .views import (
    CreerTypeAffaireView,
    ListeTypeAffaireView,
    ModifierTypeAffaireView,
    SupprimerTypeAffaireView,
    DetailTypeAffaireView,
)

urlpatterns = [
    path('typeaffaire/creer/', CreerTypeAffaireView.as_view(), name='creertypeaffaire'),
    path('typeaffaire/', ListeTypeAffaireView.as_view(), name='typeaffaireliste'),
    path('typeaffaire/<int:pk>/modifier/', ModifierTypeAffaireView.as_view(), name='modifiertypeaffaire'),
    path('typeaffaire/<int:pk>/supprimer/', SupprimerTypeAffaireView.as_view(), name='supprimertypeaffaire'),
    path('typeaffaire/<int:pk>/', DetailTypeAffaireView.as_view(), name='detailtypeaffaire'),
]
