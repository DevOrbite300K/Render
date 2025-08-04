from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView
from .models import Avocat
from cabinet.models import CustomUser
from .forms import CustomUserCreationFormAvocat  # formulaire ModelForm à créer
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.edit import UpdateView
from django.http import HttpResponseForbidden
from .forms import AvocatForm  # Assurez-vous d'avoir créé ce formulaire
from Document.models import Document

class AvocatCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = CustomUser  
    form_class = CustomUserCreationFormAvocat
    template_name = 'formAvocat.html'
    success_url = reverse_lazy('dash')  # redirige vers la liste après création
    
    def test_func(self):
        user = self.request.user
        # Permet l'accès si superuser ou role == 'admin'
        return user.is_superuser or getattr(user, 'role', None) == 'admin'

    
    
    


class AvocatListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Avocat
    template_name = 'listeAvocat.html'
    context_object_name = 'avocats'  
    
    def test_func(self):
        user = self.request.user
        # Permet l'accès si superuser ou role == 'admin'
        return user.is_superuser or getattr(user, 'role', None) == 'admin'

    

class AvocatDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Avocat
    template_name = 'detailAvocat.html'
    context_object_name = 'avocat'
    
    def test_func(self):
        user = self.request.user
        # Permet l'accès si superuser ou role == 'admin'
        return user.is_superuser or getattr(user, 'role', None) == 'admin'
    

class AvocatUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Avocat
    form_class = AvocatForm
    template_name = 'modifieAvocat.html'
    success_url = reverse_lazy('listeavocat')  # page de retour après modification
    
    # def test_func(self):
    #     user = self.request.user
    #     # Permet l'accès si superuser ou role == 'admin'
    #     return user.is_superuser or getattr(user, 'role', None) == 'admin'

    # def handle_no_permission(self):
    #     return HttpResponseForbidden("Vous n'avez pas accès à cette page.")
    
    def test_func(self):
        return self.request.user.is_superuser or getattr(self.request.user, 'role', None) == 'admin'
    

class AvocatDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Avocat
    template_name = 'confirmSuppressionAvocat.html'
    success_url = reverse_lazy('listeavocat')  # page de retour après suppression

    def test_func(self):
        user = self.request.user
        # Permet l'accès si superuser ou role == 'admin'
        return user.is_superuser or getattr(user, 'role', None) == 'admin'

    def handle_no_permission(self):
        return HttpResponseForbidden("Vous n'avez pas accès à cette page.")
    
    
    
    





### les access restreint a avocat specifique

from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404
from Dossier.models import Dossier
from Avocat.models import Avocat
from Message.models import Message
from cabinet.models import CustomUser

# 📁 Liste des dossiers liés à l’avocat
class AvocatDossierListView(LoginRequiredMixin, ListView):
    model = Dossier
    template_name = 'accessAvocat/dossierlisteavocat.html'
    context_object_name = 'dossiers'

    def get_queryset(self):
        if not self.request.user.is_avocat() and not self.request.user.is_expert() and not self.request.user.is_personnelAdministratif():
            return Dossier.objects.none()
        avocat = get_object_or_404(Avocat, utilisateur=self.request.user)
        return Dossier.objects.filter(avocats=avocat)

# 📄 Détail d’un dossier + messages
class AvocatDossierDetailView(LoginRequiredMixin, DetailView):
    model = Dossier
    template_name = 'accessAvocat/dossierdetail.html'
    context_object_name = 'dossier'

    def get_object(self, queryset=None):
        dossier = super().get_object(queryset)
        avocat = get_object_or_404(Avocat, utilisateur=self.request.user)
        if dossier.avocats.filter(id=avocat.id).exists():
            return dossier
        raise HttpResponseForbidden("Accès refusé à ce dossier.")
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        dossier = context['dossier']
        context['messages'] = dossier.messages.all()
        context['documents'] = Document.objects.filter(dossier=dossier).order_by('-date_ajout')
        return context


    
    

# ✉️ Ajout de commentaire par l’avocat
class AvocatCommentCreateView(LoginRequiredMixin, CreateView):
    model = Message
    fields = ['message', 'dossier']
    template_name = 'accessAvocat/messageAvocat.html'
    success_url = reverse_lazy('mesdossiers')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_avocat() and not request.user.is_expert() and not request.user.is_personnelAdministratif():
            return HttpResponseForbidden("Action non autorisée.")
        return super().dispatch(request, *args, **kwargs)

    def get_form(self, form_class=None):
        form = super().get_form(form_class)

        # 🧠 Limiter les dossiers auxquels l'avocat est réellement associé
        try:
            avocat = Avocat.objects.get(utilisateur=self.request.user)
            form.fields['dossier'].queryset = Dossier.objects.filter(avocats=avocat)
        except Avocat.DoesNotExist:
            form.fields['dossier'].queryset = Dossier.objects.none()

        return form

    def form_valid(self, form):
        dossier = form.cleaned_data['dossier']
        avocat = get_object_or_404(Avocat, utilisateur=self.request.user)

        # 🔒 Vérification supplémentaire côté sécurité
        if not dossier.avocats.filter(id=avocat.id).exists():
            return HttpResponseForbidden("Ce dossier ne vous concerne pas.")
        
        form.instance.utilisateur = self.request.user
        return super().form_valid(form)


    
    

#### je peux modifier mon profile    

from django.views.generic.edit import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.http import HttpResponseForbidden
from django.urls import reverse_lazy
from .models import Avocat
from .forms import AvocatUpdateForm


class AvocatProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = Avocat
    form_class = AvocatUpdateForm
    template_name = 'accessAvocat/modifierprofileavocat.html'
    success_url = reverse_lazy('mesdossiers')

    def get_object(self, queryset=None):
        return get_object_or_404(Avocat, utilisateur=self.request.user)

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_avocat() and not request.user.is_expert() and not request.user.is_personnelAdministratif():
            return HttpResponseForbidden("Accès refusé.")
        return super().dispatch(request, *args, **kwargs)



### je peux modifier 


from django.contrib.auth import get_user_model
from django.views.generic.edit import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.http import HttpResponseForbidden
from django.urls import reverse_lazy

from cabinet.models import CustomUser

User = get_user_model()

class AvocatCompteUpdateView(LoginRequiredMixin, UpdateView):
    model = CustomUser
    fields = ['first_name', 'last_name', 'email']
    template_name = 'accessAvocat/modifiercompteavocat.html'
    success_url = reverse_lazy('mesdossiers')

    def get_object(self, queryset=None):
        return get_object_or_404(User, pk=self.request.user.pk)

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_avocat() and not request.user.is_expert() and not request.user.is_personnelAdministratif():
            return HttpResponseForbidden("Accès refusé.")
        return super().dispatch(request, *args, **kwargs)






### l'avocat peut televerser un document apres travail

from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.http import HttpResponseForbidden
from django.urls import reverse_lazy

from Document.forms import DocumentForm, DocumentUploadForm

class AvocatDocumentCreateView(LoginRequiredMixin, CreateView):
    model = Document
    form_class = DocumentUploadForm
    template_name = 'accessAvocat/ajoutdocument.html'
    success_url = reverse_lazy('mesdossiers')

    def form_valid(self, form):
        if not self.request.user.is_avocat() and not self.request.user.is_expert() and not self.request.user.is_personnelAdministratif():
            return HttpResponseForbidden("Action non autorisée.")
        
        dossier = form.cleaned_data['dossier']
        avocat = get_object_or_404(Avocat, utilisateur=self.request.user)

        if not dossier.avocats.filter(id=avocat.id).exists():
            return HttpResponseForbidden("Ce dossier ne vous concerne pas.")
        
        form.instance.utilisateur = self.request.user
        return super().form_valid(form)
    
    def get_initial(self):
        initial = super().get_initial()
        dossier_id = self.request.GET.get('dossier')
        if dossier_id:
            initial['dossier'] = dossier_id
        return initial





from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.http import HttpResponseForbidden
from .models import Avocat

class ProfilAvocatView(LoginRequiredMixin, TemplateView):
    template_name = 'accessAvocat/profileavocat.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        if not self.request.user.is_avocat() and not self.request.user.is_expert() and not self.request.user.is_personnelAdministratif():
            raise HttpResponseForbidden("Accès refusé")
        
        avocat = get_object_or_404(Avocat, utilisateur=self.request.user)
        context['avocat'] = avocat
        return context
