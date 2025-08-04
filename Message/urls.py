from django.urls import path
from .views import (
    CreerMessageView,
    ListeMessageView,
    ModifierMessageView,
    SupprimerMessageView,
    DetailMessageView,
)

urlpatterns = [
    path('messages/', ListeMessageView.as_view(), name='messageliste'),
    path('messages/nouveau/', CreerMessageView.as_view(), name='creermessage'),
    path('messages/<int:pk>/', DetailMessageView.as_view(), name='detailmessage'),
    path('messages/<int:pk>/modifier/', ModifierMessageView.as_view(), name='modifymessage'),
    path('messages/<int:pk>/supprimer/', SupprimerMessageView.as_view(), name='supprimermessage'),
]
