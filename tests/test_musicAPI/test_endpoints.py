import pytest, json

pytestmark = pytest.mark.django_db


class TestSingerEndpoints:
    endpoint = "api/singer"

    def test_singer_get(self, singer_factory, api_client):
        singer_factory.create_batch(4)
        response = api_client(self.endpoint)
        assert response.status_code == 200
        assert len(json.loads(response.content)) == 4


class TestSongEndpoints:
    pass


class TestAlbumEndpoints:
    pass
