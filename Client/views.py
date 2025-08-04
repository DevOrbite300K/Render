from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import Client
from .forms import CustomUserCreationFormClient, ClientForm
#from django.shortcuts import render
#from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

class ClientListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Client
    template_name = 'listeClient2.html'
    context_object_name = 'clients'
    paginate_by = 10

    def test_func(self):
        return self.request.user.is_superuser or getattr(self.request.user, 'role', None) == 'admin'
    def handle_no_permission(self):
        return HttpResponseForbidden("Vous n'avez pas accès à cette page.")

class ClientDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Client
    template_name = 'detailClient.html'
    context_object_name = 'client'

    def test_func(self):
        return self.request.user.is_superuser or getattr(self.request.user, 'role', None) == 'admin'

    def handle_no_permission(self):
        return HttpResponseForbidden("Vous n'avez pas accès à cette page.")

class ClientCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Client
    form_class = CustomUserCreationFormClient
    template_name = 'formClient.html'
    success_url = reverse_lazy('listeclient')

    def test_func(self):
        return self.request.user.is_superuser or getattr(self.request.user, 'role', None) == 'admin'
    def handle_no_permission(self):
        return HttpResponseForbidden("Vous n'avez pas accès à cette page.")

class ClientUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Client
    form_class = ClientForm
    template_name = 'modifieClient.html'
    success_url = reverse_lazy('listeclient')

    def test_func(self):
        return self.request.user.is_superuser or getattr(self.request.user, 'role', None) == 'admin'
    def handle_no_permission(self):
        return HttpResponseForbidden("Vous n'avez pas accès à cette page.")


class ClientDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Client
    template_name = 'confirmSuppressionClient.html'
    success_url = reverse_lazy('listeclient')

    def test_func(self):
        return self.request.user.is_superuser or getattr(self.request.user, 'role', None) == 'admin'
    def handle_no_permission(self):
        return HttpResponseForbidden("Vous n'avez pas accès à cette page.")











from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseForbidden
from django.shortcuts import get_object_or_404
from Dossier.models import Dossier
from Message.models import Message  # adapte selon ton app
from Client.models import Client
from cabinet.models import CustomUser

# 📁 Liste des dossiers du client
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Sum
# from .models import Dossier, Client, Paiement

class ClientDossierListView(LoginRequiredMixin, ListView):
    model = Dossier
    template_name = 'accessClient/mesdossiers.html'
    context_object_name = 'dossiers'

    def get_queryset(self):
        if not self.request.user.is_client():
            return Dossier.objects.none()
        try:
            self.client = Client.objects.get(utilisateur=self.request.user)
            return Dossier.objects.filter(clients=self.client)
        except Client.DoesNotExist:
            self.client = None
            return Dossier.objects.none()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        client = getattr(self, 'client', None)

        if client:
            # Récupérer tous les paiements du client
            paiements = Paiement.objects.filter(client=client).select_related('dossier').order_by('-date_paiement')

            # Total des montants payés
            total_montant = paiements.aggregate(total=Sum('montant'))['total'] or 0

            # Total des paiements
            total_paiements = paiements.count()
        else:
            paiements = Paiement.objects.none()
            total_montant = 0
            total_paiements = 0

        context['paiements'] = paiements
        context['total_montant'] = total_montant
        context['total_paiements'] = total_paiements

        return context



# 🔍 Détail d’un dossier + messages
class ClientDossierDetailView(LoginRequiredMixin, DetailView):
    model = Dossier
    template_name = 'accessClient/detaildossier.html'
    context_object_name = 'dossier'

    def get_object(self, queryset=None):
        dossier = super().get_object(queryset)
        client = get_object_or_404(Client, utilisateur=self.request.user)
        if dossier.clients.filter(id=client.id).exists():
            return dossier
        raise HttpResponseForbidden("Accès refusé à ce dossier.")


# ✉️ Ajout de commentaire lié à un dossier
class ClientCommentCreateView(LoginRequiredMixin, CreateView):
    model = Message
    fields = ['message', 'dossier']
    template_name = 'accessClient/messageClient.html'
    success_url = reverse_lazy('mesdossiersclient')

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['message'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Tapez votre commentaire...'
        })
        form.fields['dossier'].widget.attrs.update({
            'class': 'form-select'
        })
        return form

    def form_valid(self, form):
        if not self.request.user.is_client():
            return HttpResponseForbidden("Action non autorisée.")

        dossier = form.cleaned_data['dossier']
        client = get_object_or_404(Client, utilisateur=self.request.user)

        if not dossier.clients.filter(id=client.id).exists():
            return HttpResponseForbidden("Ce dossier ne vous concerne pas.")

        form.instance.utilisateur = self.request.user
        return super().form_valid(form)

    def get_initial(self):
        initial = super().get_initial()
        dossier_id = self.request.GET.get('dossier')
        if dossier_id:
            initial['dossier'] = dossier_id
        return initial


#### modifier les infos du client actuellement connecter:

from django.views.generic.edit import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from .models import Client

class ClientProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = Client
    fields = ['adresse', 'telephone', 'photo', 'datenaissance']
    template_name = 'accessClient/modifierprofileclient.html'
    success_url = reverse_lazy('mesdossiersclient')

    def get_object(self, queryset=None):
        return get_object_or_404(Client, utilisateur=self.request.user)

    def form_valid(self, form):

        return super().form_valid(form)

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['adresse'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Votre adresse'})
        form.fields['telephone'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Votre téléphone'})
        form.fields['photo'].widget.attrs.update({'class': 'form-control'})
        form.fields['datenaissance'].widget.attrs.update({'class': 'form-control'})

        return form








class CustomUserUpdateView(LoginRequiredMixin, UpdateView):
    model = CustomUser
    fields = ['first_name', 'last_name', 'email']
    template_name = 'accessClient/modifiercompteclient.html'
    success_url = reverse_lazy('mesdossiersclient')

    def get_object(self, queryset=None):
        return get_object_or_404(CustomUser, pk=self.request.user.pk)

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['first_name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Prénom'
        })
        form.fields['last_name'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Nom'
        })
        form.fields['email'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Email'
        })

        return form



class ClientConnecterDetailView(LoginRequiredMixin, DetailView):
    model = Client
    template_name = 'accessClient/infosclient.html'
    context_object_name = 'client'

    def get_object(self, queryset=None):
        return get_object_or_404(Client, utilisateur=self.request.user)




### voir les detail d'un dossier

# from django.views.generic import DetailView
# from django.contrib.auth.mixins import LoginRequiredMixin
# from django.http import HttpResponseForbidden
# from django.shortcuts import get_object_or_404
# from .models import Dossier, Client

class DossierDetailView(LoginRequiredMixin, DetailView):
    model = Dossier
    template_name = 'accessClient/dossier_detail.html'
    context_object_name = 'dossier'

    def get_object(self, queryset=None):
        dossier = super().get_object(queryset)
        client = get_object_or_404(Client, utilisateur=self.request.user)
        if not dossier.clients.filter(id=client.id).exists():
            raise HttpResponseForbidden("Vous n'avez pas accès à ce dossier.")
        return dossier



#### le client connecté peut voir ses paiements

from django.views.generic import ListView
from Paiement.models import Paiement

class PaiementsClientView(ListView):
    model = Paiement
    template_name = 'accessClient/paiementsclient.html'
    context_object_name = 'paiements'

    def get_queryset(self):
        user = self.request.user
        return Paiement.objects.filter(client=user.client)




from django.views import View
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from Paiement.models import Paiement


class ImprimerPaiementView(View):
    template_name = 'accessClient/facture.html'

    def get(self, request, paiement_id):
        # Corriger ici : récupération du client lié à l'utilisateur
        client = get_object_or_404(Client, utilisateur=request.user)

        paiement = get_object_or_404(Paiement, id=paiement_id, client=client)
        context = {'paiement': paiement}

        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = f'filename="paiement_{paiement.id}.pdf"'

        template = get_template(self.template_name)
        html = template.render(context)
        pisa_status = pisa.CreatePDF(html, dest=response)

        if pisa_status.err:
            return HttpResponse('Une erreur est survenue lors de la génération du PDF.', status=500)

        return response


