from rest_framework import serializers

from apps.albums.models import Album, Track


class TrackDefaultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = ('name',)

    def to_representation(self, instance):
        return instance.name


class AlbumDefaultSerializer(serializers.ModelSerializer):
    # tracks = serializers.SlugRelatedField(many=True, slug_field='album', read_only=True)
    tracks = TrackDefaultSerializer(many=True, read_only=True)

    class Meta:
        model = Album
        fields = ('title', 'tracks',)


class AlbumAgregatedDataSerializer(serializers.ModelSerializer):
    artist = serializers.SerializerMethodField()
    tracks_number = serializers.SerializerMethodField()

    class Meta:
        model = Album
        fields = ('title', 'artist', 'tracks_number')

    def get_artist(self, obj):
        return obj.artist.name

    def get_tracks_number(self, obj):
        return obj.tracks.all().count()


