from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from cabinet.models import CustomUser
from .forms import UtilisateurCreationForm, UtilisateurModificationForm
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin





class UtilisateurListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = CustomUser
    template_name = 'listeUtilisateur.html'
    context_object_name = 'utilisateurs'

    def test_func(self):
        return self.request.user.is_superuser
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Liste des utilisateurs'
        return context
    
class UtilisateurDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = CustomUser
    template_name = 'detailUtilisateur.html'
    context_object_name = 'user'
    
    def test_func(self):
        return self.request.user.is_superuser
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context['title'] = 'Détails de l\'utilisateur'
        return context
    
class UtilisateurCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = CustomUser
    form_class = UtilisateurCreationForm
    template_name = 'creerUtilisateur.html'
    success_url = reverse_lazy('listeUtilisateur')
    
    def test_func(self):
        return self.request.user.is_superuser
    def form_valid(self, form):
        messages.success(self.request, 'Utilisateur créé avec succès.')
        return super().form_valid(form)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Création d\'un utilisateur'
        return context

class UtilisateurUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = CustomUser
    form_class = UtilisateurModificationForm
    template_name = 'modifieUtilisateur.html'
    success_url = reverse_lazy('listeUtilisateur')
    def test_func(self):
        return self.request.user.is_superuser
    def form_valid(self, form):
        messages.success(self.request, 'Utilisateur modifié avec succès.')
        return super().form_valid(form)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Modification de l\'utilisateur'
        return context
class UtilisateurDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = CustomUser
    template_name = 'confirmSuppressionUtilisateur.html'
    success_url = reverse_lazy('listeUtilisateur')
    def test_func(self):
        return self.request.user.is_superuser
    def form_valid(self, form):
        messages.success(self.request, 'Utilisateur supprimé avec succès.')
        return super().form_valid(form)
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Suppression de l\'utilisateur'
        return context
    


from .models import Profile
from .forms import ProfileForm

### l'utilisateur actuellement connecter peut modifier son profil
class ModifierProfilView(LoginRequiredMixin, UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'modifierprofil.html'
    success_url = reverse_lazy('dash')

    def get_object(self, queryset=None):
        return self.request.user.profile

    def form_valid(self, form):
        messages.success(self.request, 'Profil modifié avec succès.')
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Modifier mon profil'
        return context
    

## afficher les details concernant l'utilisateur actuellement connecter
class MonProfilView(LoginRequiredMixin, DetailView):
    model = CustomUser
    template_name = 'monprofil.html'
    context_object_name = 'user'

    def get_object(self, queryset=None):
        return self.request.user

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Mon Profil'
        return context


### Modifier quelque information lié à mon compte
class ModifierUtilisateurCompteView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = CustomUser
    form_class = UtilisateurModificationForm
    template_name = 'modifiermoncompte.html'
    success_url = reverse_lazy('monProfil')

    def get_object(self, queryset=None):
        return self.request.user

    def form_valid(self, form):
        messages.success(self.request, 'Compte modifié avec succès.')
        return super().form_valid(form)

    def test_func(self):
        return self.request.user.is_authenticated