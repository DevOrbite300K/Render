from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from .models import EntrepriseCreer, Etude, Formation
from .forms import EntrepriseCreerForm, EtudeForm, FormationForm
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin












#### Logique metier pour la gestions des entreprises creer###################################################

class CreerEntrepriseView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = EntrepriseCreer
    form_class = EntrepriseCreerForm
    template_name = 'entreprisecreer/entrepriseforme.html'
    success_url = reverse_lazy('listeentreprise')
    
    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.is_superuser
    
class ListeEntrepriseView(LoginRequiredMixin, UserPassesTestMixin,  ListView):
    model = EntrepriseCreer
    template_name = 'entreprisecreer/listeentreprise.html'
    context_object_name = 'entreprises'
    
    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.is_superuser
    
class ModifierEntrepriseView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = EntrepriseCreer
    form_class = EntrepriseCreerForm
    template_name = 'entreprisecreer/entrepriseforme.html'
    success_url = reverse_lazy('listeentreprise')
    
    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.is_superuser
    
class SupprimerEntrepriseView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = EntrepriseCreer
    template_name = 'entreprisecreer/supprimerentreprise.html'
    success_url = reverse_lazy('listeentreprise')
    
    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.is_superuser
    
class DetailEntrepriseView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = EntrepriseCreer
    template_name = 'entreprisecreer/detailentreprise.html'
    context_object_name = 'entreprise'
    
    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.is_superuser
    
    
    

















###### Logique metier pour la gestions des etudes realisé ######################################################



class CreerEtudeView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Etude
    form_class = EtudeForm
    template_name = 'etude/etudeforme.html'
    success_url = reverse_lazy('listeetude')
    
    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.is_superuser
    
class ListeEtudeView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Etude
    template_name = 'etude/listeetude.html'
    context_object_name = 'etudes'
    
    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.is_superuser
    
class ModifierEtudeView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Etude
    form_class = EtudeForm
    template_name = 'etude/etudeforme.html'
    success_url = reverse_lazy('listeetude')
    
    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.is_superuser
    
class SupprimerEtudeView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Etude
    template_name = 'etude/supprimeretude.html'
    success_url = reverse_lazy('listeetude')
    
    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.is_superuser
    
class DetailEtudeView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Etude
    template_name = 'etude/detailetude.html'
    context_object_name = 'etude'
    
    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.is_superuser




















###### Logique metier pour la gestions des formations realisés ################################################

class CreerFormationView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Formation
    form_class = FormationForm
    template_name = 'formation/formationforme.html'
    success_url = reverse_lazy('listeformation')
    
    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.is_superuser

class ListeFormationView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Formation
    template_name = 'formation/listeformation.html'
    context_object_name = 'formations'
    
    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.is_superuser
    
class ModifierFormationView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Formation
    form_class = FormationForm
    template_name = 'formation/formationforme.html'
    success_url = reverse_lazy('listeformation')
    
    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.is_superuser
    
class SupprimerFormationView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Formation
    template_name = 'formation/supprimerformation.html'
    success_url = reverse_lazy('listeformation')
    
    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.is_superuser
    
class DetailFormationView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Formation
    template_name = 'formation/detailformation.html'
    context_object_name = 'formation'
    
    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.is_superuser