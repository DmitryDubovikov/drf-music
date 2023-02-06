from rest_framework import serializers
from .models import Singer, Album, Song, Content


class SingerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Singer
        fields = ["name"]


class AlbumSerializer(serializers.ModelSerializer):
    singer = serializers.PrimaryKeyRelatedField(queryset=Singer.objects.all())

    class Meta:
        model = Album
        fields = ["title", "singer", "year"]


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ["title"]


class ContentSerializer(serializers.ModelSerializer):
    song = serializers.PrimaryKeyRelatedField(queryset=Song.objects.all())
    album = serializers.PrimaryKeyRelatedField(queryset=Album.objects.all())

    class Meta:
        model = Content
        fields = ["song", "track_number", "album"]
