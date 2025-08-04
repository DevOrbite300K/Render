from django.urls import path
from .views import (
    UtilisateurListView,
    UtilisateurDetailView,
    UtilisateurCreateView,
    UtilisateurUpdateView,
    UtilisateurDeleteView
)



from .views import ModifierProfilView, MonProfilView

urlpatterns = [
    path('utilisateurs/', UtilisateurListView.as_view(), name='listeUtilisateur'),
    path('utilisateur/<int:pk>/', UtilisateurDetailView.as_view(), name='detailUtilisateur'),
    path('utilisateur/ajouter/', UtilisateurCreateView.as_view(), name='creationUtilisateur'),
    path('utilisateur/<int:pk>/modifier/', UtilisateurUpdateView.as_view(), name='modificationUtilisateur'),
    path('utilisateur/<int:pk>/supprimer/', UtilisateurDeleteView.as_view(), name='suppressionUtilisateur'),
    path('profil/', ModifierProfilView.as_view(), name='modifiermonProfil'),
    path('monprofil/', MonProfilView.as_view(), name='monProfil'),
]

