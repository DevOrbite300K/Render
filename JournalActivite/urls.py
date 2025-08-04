from django.urls import path
from .views import JournalActiviteListView, JournalActiviteCreateView

urlpatterns = [
    path('journal/', JournalActiviteListView.as_view(), name='journallist'),
    path('journal/nouveau/', JournalActiviteCreateView.as_view(), name='journalcreer'),
]
