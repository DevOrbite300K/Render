from django.urls import path
from .views import (
    DocumentListView, DocumentDetailView,
    DocumentCreateView, DocumentUpdateView, DocumentDeleteView
)

urlpatterns = [
    path('', DocumentListView.as_view(), name='documentlist'),
    path('<int:pk>/', DocumentDetailView.as_view(), name='documentdetail'),
    path('ajouter/', DocumentCreateView.as_view(), name='documentcreer'),
    path('<int:pk>/modifier/', DocumentUpdateView.as_view(), name='documentmodifier'),
    path('<int:pk>/supprimer/', DocumentDeleteView.as_view(), name='documentsupprimer'),
]
