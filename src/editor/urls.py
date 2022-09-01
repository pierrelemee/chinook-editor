from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("artists", views.artists, name="artists"),
    path("artist/create", views.new_artist, name="artist_create"),
]
