from rest_framework import serializers

from apps.musicians.models import Artist
from apps.albums.models import Album


class ArtistDefaultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = ('name',)

    def to_representation(self, instance):
        return instance.name


class AlbumArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ('title',)

    def to_representation(self, instance):
        return instance.title