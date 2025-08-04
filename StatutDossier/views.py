from django.shortcuts import render
from django.http import HttpResponse
from .models import StatutDossier
from .forms import StatutDossierForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin




class CreerStatutDossierView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = StatutDossier
    form_class = StatutDossierForm
    template_name = 'creerstatutdossier.html'
    success_url = reverse_lazy('statutdossierliste')

    def test_func(self):
        return self.request.user.is_superuser
    
class ListeStatutDossierView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = StatutDossier
    template_name = 'listestatutdossier.html'
    context_object_name = 'statuts'

    def get_queryset(self):
        return StatutDossier.objects.all()
    
    def test_func(self):
        return self.request.user.is_superuser
    
class ModifierStatutDossierView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = StatutDossier
    form_class = StatutDossierForm
    template_name = 'modifierstatutdossier.html'
    
    def get_success_url(self):
        return reverse_lazy('statutdossierliste')
    
    def test_func(self):
        return self.request.user.is_superuser
    
class SupprimerStatutDossierView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = StatutDossier
    template_name = 'supprimerstatutdossier.html'
    success_url = reverse_lazy('statutdossierliste')
    
    def test_func(self):
        return self.request.user.is_superuser
    
class DetailStatutDossierView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = StatutDossier
    template_name = 'detailstatutdossier.html'
    context_object_name = 'statut'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['statut'] = self.object
        return context
    
    def test_func(self):
        return self.request.user.is_superuser
