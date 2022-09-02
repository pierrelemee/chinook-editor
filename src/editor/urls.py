from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("artists", views.artists, name="artists"),
    path("artist/create", views.artist_create, name="artist_create"),
    path("artist/<int:id>/edit", views.artist_edit, name="artist_edit"),
]
