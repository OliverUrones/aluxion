from apps.musicians.api.v1.urls import urlpatterns as musicians_urls
from apps.albums.api.v1.urls import urlpatterns as albums_urls

urlpatterns = []

urls_list = [musicians_urls, albums_urls]

for url in urls_list:
    urlpatterns += url
