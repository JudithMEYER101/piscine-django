from django.urls import path
from . import views

urlpatterns = [
    path("django", views.django),
    path("django/", views.django),
    path("affichage", views.affichage),
    path("affichage/", views.affichage),
    path("templates", views.templates),
    path("templates/", views.templates),
]