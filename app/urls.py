from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    path('', views.INDEX, name='index'),
    
    path('contacts', views.contact_view, name='contact'),
    
    path('abouts', views.ABOUT, name='about'),
    
    path('teams', views.TEAM, name='team'),
    
    path('publicationsS', views.PUBLICATION, name='publications'),
    
    #publication individuel
    path('publication/<int:pk>/', views.PUBLICATION1, name='detail_publication'),
    
    path('Politiques', views.PDPS, name='politique'),
    
    path('conseils', views.CONSEIL, name='conseil'),
    
    # les urls des page de details de chaque domaine d'interventions (conseil & assistance)
    path('conseils/con1', views.CON1, name='conseil1'),
    path('conseils/con2', views.CON2, name='conseil2'),
    path('conseils/con3', views.CON3, name='conseil3'),
    path('conseils/con4', views.CON4, name='conseil4'),
    path('conseils/con5', views.CON5, name='conseil5'),
    path('conseils/con6', views.CON6, name='conseil6'),
    path('conseils/con7', views.CON7, name='conseil7'),
    path('conseils/con8', views.CON8, name='conseil8'),
    path('conseils/con9', views.CON9, name='conseil9'),
    path('conseils/con10', views.CON10, name='conseil10'),
    path('conseils/con11', views.CON11, name='conseil11'),
    path('conseils/con12', views.CON12, name='conseil12'),
    path('conseils/con13', views.CON13, name='conseil13'),
    path('conseils/con14', views.CON14, name='conseil14'),
    
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
