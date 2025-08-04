from django.urls import path
from .views import (
    DossierListView, DossierDetailView, DossierCreateView,
    DossierUpdateView, DossierDeleteView
)

urlpatterns = [
    path('', DossierListView.as_view(), name='dossierlist'),
    path('<int:pk>/', DossierDetailView.as_view(), name='dossierdetail'),
    path('ajouter/', DossierCreateView.as_view(), name='dossiercreer'),
    path('<int:pk>/modifier/', DossierUpdateView.as_view(), name='dossiermodifier'),
    path('<int:pk>/supprimer/', DossierDeleteView.as_view(), name='dossiersupprimer'),
]
