from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("artists", views.artists, name="artists"),
]
