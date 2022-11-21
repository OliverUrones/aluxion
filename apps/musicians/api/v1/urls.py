from django.urls import path, include
from django.conf.urls import url
from rest_framework.routers import SimpleRouter

from .views import ArtistModelViewSet, AlbumsArtistViewSet

router_artist = SimpleRouter()

router_artist.register(r'artist', ArtistModelViewSet, basename='artist')

urlpatterns = [
    path(r'', include(router_artist.get_urls())),
    path(r'artist/<str:name>/albums', AlbumsArtistViewSet.as_view({'get': 'list'}))
]