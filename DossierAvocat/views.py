from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from .models import DossierAvocat
from .forms import DossierAvocatForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

class CreerDossierAvocatView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = DossierAvocat
    form_class = DossierAvocatForm
    template_name = 'creerdossieravocat.html'
    success_url = reverse_lazy('dossieravocatliste')
    
    def test_func(self):
        return self.request.user.is_superuser

class ListeDossierAvocatView(ListView):
    model = DossierAvocat
    template_name = 'listedossieravocat.html'
    context_object_name = 'dossiersavocats'
    
    def test_func(self):
        return self.request.user.is_superuser

class ModifierDossierAvocatView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = DossierAvocat
    form_class = DossierAvocatForm
    template_name = 'modifierdossieravocat.html'

    def get_success_url(self):
        return reverse_lazy('dossieravocatliste')
    
    def test_func(self):
        return self.request.user.is_superuser

class SupprimerDossierAvocatView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = DossierAvocat
    template_name = 'supprimerdossieravocat.html'
    success_url = reverse_lazy('dossieravocatliste')
    
    def test_func(self):
        return self.request.user.is_superuser

class DetailDossierAvocatView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = DossierAvocat
    template_name = 'detaildossieravocat.html'
    context_object_name = 'dossieravocat'
    
    def test_func(self):
        return self.request.user.is_superuser
    


