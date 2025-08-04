from django.db import models




class Publication(models.Model):
    titre = models.CharField(max_length=200)
    contenu1 = models.TextField()
    contenu2 = models.TextField()
    date_publication = models.DateTimeField(auto_now_add=True)
    auteur = models.CharField(max_length=100)
    image1 = models.ImageField(upload_to='media/pub', blank=True, null=True)
    image2 = models.ImageField(upload_to='media/pub', blank=True, null=True)

    def __str__(self):
        return self.titre
    
    
class Expert(models.Model):
    nom = models.CharField(max_length=100)
    titre = models.CharField(max_length=100)
    description = models.TextField()
    photo = models.ImageField(upload_to='media/exp')

    def __str__(self):
        return self.nom
    
class MembreDirectoire(models.Model):
    nom = models.CharField(max_length=100)
    fonction = models.CharField(max_length=100)
    biographie = models.TextField()
    photo = models.ImageField(upload_to='media/ekip')

    def __str__(self):
        return self.nom
    
    
class Contact(models.Model):
    nom = models.CharField(max_length=100)
    email = models.EmailField()
    sujet = models.CharField(max_length=150)
    message = models.TextField()
    date_envoi = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nom} - {self.sujet}"
