from django.urls import path
from musicAPI import views


urlpatterns = [
    path("singers", views.SingersView.as_view()),
    path("singers/<int:pk>", views.SingleSingerView.as_view()),
    path("albums", views.AlbumsView.as_view()),
    path("albums/<int:pk>", views.SingleAlbumView.as_view()),
    path("songs", views.SongsView.as_view()),
    path("songs/<int:pk>", views.SingleSongView.as_view()),
    path("catalog", views.ContentView.as_view()),
]
