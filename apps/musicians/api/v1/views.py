from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.status import HTTP_200_OK, HTTP_404_NOT_FOUND
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from apps.musicians.models import Artist
from apps.albums.models import Album
from apps.musicians.api.v1.serializers import ArtistDefaultSerializer, AlbumArtistSerializer


class ArtistModelViewSet(ModelViewSet):
    permission_classes = (AllowAny,)
    permission_classes_by_action = {
        'create': (AllowAny,),
        'retrieve': (AllowAny,),
        'list': (AllowAny,),
        'update': (AllowAny,),
        'partial_update': (AllowAny,),
    }
    serializer_class = ArtistDefaultSerializer
    serializer_action_classes = {
        'create': ArtistDefaultSerializer,
        'retrieve': ArtistDefaultSerializer,
        'list': ArtistDefaultSerializer,
        'update': ArtistDefaultSerializer,
        'partial_update': ArtistDefaultSerializer
    }

    def get_queryset(self):
        if self.action == 'list':
            return Artist.objects.all()

    def get_serializer_class(self):
        return self.serializer_action_classes[self.action]


class AlbumsArtistViewSet(GenericViewSet):
    permission_classes = (AllowAny,)
    permission_classes_by_action = {
        'create': (AllowAny,),
        'retrieve': (AllowAny,),
        'list': (AllowAny,),
        'update': (AllowAny,),
        'partial_update': (AllowAny,),
    }
    serializer_class = AlbumArtistSerializer

    def get_queryset(self):
        if self.action == 'list':
            return Album.objects.filter(artist__name__icontains=self.kwargs.get('name'))

    def list(self, request, name=None):
        query_set = self.get_queryset()
        if query_set:
            serializer = self.get_serializer_class()
            albums = serializer(query_set, many=True)
            return Response(albums.data, status=HTTP_200_OK)
        else:
            return Response({'detail': 'Artist not found'}, status=HTTP_404_NOT_FOUND)