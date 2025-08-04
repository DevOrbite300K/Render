from django.urls import path
from . import views
from .views import AvocatDetailView, AvocatUpdateView, AvocatDeleteView, AvocatCreateView

from django.urls import path
from .views import (
    AvocatDossierListView,
    AvocatDossierDetailView,
    AvocatCommentCreateView,
    AvocatCompteUpdateView
)


from .views import AvocatProfileUpdateView

from .views import AvocatDocumentCreateView

from .views import ProfilAvocatView








urlpatterns = [
    path("avocat/", views.AvocatCreateView.as_view(), name="avocat"),
    path("listeavocat/", views.AvocatListView.as_view(), name="listeavocat"),
    
    path('<int:pk>/', AvocatDetailView.as_view(), name='detailavocat'),
    path('<int:pk>/update/', AvocatUpdateView.as_view(), name='modifieavocat'),
    path('<int:pk>/delete/', AvocatDeleteView.as_view(), name='supprimeravocat'),
    
    
    
    ### pour avocat specifique
    
    path('mesdossiers/', AvocatDossierListView.as_view(), name='mesdossiers'),
    path('mesdossiers/<int:pk>/', AvocatDossierDetailView.as_view(), name='avocatdossierdetail'),
    path('commentaire/ajouter/', AvocatCommentCreateView.as_view(), name='avocatcommenter'),
    path('profil/modifier/', AvocatProfileUpdateView.as_view(), name='modifierprofileavocat'),
    path('modifier/compte/avocat', AvocatCompteUpdateView.as_view(), name='modifiercompteavocat'),
    
    
    ## lien de televersement de document:
    path('document/ajouter/', AvocatDocumentCreateView.as_view(), name='ajoutdocumentavocat'),
    
    path('profil/avocat/', ProfilAvocatView.as_view(), name='profileavocat'),

    
]