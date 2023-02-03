from django.shortcuts import render
from rest_framework import generics
from .models import Singer, Album, Song, Content
from .serializers import (
    SingerSerializer,
    AlbumSerializer,
    SongSerializer,
    ContentSerializer,
)

# Create your views here.


class SingersView(generics.ListCreateAPIView):
    queryset = Singer.objects.all()
    serializer_class = SingerSerializer


class SingleSingerView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Singer.objects.all()
    serializer_class = SingerSerializer


class AlbumsView(generics.ListCreateAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer


class SingleAlbumView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer


class SongsView(generics.ListCreateAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer


class SingleSongView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Song.objects.all()
    serializer_class = SongSerializer


class ContentView(generics.ListCreateAPIView):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
