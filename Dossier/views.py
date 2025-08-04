from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Dossier
from .forms import DossierForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from datetime import date

class DossierListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Dossier
    template_name = 'dossierlist.html'
    context_object_name = 'dossiers'
    
    def test_func(self):
        return self.request.user.is_superuser
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['today'] = date.today()  # ⬅️ Ajout ici
        return context

class DossierDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Dossier
    template_name = 'dossierdetail.html'
    context_object_name = 'dossier'
    
    def test_func(self):
        return self.request.user.is_superuser

class DossierCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Dossier
    form_class = DossierForm
    template_name = 'dossierform.html'
    success_url = reverse_lazy('dossierlist')
    
    def test_func(self):
        return self.request.user.is_superuser

class DossierUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Dossier
    form_class = DossierForm
    template_name = 'dossierform.html'
    success_url = reverse_lazy('dossierlist')
    
    def test_func(self):
        return self.request.user.is_superuser

class DossierDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Dossier
    template_name = 'confirmSuppressionDossier.html'
    success_url = reverse_lazy('dossierlist')
    
    def test_func(self):
        return self.request.user.is_superuser
