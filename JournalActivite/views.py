from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import JournalActivite
from .forms import JournalActiviteForm

class JournalActiviteListView(LoginRequiredMixin, ListView):
    model = JournalActivite
    template_name = 'journalactivitelist.html'
    context_object_name = 'journaux'

    def get_queryset(self):
        return JournalActivite.objects.select_related('utilisateur', 'dossier').order_by('-date_action')


class JournalActiviteCreateView(LoginRequiredMixin, CreateView):
    model = JournalActivite
    form_class = JournalActiviteForm
    template_name = 'journalactiviteform.html'
    success_url = reverse_lazy('journallist')

    def form_valid(self, form):
        form.instance.utilisateur = self.request.user
        return super().form_valid(form)
