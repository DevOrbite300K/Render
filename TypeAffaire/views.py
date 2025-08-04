from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from .models import TypeAffaire
from .forms import TypeAffaireForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

class CreerTypeAffaireView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = TypeAffaire
    form_class = TypeAffaireForm
    template_name = 'creertypeaffaire.html'
    success_url = reverse_lazy('typeaffaireliste')
    
    def test_func(self):
        return self.request.user.is_superuser
    
    
class ListeTypeAffaireView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = TypeAffaire
    template_name = 'listetypeaffaire.html'
    context_object_name = 'types'
    
    def test_func(self):
        return self.request.user.is_superuser

class ModifierTypeAffaireView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = TypeAffaire
    form_class = TypeAffaireForm
    template_name = 'modifiertypeaffaire.html'

    def get_success_url(self):
        return reverse_lazy('typeaffaireliste')
    
    def test_func(self):
        return self.request.user.is_superuser

class SupprimerTypeAffaireView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = TypeAffaire
    template_name = 'supprimertypeaffaire.html'
    success_url = reverse_lazy('typeaffaireliste')
    
    def test_func(self):
        return self.request.user.is_superuser

class DetailTypeAffaireView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = TypeAffaire
    template_name = 'detailtypeaffaire.html'
    context_object_name = 'typeaffaire'
    
    def test_func(self):
        return self.request.user.is_superuser
