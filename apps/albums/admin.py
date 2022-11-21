from django.contrib import admin

from apps.albums.models import Album, PlayList, Genre, MediaType, Track


class AlbumAdmin(admin.ModelAdmin):
    list_display = ('title', 'artist')


class PlayListAdmin(admin.ModelAdmin):
    list_display = ('name',)


class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)


class MediaTypeAdmin(admin.ModelAdmin):
    list_display = ('name',)


class TrackAdmin(admin.ModelAdmin):
    list_display = ('name', 'composer', 'milliseconds', 'bytes', 'unit_price', 'get_album_name', 'media_type', 'genre')

    def get_album_name(self, obj):
        return obj.album.title

    get_album_name.short_description = 'Album title'


admin.site.register(Album, AlbumAdmin)
admin.site.register(PlayList, PlayListAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(MediaType, MediaTypeAdmin)
admin.site.register(Track, TrackAdmin)

