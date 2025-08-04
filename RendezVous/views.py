from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from .models import RendezVous
from .forms import RendezVousForm  # à créer si nécessaire
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

class CreerRendezVousView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = RendezVous
    form_class = RendezVousForm
    template_name = 'creerrendezvous.html'
    success_url = reverse_lazy('rendezvousliste')
    
    def test_func(self):
        return self.request.user.is_superuser
    

class ListeRendezVousView(LoginRequiredMixin, UserPassesTestMixin,  ListView):
    model = RendezVous
    template_name = 'listerendezvous.html'
    context_object_name = 'rendezvous_list'
    
    def test_func(self):
        return self.request.user.is_superuser

class ModifierRendezVousView(LoginRequiredMixin, UserPassesTestMixin,  UpdateView):
    model = RendezVous
    form_class = RendezVousForm
    template_name = 'modifierrendezvous.html'

    def get_success_url(self):
        return reverse_lazy('rendezvousliste')
    
    def test_func(self):
        return self.request.user.is_superuser

class SupprimerRendezVousView(LoginRequiredMixin, UserPassesTestMixin,  DeleteView):
    model = RendezVous
    template_name = 'supprimerrendezvous.html'
    success_url = reverse_lazy('rendezvousliste')
    
    def test_func(self):
        return self.request.user.is_superuser

class DetailRendezVousView(LoginRequiredMixin, UserPassesTestMixin,  DetailView):
    model = RendezVous
    template_name = 'detailrendezvous.html'
    context_object_name = 'rendezvous'
    
    def test_func(self):
        return self.request.user.is_superuser
