from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Document
from .forms import DocumentForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

class DocumentListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Document
    template_name = 'documentlist.html'
    context_object_name = 'documents'
    
    def test_func(self):
        return self.request.user.is_superuser

class DocumentDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Document
    template_name = 'documentdetail.html'
    context_object_name = 'document'
    
    def test_func(self):
        return self.request.user.is_superuser

class DocumentCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Document
    form_class = DocumentForm
    template_name = 'documentform.html'
    success_url = reverse_lazy('documentlist')
    
    def test_func(self):
        return self.request.user.is_superuser

class DocumentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Document
    form_class = DocumentForm
    template_name = 'documentform.html'
    success_url = reverse_lazy('documentlist')
    
    def test_func(self):
        return self.request.user.is_superuser

class DocumentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Document
    template_name = 'confirmDoc.html'
    success_url = reverse_lazy('documentlist')
    
    def test_func(self):
        return self.request.user.is_superuser
    
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        
        context['document'] = self.get_object()
        return context
