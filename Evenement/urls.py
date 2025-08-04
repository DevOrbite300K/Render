from django.urls import path
from .views import (
    CreerEvenementView,
    ListeEvenementView,
    ModifierEvenementView,
    SupprimerEvenementView,
    DetailEvenementView,
)

urlpatterns = [
    path('evenements/', ListeEvenementView.as_view(), name='evenementliste'),
    path('evenements/nouveau/', CreerEvenementView.as_view(), name='creerevenement'),
    path('evenements/<int:pk>/', DetailEvenementView.as_view(), name='detailevenement'),
    path('evenements/<int:pk>/modifier/', ModifierEvenementView.as_view(), name='modifierevenement'),
    path('evenements/<int:pk>/supprimer/', SupprimerEvenementView.as_view(), name='supprimerevenement'),
]
