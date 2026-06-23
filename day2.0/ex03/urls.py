from django.urls import path
from . import views

urlpatterns = [
    path("populate", views.populate),
    path("populate/", views.populate),
    path("display", views.display),
    path("display/", views.display),
]