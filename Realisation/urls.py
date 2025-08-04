from django.urls import path

from .views import (
    CreerEntrepriseView,
    ListeEntrepriseView,
    ModifierEntrepriseView,
    SupprimerEntrepriseView,
    DetailEntrepriseView,
    
    CreerEtudeView,
    ListeEtudeView,
    ModifierEtudeView,
    SupprimerEtudeView,
    DetailEtudeView,
    
    CreerFormationView,
    ListeFormationView,
    ModifierFormationView,
    SupprimerFormationView,
    DetailFormationView
    
    )


urlpatterns = [
    path('creer-entreprise/', CreerEntrepriseView.as_view(), name='creerentreprise'),
    path('liste-entreprise/', ListeEntrepriseView.as_view(), name='listeentreprise'),
    path('modifier-entreprise/<int:pk>/', ModifierEntrepriseView.as_view(), name='modifierentreprise'),
    path('supprimer-entreprise/<int:pk>/', SupprimerEntrepriseView.as_view(), name='supprimerentreprise'),
    path('detail-entreprise/<int:pk>/', DetailEntrepriseView.as_view(), name='detailentreprise'),
    
    
    
    path('creer-etude/', CreerEtudeView.as_view(), name='creeretude'),
    path('liste-etude/', ListeEtudeView.as_view(), name='listeetude'),
    path('modifier-etude/<int:pk>/', ModifierEtudeView.as_view(), name='modifieretude'),
    path('supprimer-etude/<int:pk>/', SupprimerEtudeView.as_view(), name='supprimeretude'),
    path('detail-etude/<int:pk>/', DetailEtudeView.as_view(), name='detailetude'),
    
    
    
    path('creer-formation/', CreerFormationView.as_view(), name='creerformation'),
    path('liste-formation/', ListeFormationView.as_view(), name='listeformation'),
    path('modifier-formation/<int:pk>/', ModifierFormationView.as_view(), name='modifierformation'),
    path('supprimer-formation/<int:pk>/', SupprimerFormationView.as_view(), name='supprimerformation'),
    path('detail-formation/<int:pk>/', DetailFormationView.as_view(), name='detailformation'),
]
