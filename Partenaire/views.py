from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin




def formPartenaire(request):
    return render(request, 'formPartenaire.html')

def listePartenaire(request):
    return render(request, 'listePartenaire.html')