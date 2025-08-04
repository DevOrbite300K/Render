from django.urls import path
from . import views

urlpatterns = [
    path("partenaire/", views.formPartenaire, name="partenaire"),
    path("listepartenaire/", views.listePartenaire, name="listepartenaire")
]
