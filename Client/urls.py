from django.urls import path
from .views import (
    ClientListView,
    ClientDetailView,
    ClientCreateView,
    ClientUpdateView,
    ClientDeleteView,
)
from .views import (
    ClientDossierListView,
    ClientDossierDetailView,
    ClientCommentCreateView
)


from .views import ClientProfileUpdateView
from .views import CustomUserUpdateView

from .views import ClientConnecterDetailView


from django.urls import path
from .views import PaiementsClientView, ImprimerPaiementView

urlpatterns = [
    
]


urlpatterns = [
    path('', ClientListView.as_view(), name='listeclient'),
    path('ajouter/', ClientCreateView.as_view(), name='ajouterclient'),
    path('<int:pk>/', ClientDetailView.as_view(), name='detailclient'),
    path('<int:pk>/modifier/', ClientUpdateView.as_view(), name='modifierclient'),
    path('<int:pk>/supprimer/', ClientDeleteView.as_view(), name='supprimerclient'),
    
    ### pour Client
    
    path('dossiers/', ClientDossierListView.as_view(), name='mesdossiersclient'),
    path('dossier/<int:pk>/', ClientDossierDetailView.as_view(), name='dossierdetailclient'),
    path('commentaire/ajouter/', ClientCommentCreateView.as_view(), name='clientcommenter'),
    path('modifier/mon/profil/', ClientProfileUpdateView.as_view(), name='modifierprofileclient'),
    path('modifier/compte/client/', CustomUserUpdateView.as_view(), name='modifiercompteclient'),
    path('mon/profil/', ClientConnecterDetailView.as_view(), name='infosclient'),
    
    
    ## pour ces paiements:
    
    path('mespaiements/', PaiementsClientView.as_view(), name='mespaiements'),
    path('imprimer-paiement/<int:paiement_id>/', ImprimerPaiementView.as_view(), name='imprimerpaiementclient'),
]
