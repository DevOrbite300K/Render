from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from .models import Evenement
from .forms import EvenementForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

class CreerEvenementView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Evenement
    form_class = EvenementForm
    template_name = 'creerevenement.html'
    success_url = reverse_lazy('evenementliste')
    
    def test_func(self):
        return self.request.user.is_superuser

class ListeEvenementView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Evenement
    template_name = 'listeevenement.html'
    context_object_name = 'evenements'
    
    def test_func(self):
        return self.request.user.is_superuser

class ModifierEvenementView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Evenement
    form_class = EvenementForm
    template_name = 'modifierevenement.html'

    def get_success_url(self):
        return reverse_lazy('evenementliste')
    
    def test_func(self):
        return self.request.user.is_superuser

class SupprimerEvenementView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Evenement
    template_name = 'supprimerevenement.html'
    success_url = reverse_lazy('evenementliste')
    
    def test_func(self):
        return self.request.user.is_superuser

class DetailEvenementView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Evenement
    template_name = 'detailevenement.html'
    context_object_name = 'evenement'
    
    def test_func(self):
        return self.request.user.is_superuser

