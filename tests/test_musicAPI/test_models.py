import pytest

pytestmark = pytest.mark.django_db


class TestSingerModel:
    def test_str_method(self, singer_factory):
        obj = singer_factory(name="test_singer")
        assert obj.__str__() == "test_singer"


class TestSongModel:
    def test_str_method(self, song_factory):
        obj = song_factory()
        assert obj.__str__() == "test_song"


class TestAlbumModel:
    def test_str_method(self, album_factory):
        obj = album_factory()
        assert obj.__str__() == "test_album (test_singer, 2019)"
