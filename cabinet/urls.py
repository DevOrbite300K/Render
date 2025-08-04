from django.urls import path
from . import views
from .views import CreerUtilisateurView
urlpatterns = [
    path("", views.CustomLoginView.as_view(), name='connexion'),
    path("dash/", views.DashView.as_view(), name='dash'),
    path("deconnexion/", views.deconnexion, name="deconnexion"),
    path("modifierutilisateur/", views.ModifierUtilisateurView.as_view(), name="modifierutilisateur"),
    path("avocatdash/", views.AvocatDashboardView.as_view(), name="avocatdash"),
    path("clientdash/", views.ClientDashboardView.as_view(), name="clientdash"),
    #path("client/", views.client, name="client"),
    #path("utilisateur/", views.CreerUtilisateurView.as_view(), name="utilisateur")
    
    
]
