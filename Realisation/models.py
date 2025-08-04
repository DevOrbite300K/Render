from django.db import models


class EntrepriseCreer(models.Model):
    
    denomination = models.CharField(max_length=100)
    #numeroImmatriculation = models.CharField(max_length=50)
    numeroRCCM= models.CharField(max_length=50)
    numeroNIF = models.CharField(max_length=50)
    siege= models.CharField(max_length=255)
    nomGerant = models.CharField(max_length=100)
    adresseGerant = models.CharField(max_length=255)
    emailGerant = models.EmailField(max_length=254)
    telephoneGerant = models.CharField(max_length=20)
    date_creation = models.DateField()
    documentation = models.FileField(upload_to='documents/', blank=True, null=True)

    def __str__(self):
        return self.denomination
    
    class Meta:
        verbose_name = 'Entreprise Créée'
        verbose_name_plural = 'Entreprises Créées'
        ordering = ['-date_creation']
        unique_together = ('denomination', 'numeroRCCM')
    

class Etude(models.Model):
    
    intitule = models.CharField(max_length=100)
    date_debut = models.DateField()
    date_fin = models.DateField()
    lieu = models.CharField(max_length=255)
    commanditaire = models.CharField(max_length=100)
    document = models.FileField(upload_to='documents/', blank=True, null=True)
    
    def __str__(self):
        return self.intitule
    
    class Meta:
        verbose_name = 'Etude'
        verbose_name_plural = 'Etudes'
        ordering = ['-date_debut']
        unique_together = ('intitule', 'date_debut')
    

class Formation(models.Model):
    
    type_formation=[
        ('certifiante', 'Certifiante'),
        ('atelier', 'Atelier'),
        ('seminaire', 'Séminaire'),
    ]
    
    type = models.CharField(max_length=20, choices=type_formation, default='certifiante')
    theme= models.CharField(max_length=100)
    nombre_participants = models.IntegerField()
    date_debut = models.DateField()
    date_fin = models.DateField()
    lieu = models.CharField(max_length=255)
    document = models.FileField(upload_to='documents/', blank=True, null=True)
    
    
    class Meta:
        verbose_name = 'Formation'
        verbose_name_plural = 'Formations'
        ordering = ['-date_debut']
        unique_together = ('theme', 'date_debut')
    
    def __str__(self):
        return self.theme
    
    
    
    
    


