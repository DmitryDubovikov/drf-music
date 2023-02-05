from django.shortcuts import render
from rest_framework import generics, viewsets, status
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

    @extend_schema(responses=SingerSerializer)
    def create(self, request):
        serializer = SingerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg": "Data  created"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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
