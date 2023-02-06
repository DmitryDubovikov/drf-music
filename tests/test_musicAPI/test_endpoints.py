import pytest, json

pytestmark = pytest.mark.django_db


class TestSingerEndpoints:
    endpoint = "/api/singer/"

    def test_singer_get(self, singer_factory, api_client):
        singer_factory.create_batch(4)
        response = api_client.get(self.endpoint)
        assert response.status_code == 200
        assert len(json.loads(response.content)) == 4


class TestSongEndpoints:
    endpoint = "/api/song/"

    def test_song_get(self, song_factory, api_client):
        song_factory.create_batch(4)
        response = api_client.get(self.endpoint)
        assert response.status_code == 200
        assert len(json.loads(response.content)) == 4


class TestAlbumEndpoints:
    endpoint = "/api/album/"

    def test_album_get(self, album_factory, api_client):
        album_factory.create_batch(5)
        response = api_client.get(self.endpoint)
        assert response.status_code == 200
        assert len(json.loads(response.content)) == 5
