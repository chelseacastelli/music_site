
from django.shortcuts import render
from .models import Album, Musician, Song

def home(request):
    context = {
        'musicians': Musician.objects.all()
    }
    return render(request, 'home.html', context)

def musician_detail(request, musician_id):
    context = {
        'musician': Musician.objects.get(id=musician_id),
        'albums': Album.objects.filter(artist=musician_id)
    }
    return render(request, 'musician_detail.html', context)


def album_detail(request, album_id):
    context = {
        'album': Album.objects.get(id=album_id),
        'songs': Song.objects.filter(album=album_id)
    }
    return render(request, 'album_detail.html', context)

def song_detail(request, song_id):
    context = {
        'song': Song.objects.get(id=song_id)
    }
    return render(request, 'song_detail.html', context)
