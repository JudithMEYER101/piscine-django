from django.urls import path
from . import views

urlpatterns = [
    path("init", views.init),
    path("init/", views.init),
    path("populate", views.populate),
    path("populate/", views.populate),
    path("display", views.display),
    path("display/", views.display),
    path("update", views.update),
    path("update/", views.update),
]