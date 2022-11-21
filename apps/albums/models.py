from django.db import models

from apps.musicians.models import Artist


class MediaType(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name


class PlayList(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name


class Album(models.Model):
    title = models.CharField(max_length=160)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name='artists')

    def __str__(self):
        return self.title


class Track(models.Model):
    name = models.CharField(max_length=200)
    composer = models.CharField(max_length=220)
    milliseconds = models.IntegerField()
    bytes = models.IntegerField()
    unit_price = models.FloatField(max_length=10)
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='tracks')
    media_type = models.ForeignKey(MediaType, on_delete=models.CASCADE, related_name='media_types')
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, related_name='genres')
    play_list = models.ManyToManyField(PlayList, related_name='playlists')

    def __str__(self):
        return '{0} - {1} - {2}'.format(self.name, self.album.title, self.album.artist.name)
