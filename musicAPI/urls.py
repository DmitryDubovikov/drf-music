from django.urls import path, include
from rest_framework.routers import DefaultRouter
from musicAPI import views

router = DefaultRouter()
router.register(r"album", views.AlbumsViewSet)
router.register(r"song", views.SongsViewSet)
router.register(r"singer", views.SingersViewSet)


urlpatterns = [
    path("", include(router.urls)),
    path("content", views.ContentView.as_view()),
]
