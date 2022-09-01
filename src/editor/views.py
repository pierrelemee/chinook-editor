from django.core.paginator import Paginator
from django.shortcuts import render
from editor.models import Artist


def index(request):
    return render(request, "index.html")


def artists(request):
    artists = Artist.objects.all()
    paginator = Paginator(artists, 10)

    page = request.GET.get('p')
    results = paginator.get_page(page)

    return render(request, "artists.html", context={'results': results})
