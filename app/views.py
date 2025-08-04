from django.shortcuts import render, redirect
from .forms import ContactForm
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from app.models import Publication, Expert, MembreDirectoire


def BASE(request):
    return render(request,'baseS.html')

# Create your views here.

#=======================vue pour la page d'accueil du site========================================
def INDEX(request):
    publications = Publication.objects.all().order_by('-date_publication')
    recentes1 = Publication.objects.all().order_by('-date_publication')[:3]
    experts = Expert.objects.all()[:4]
    
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save()

            # Envoi d'email
            sujet = f"[SITE MIP] Nouveau message : {contact.sujet}"
            message = f"Nom : {contact.nom}\nEmail : {contact.email}\n\nMessage :\n{contact.message}"
            from_email = settings.DEFAULT_FROM_EMAIL
            to_email = ['roger@mipgroup-expert.com']

            send_mail(sujet, message, from_email, to_email, fail_silently=False)

            messages.success(request, "Votre message a été envoyé avec succès.")
            return redirect('index')
    else:
        form = ContactForm()
    
    return render(request,'includesS/indexS.html', {
        'publications': publications,
        'experts': experts,
        'recentes1': recentes1,
        'form': form})

#======================vue pour la messagerie de contact========================================


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save()

            # Envoi d'email
            sujet = f"[SITE MIP] Nouveau message : {contact.sujet}"
            message = f"Nom : {contact.nom}\nEmail : {contact.email}\n\nMessage :\n{contact.message}"
            from_email = settings.DEFAULT_FROM_EMAIL
            to_email = ['roger@mipgroup-expert.com']

            send_mail(sujet, message, from_email, to_email, fail_silently=False)

            messages.success(request, "Votre message a été envoyé avec succès.")
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request, 'includesS/contactS.html', {'form': form})

#=================================vue pour la page "à propos du site web"==========================================
def ABOUT(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save()

            # Envoi d'email
            sujet = f"[SITE MIP] Nouveau message : {contact.sujet}"
            message = f"Nom : {contact.nom}\nEmail : {contact.email}\n\nMessage :\n{contact.message}"
            from_email = settings.DEFAULT_FROM_EMAIL
            to_email = ['roger@mipgroup-expert.com']

            send_mail(sujet, message, from_email, to_email, fail_silently=False)

            messages.success(request, "Votre message a été envoyé avec succès.")
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request,'includesS/aboutS.html', {'form': form})



#====================vue pour la page d'affichage des membres de la direction et des experts=======================================
def TEAM(request):
    experts = Expert.objects.all()
    membres = MembreDirectoire.objects.all()
    return render(request,'includesS/teamS.html', {
        'experts': experts,
        'membres': membres})
    

#===================vue pour la page de Politique des prix==============================================    
def PDPS(request):
    return render(request,'includesS/PDPS.html')


#====================vue pour la page des services conseil et assistances====================================
def CONSEIL(request):
    return render(request,'includesS/conseilS.html')


#=======================vue pour la page de publication =============================================================
def PUBLICATION(request):
    publications = Publication.objects.all().order_by('-date_publication')
    
    return render(request,'includesS/publicationS.html', {'publications': publications}) 

#=====================vue pour chacune des publications induviduelle========================
def PUBLICATION1(request, pk):
    publication = get_object_or_404(Publication, pk=pk)
    recentes = Publication.objects.all().order_by('-date_publication')[:10]
    
    return render(request,'includesS/publications/pub1.html', {
        'publication': publication, 
        'recentes': recentes})


# ==================Affichage des details de chaque domaines d'intervention ========================================

def CON1(request):
    return render(request, 'includesS/conseils/con1.html')

def CON2(request):
    return render(request, 'includesS/conseils/con2.html')

def CON3(request):
    return render(request, 'includesS/conseils/con3.html')

def CON4(request):
    return render(request, 'includesS/conseils/con4.html')

def CON5(request):
    return render(request, 'includesS/conseils/con5.html')

def CON6(request):
    return render(request, 'includesS/conseils/con6.html')

def CON7(request):
    return render(request, 'includesS/conseils/con7.html')

def CON8(request):
    return render(request, 'includesS/conseils/con8.html')

def CON9(request):
    return render(request, 'includesS/conseils/con9.html')

def CON10(request):
    return render(request, 'includesS/conseils/con10.html')

def CON11(request):
    return render(request, 'includesS/conseils/con11.html')

def CON12(request):
    return render(request, 'includesS/conseils/con12.html')

def CON13(request):
    return render(request, 'includesS/conseils/con13.html')

def CON14(request):
    return render(request, 'includesS/conseils/con14.html')

