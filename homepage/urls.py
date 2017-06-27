from django.conf.urls import url
from homepage import views
from homepage.views import FavoriteFilter

app_name = 'homepage'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<id>[0-9]+)/favs-filter/$', FavoriteFilter.as_view(), name='fav-filter'),
    url(r'^policealert/$', views.police_alert, name='police_alert'),
]
