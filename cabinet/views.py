from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from cabinet.models import CustomUser
from .forms import UtilisateurForm, ModifierUtilisateurForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView, LogoutView
from .forms import CustomAuthenticationForm
from Dossier.models import Dossier
from Document.models import Document
from Paiement.models import Paiement
from Client.models import Client
from Avocat.models import Avocat
from Message.models import Message
from django.db.models import Count, Sum
from django.db.models.functions import TruncMonth


from datetime import date
# Create your views here.

### la logique de la connexion
class CustomLoginView(LoginView):
    template_name = 'pages/login.html'
    authentication_form = CustomAuthenticationForm
    
    def get_success_url(self):
        user = self.request.user

        if user.is_superuser or getattr(user, 'role', None) == 'admin':
            return reverse_lazy('dash') 
        elif getattr(user, 'role', None) == 'client':
            return reverse_lazy('clientdash')  
        elif getattr(user, 'role', None) == 'avocat':
            return reverse_lazy('avocatdash')
        elif getattr(user, 'role', None) == 'expert_metier':
            return reverse_lazy('avocatdash')
        elif getattr(user, 'role', None) == 'personnel_administratif':
            return reverse_lazy('avocatdash') 
        
        else:
            return reverse_lazy("connexion")  
              



#### affichage de la dashboard
from django.db.models import Count
from django.utils.timezone import now
import json

from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponseForbidden
from django.db.models import Count, Sum
from django.contrib.auth import get_user_model
from django.utils.timezone import now
import json

from Paiement.models import  Paiement
from Utilisateur.models import Profile  # adapte selon ton projet

from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponseForbidden
from django.db.models import Count, Sum
from django.contrib.auth import get_user_model
from django.utils.timezone import now
import json



class DashView(LoginRequiredMixin, UserPassesTestMixin, TemplateView):
    template_name = 'dash/index.html'

    def test_func(self):
        user = self.request.user
        return user.is_superuser or getattr(user, 'role', None) == 'admin'

    def handle_no_permission(self):
        return HttpResponseForbidden("Vous n'avez pas accès à cette page.")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user.username

        # 🔢 Statistiques globales
        context['nb_dossiers'] = Dossier.objects.count()
        context['nb_avocats'] = Avocat.objects.count()
        context['nb_clients'] = Client.objects.count()
        context['nb_documents'] = Document.objects.count()
        context['nb_profils'] = Profile.objects.count()
        context['montant_total'] = Paiement.objects.aggregate(total=Sum('montant'))['total'] or 0

        # 🔍 Fonction pour formatter labels et data
        def extract_chart_data(queryset, label_field):
            labels = [entry[label_field] or 'Non défini' for entry in queryset]
            data = [entry['count'] for entry in queryset]
            return json.dumps(labels), json.dumps(data)

        # 📊 Diagrammes
        avocat_qs = Avocat.objects.values('specialite').annotate(count=Count('id'))
        document_qs = Document.objects.values('type_document').annotate(count=Count('id'))
        paiement_qs = Paiement.objects.values('moyen_paiement').annotate(count=Count('id'))
        client_qs = Client.objects.values('type_client').annotate(count=Count('id'))
        role_qs = get_user_model().objects.values('role').annotate(count=Count('id'))

        context['avocat_labels'], context['avocat_data'] = extract_chart_data(avocat_qs, 'specialite')
        context['document_labels'], context['document_data'] = extract_chart_data(document_qs, 'type_document')
        context['paiement_labels'], context['paiement_data'] = extract_chart_data(paiement_qs, 'moyen_paiement')
        context['client_labels'], context['client_data'] = extract_chart_data(client_qs, 'type_client')
        context['roles_labels'], context['roles_data'] = extract_chart_data(role_qs, 'role')

        # 🕒 Activités récentes
        context['recent_dossiers'] = Dossier.objects.order_by('-date_ouverture')[:5]
        context['recent_avocats'] = Avocat.objects.order_by('-date_inscription')[:5]
        context['recent_clients'] = Client.objects.order_by('-id')[:5]
        context['recent_documents'] = Document.objects.order_by('-date_ajout')[:5]
        context['recent_paiements'] = Paiement.objects.order_by('-date_paiement')[:5]
        context['recent_messages'] = Message.objects.order_by('-date_creation')[:5]

        return context


from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponseForbidden
from django.db.models import Count, Sum, Q
from django.utils import timezone
from datetime import timedelta
import json
from Dossier.models import Dossier
from Document.models import Document
from Message.models import Message
from Paiement.models import Paiement
from .models import CustomUser
from django.db.models.functions import TruncMonth

class ClientDashboardView(LoginRequiredMixin, UserPassesTestMixin, TemplateView):
    template_name = 'pages/clientdash.html'

    def test_func(self):
        user = self.request.user
        try:
            client = CustomUser.objects.get(username=user.username)
            return client.role == 'client'
        except CustomUser.DoesNotExist:
            return False

    def handle_no_permission(self):
        return HttpResponseForbidden("Vous n'avez pas accès à cette page.")
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        client = user.client_profile
        
        # Récupération des messages (utilisés comme notifications)
        messages = Message.objects.filter(
            dossier__clients=client
        ).exclude(
            utilisateur=user  # Exclure les messages de l'utilisateur lui-même
        ).order_by('-date_creation')
        
        unread_messages = messages.filter(lu=False)
        recent_messages = messages[:5]  # 5 derniers messages
        
        # Statistiques de base
        dossiers = client.dossiers.all()
        paiements = Paiement.objects.filter(client=client)
        documents = Document.objects.filter(dossier__clients=client)
        
        now = timezone.now()
        thirty_days_ago = now - timedelta(days=30)
        
        stats = {
            'dossiers_total': dossiers.count(),
            'dossiers_actifs': dossiers.filter(date_cloture__isnull=True).count(),
            'total_paiements': paiements.count(),
            'montant_total': paiements.aggregate(total=Sum('montant'))['total'] or 0,
            'total_documents': documents.count(),
            'documents_30j': documents.filter(date_ajout__gte=thirty_days_ago).count(),
            'total_messages': messages.count(),
            'messages_non_lus': unread_messages.count(),
        }
        
        # Données pour les graphiques (inchangées)
        paiements_par_mois = paiements.annotate(
            mois=TruncMonth('date_paiement')
        ).values('mois').annotate(
            total=Sum('montant')
        ).order_by('mois')[:12]
        
        documents_par_type = documents.values('type_document').annotate(
            total=Count('id')
        ).order_by('type_document')
        
        context.update({
            'client': client,
            'stats': stats,
            'derniers_paiements': paiements.order_by('-date_paiement')[:5],
            'derniers_messages': recent_messages,  # Utilisé pour les notifications
            'unread_messages': unread_messages,    # Notifications non lues
            'mois_paiements': json.dumps([p['mois'].strftime("%b %Y") for p in paiements_par_mois]),
            'montants_paiements': json.dumps([float(p['total']) for p in paiements_par_mois]),
            'types_documents_labels': json.dumps([dict(Document.TYPES).get(t['type_document'], t['type_document']) 
                                    for t in documents_par_type]),
            'types_documents_data': json.dumps([t['total'] for t in documents_par_type]),
            'dossiers_recents': dossiers.order_by('-date_ouverture')[:3],
        })
        
        return context

class AvocatDashboardView(LoginRequiredMixin, UserPassesTestMixin, TemplateView):
    template_name = 'pages/avocatdash.html'

    def test_func(self):
        return self.request.user.role == 'personnel_administratif' or self.request.user.role == 'expert_metier' or self.request.user.role == 'avocat'

    def handle_no_permission(self):
        return HttpResponseForbidden("Vous n'avez pas accès à cette page.")

    def get_context_data(self, **kwargs):
        from django.utils import timezone
        from django.db.models import Count, Sum
        from django.db.models.functions import TruncMonth
        from datetime import timedelta
        import json

        context = super().get_context_data(**kwargs)
        user = self.request.user
        avocat = user.avocat_profile

        # Relation ManyToMany : on filtre les dossiers contenant cet avocat
        dossiers = Dossier.objects.filter(avocats=avocat)

        # Tous les paiements/documents/messages liés à ces dossiers
        paiements = Paiement.objects.filter(dossier__in=dossiers)
        documents = Document.objects.filter(dossier__in=dossiers)
        messages = Message.objects.filter(dossier__in=dossiers).exclude(utilisateur=user).order_by('-date_creation')

        unread_messages = messages.filter(lu=False)
        recent_messages = messages[:5]
        now = timezone.now()
        thirty_days_ago = now - timedelta(days=30)

        stats = {
            'dossiers_total': dossiers.count(),
            'dossiers_actifs': dossiers.filter(date_cloture__isnull=True).count(),
            'total_paiements': paiements.count(),
            'montant_total': paiements.aggregate(total=Sum('montant'))['total'] or 0,
            'total_documents': documents.count(),
            'documents_30j': documents.filter(date_ajout__gte=thirty_days_ago).count(),
            'total_messages': messages.count(),
            'messages_non_lus': unread_messages.count(),
        }

        paiements_par_mois = paiements.annotate(
            mois=TruncMonth('date_paiement')
        ).values('mois').annotate(
            total=Sum('montant')
        ).order_by('mois')[:12]

        documents_par_type = documents.values('type_document').annotate(
            total=Count('id')
        ).order_by('type_document')

        context.update({
            'avocat': avocat,
            'stats': stats,
            'derniers_paiements': paiements.order_by('-date_paiement')[:5],
            'derniers_messages': recent_messages,
            'unread_messages': unread_messages,
            'mois_paiements': json.dumps([p['mois'].strftime("%b %Y") for p in paiements_par_mois]),
            'montants_paiements': json.dumps([float(p['total']) for p in paiements_par_mois]),
            'types_documents_labels': json.dumps([
                dict(Document.TYPES).get(t['type_document'], t['type_document']) for t in documents_par_type
            ]),
            'types_documents_data': json.dumps([t['total'] for t in documents_par_type]),
            'dossiers_recents': dossiers.order_by('-date_ouverture')[:3],
            'today': date.today(),
        })
        

        return context


class CreerUtilisateurView(LoginRequiredMixin, CreateView):
    #model = User
    #form_class = UtilisateurForm
    pass#template_name = 'pages/ajoutclient.html'
    #success_url = reverse_lazy('utilisateur')
    


def deconnexion(request):
    logout(request)
    return redirect('connexion')
    
    
class ModifierUtilisateurView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = CustomUser
    ## pour modifier l'utilisateur actuellement connecter
    form_class = ModifierUtilisateurForm
    template_name = 'pages/modifierutilisateur.html'
    success_url = reverse_lazy('modifierutilisateur')
    
    ## modifier l'utilisateur actuellement connecter
    
    def get_object(self, queryset=None):
        return self.request.user
    
    def test_func(self):
        return self.request.user.is_superuser
    