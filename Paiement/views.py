from django.shortcuts import render

from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from .models import Paiement
from .forms import PaiementForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

class CreerPaiementView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Paiement
    form_class = PaiementForm
    template_name = 'creerpaiement.html'
    success_url = reverse_lazy('paiementliste')
    
    def test_func(self):
        return self.request.user.is_superuser

class ListePaiementView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Paiement
    template_name = 'listpaiement.html'
    context_object_name = 'paiements'
    
    def test_func(self):
        return self.request.user.is_superuser

class ModifierPaiementView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Paiement
    form_class = PaiementForm
    template_name = 'modifierpaiement.html'

    def get_success_url(self):
        return reverse_lazy('paiementliste')
    
    def test_func(self):
        return self.request.user.is_superuser

class SupprimerPaiementView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Paiement
    template_name = 'supprimerpaiement.html'
    success_url = reverse_lazy('paiementliste')
    
    def test_func(self):
        return self.request.user.is_superuser

class DetailPaiementView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Paiement
    template_name = 'detailpaiement.html'
    context_object_name = 'paiement'
    
    def test_func(self):
        return self.request.user.is_superuser



from django.http import HttpResponse
from django.template.loader import get_template
from django.views import View
from xhtml2pdf import pisa
from .models import Paiement

class ImprimerPaiementView(View):
    def get(self, request, pk):
        paiement = Paiement.objects.get(pk=pk)
        template_path = 'imprimerpaiement.html'
        context = {'paiement': paiement}
        
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = f'filename="paiement_{paiement.id}.pdf"'

        template = get_template(template_path)
        html = template.render(context)

        pisa_status = pisa.CreatePDF(html, dest=response)
        
        if pisa_status.err:
            return HttpResponse('Erreur lors de la génération du PDF.')

        return response
