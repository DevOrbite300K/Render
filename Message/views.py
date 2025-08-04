from django.shortcuts import render

from django.urls import reverse_lazy
from django.views.generic import (
    CreateView, ListView, UpdateView, DeleteView, DetailView
)
from .models import Message
from .forms import MessageForm, MessageFormEnvoie
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

class CreerMessageView(CreateView):
    model = Message
    form_class = MessageFormEnvoie
    template_name = 'creermessage.html'
    success_url = reverse_lazy('messageliste')

class ListeMessageView(ListView):
    model = Message
    template_name = 'listmessage.html'
    context_object_name = 'messages'

class ModifierMessageView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Message
    form_class = MessageFormEnvoie
    template_name = 'modifymessage.html'

    def get_success_url(self):
        return reverse_lazy('messageliste')
    
    def test_func(self):
        return self.request.user.is_superuser

class SupprimerMessageView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Message
    template_name = 'supprimermessage.html'
    success_url = reverse_lazy('messageliste')
    
    def test_func(self):
        return self.request.user.is_superuser

class DetailMessageView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Message
    template_name = 'detailmessage.html'
    context_object_name = 'message'
    
    def test_func(self):
        return self.request.user.is_superuser
