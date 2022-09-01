from django.conf.urls import url
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from editor.forms import ArtistForm
from editor.models import Artist


def index(request):
    return render(request, "index.html")


def artists(request):
    artists = Artist.objects.all()
    paginator = Paginator(artists, 10)

    page = request.GET.get('p')
    results = paginator.get_page(page)

    return render(request, "artists.html", context={'results': results})


def new_artist(request):
    if request.method == 'POST':
        form = ArtistForm(request.POST)

        if form.is_valid():
            Artist.objects.create(name=form.data['name'])
            return redirect('artists', permanent=False)

    else:
        form = ArtistForm()

    return render(request, 'new_artist.html', {'form': form})
