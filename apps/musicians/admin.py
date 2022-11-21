from django.contrib import admin

from apps.musicians.models import Artist


class ArtistAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(Artist, ArtistAdmin)
