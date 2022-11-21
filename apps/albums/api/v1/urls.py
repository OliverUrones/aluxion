from django.urls import path, include
from rest_framework.routers import SimpleRouter

from .views import AlbumModelViewSet, TrackListViewSet, AlbumsListViewSet

router_album = SimpleRouter()

router_album.register(r'album', AlbumModelViewSet, basename='album')

urlpatterns = [
    path(r'', include(router_album.get_urls())),
    path(r'album/<str:title>', TrackListViewSet.as_view({'get': 'list'})),
    path(r'albums', AlbumsListViewSet.as_view({'get': 'list'}))
]