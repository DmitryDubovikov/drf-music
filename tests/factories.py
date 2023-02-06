import factory
from musicAPI.models import Singer, Song, Album, Content


class SingerFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Singer

    name = factory.Sequence(lambda n: f"singer_{n}")


class SongFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Song

    title = "test_song"


class AlbumFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Album

    title = "test_album"
    year = 2019
    singer = factory.SubFactory(SingerFactory)
