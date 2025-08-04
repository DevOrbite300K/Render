from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from .models import DossierClient
from .forms import DossierClientForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

class CreerDossierClientView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = DossierClient
    form_class = DossierClientForm
    template_name = 'creerdossierclient.html'
    success_url = reverse_lazy('dossierclientliste')
    
    def test_func(self):
        return self.request.user.is_superuser

class ListeDossierClientView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = DossierClient
    template_name = 'listedossierclient.html'
    context_object_name = 'dossiersclients'
    
    def test_func(self):
        return self.request.user.is_superuser

class ModifierDossierClientView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = DossierClient
    form_class = DossierClientForm
    template_name = 'modifierdossierclient.html'

    def get_success_url(self):
        return reverse_lazy('dossierclientliste')
    
    def test_func(self):
        return self.request.user.is_superuser

class SupprimerDossierClientView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = DossierClient
    template_name = 'supprimerdossierclient.html'
    success_url = reverse_lazy('dossierclientliste')
    
    def test_func(self):
        return self.request.user.is_superuser

class DetailDossierClientView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = DossierClient
    template_name = 'detaildossierclient.html'
    context_object_name = 'dossierclient'
    
    def test_func(self):
        return self.request.user.is_superuser
