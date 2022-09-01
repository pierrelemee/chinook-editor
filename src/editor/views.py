# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from editor.models import Artist


def index(request):
    return render(request, "index.html")


def artists(request):
    return render(request, "artists.html", context={'artists': Artist.objects.all()})
