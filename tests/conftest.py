import pytest
from pytest_factoryboy import register
from rest_framework.test import APIClient
from .factories import SingerFactory, SongFactory, AlbumFactory


register(SingerFactory)
register(SongFactory)
register(AlbumFactory)


@pytest.fixture
def api_client():
    return APIClient()
