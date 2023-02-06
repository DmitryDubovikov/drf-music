from django.shortcuts import render
from rest_framework import generics, viewsets, status
from rest_framework.response import Response
from .models import Singer, Album, Song, Content
from .serializers import (
    SingerSerializer,
    AlbumSerializer,
    SongSerializer,
    ContentSerializer,
)

# Create your views here.


class SingersViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for getting all singers.
    """

    queryset = Singer.objects.all()
    serializer_class = SingerSerializer


class AlbumsViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for getting all albums.
    """

    queryset = Album.objects.all()
    serializer_class = AlbumSerializer


class SongsViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for getting all songs.
    """

    queryset = Song.objects.all()
    serializer_class = SongSerializer


class ContentViewSet(viewsets.ModelViewSet):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
