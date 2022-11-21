from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.status import HTTP_200_OK, HTTP_404_NOT_FOUND
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from apps.albums.models import Album, Track
from apps.albums.api.v1.serializers import AlbumDefaultSerializer, TrackDefaultSerializer, AlbumAgregatedDataSerializer


class AlbumModelViewSet(ModelViewSet):
    permission_classes = (AllowAny,)
    permission_classes_by_action = {
        'create': (AllowAny,),
        'retrieve': (AllowAny,),
        'list': (AllowAny,),
        'update': (AllowAny,),
        'partial_update': (AllowAny,),
    }
    serializer_class = AlbumDefaultSerializer
    serializer_action_classes = {
        'create': AlbumDefaultSerializer,
        'retrieve': AlbumDefaultSerializer,
        'list': AlbumDefaultSerializer,
        'update': AlbumDefaultSerializer,
        'partial_update': AlbumDefaultSerializer
    }

    def get_queryset(self):
        if self.action == 'list':
            return Album.objects.all()

    def get_serializer_class(self):
        return self.serializer_action_classes[self.action]

    def list(self, request, *args, **kwargs):
        query_set = self.get_queryset()
        serializer = self.get_serializer_class()
        albums = serializer(query_set, many=True)
        print(albums.data)
        return Response(albums.data, status=HTTP_200_OK)


class TrackListViewSet(GenericViewSet):
    permission_classes = (AllowAny,)
    permission_classes_by_action = {
        'create': (AllowAny,),
        'retrieve': (AllowAny,),
        'list': (AllowAny,),
        'update': (AllowAny,),
        'partial_update': (AllowAny,),
    }
    serializer_class = TrackDefaultSerializer

    def get_queryset(self):
        if self.action == 'list':
            return Track.objects.filter(album__title__iexact=self.kwargs.get('title'))

    def list(self, request, title=None):
        query_set = self.get_queryset()
        if query_set:
            serializer = self.get_serializer_class()
            tracks = serializer(query_set, many=True)
            return Response(tracks.data, status=HTTP_200_OK)
        else:
            return Response({'detail': 'Album not found'}, status=HTTP_404_NOT_FOUND)


class AlbumsListViewSet(GenericViewSet):
    permission_classes = (AllowAny,)
    permission_classes_by_action = {
        'create': (AllowAny,),
        'retrieve': (AllowAny,),
        'list': (AllowAny,),
        'update': (AllowAny,),
        'partial_update': (AllowAny,),
    }
    serializer_class = AlbumAgregatedDataSerializer

    def get_queryset(self):
        if self.action == 'list':
            return Album.objects.all()

    def list(self, request):
        query_set = self.get_queryset()
        if query_set:
            serializer = self.get_serializer_class()
            albums = serializer(query_set, many=True)
            return Response(albums.data, status=HTTP_200_OK)
        else:
            return Response([], status=HTTP_200_OK)

