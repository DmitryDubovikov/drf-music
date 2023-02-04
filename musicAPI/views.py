from django.shortcuts import render
from rest_framework import generics, viewsets
from rest_framework.response import Response
from drf_spectacular.utils import extend_schema
from .models import Singer, Album, Song, Content
from .serializers import (
    SingerSerializer,
    AlbumSerializer,
    SongSerializer,
    ContentSerializer,
)

# Create your views here.


class SingersViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for getting all singers.
    """

    queryset = Singer.objects.all()

    @extend_schema(responses=SingerSerializer)
    def list(self, request):
        serializer = SingerSerializer(self.queryset, many=True)
        return Response(serializer.data)


class AlbumsViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for getting all albums.
    """

    queryset = Album.objects.all()

    @extend_schema(responses=AlbumSerializer)
    def list(self, request):
        serializer = AlbumSerializer(self.queryset, many=True)
        return Response(serializer.data)


class SongsViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for getting all songs.
    """

    queryset = Song.objects.all()

    @extend_schema(responses=SongSerializer)
    def list(self, request):
        serializer = SongSerializer(self.queryset, many=True)
        return Response(serializer.data)


class ContentView(generics.ListCreateAPIView):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
