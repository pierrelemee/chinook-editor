from django.contrib.messages import SUCCESS
from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods
from django.contrib import messages

from editor.forms import ArtistForm
from editor.models import Artist


@require_http_methods(["GET"])
def index(request):
    return render(request, "index.html")


@require_http_methods(["GET"])
def artists(request):
    artists = Artist.objects.all()
    paginator = Paginator(artists, 10)

    page = request.GET.get('p')
    results = paginator.get_page(page)

    return render(request, "artists/list.html", context={'results': results})


@require_http_methods(["GET", "POST"])
def artist_edit(request, id):
    artist = get_object_or_404(Artist, id=id)

    if request.method == 'POST':
        form = ArtistForm(request.POST)

        if form.is_valid():
            artist.name = form.data['name']
            artist.save()
            return redirect('artists', permanent=False)

    else:
        form = ArtistForm({'name': artist.name})

    return render(request, 'artists/edit.html', {'form': form})


@require_http_methods(["GET", "POST"])
def artist_create(request):
    if request.method == 'POST':
        form = ArtistForm(request.POST)

        if form.is_valid():
            Artist.objects.create(name=form.data['name'])
            return redirect('artists', permanent=False)

    else:
        form = ArtistForm()

    return render(request, 'artists/edit.html', {'form': form})


@require_http_methods(["POST"])
def artist_delete(request, id):
    artist = get_object_or_404(Artist, id=id)
    artist.delete()
    messages.add_message(request, level=SUCCESS, message=f'Artist "{artist.name}" has been successfully deleted')

    return redirect('artists', permanent=False)
