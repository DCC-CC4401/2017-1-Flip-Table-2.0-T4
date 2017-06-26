from django.conf.urls import url
from showcase import views
from showcase.views import SellerDetailView, DishCreateView, DishUpdateView, DishDeleteView, FavoriteView

app_name = 'showcase'

urlpatterns = [
    url(r'^(?P<pk>[0-9]+)/$', SellerDetailView.as_view(), name='seller_detail', ),

    # /showcase/<seller_id>/favorite
    url(r'^(?P<pk>[0-9]+)/favorite/$', FavoriteView.as_view(), name='favorite_seller'),

    # /showcase/<seller_id>/dish_create/<dish_id>/
    url(r'^(?P<pk>[0-9]+)/dish_create/$', DishCreateView.as_view(), name='dish_create', ),

    # /showcase/<seller_id>/dish_update/<dish_id>/
    url(r'^(?P<pk>[0-9]+)/dish_update/(?P<dish_id>[0-9]+)/$', DishUpdateView.as_view(), name='dish_update', ),

    # /showcase/<seller_id>/dish_delete/<dish_id>/delete
    url(r'^(?P<pk>[0-9]+)/dish_delete/(?P<dish_id>[0-9]+)$', DishDeleteView.as_view(), name='dish_delete'),

    # /showcase/<seller_id>/checkin
    url(r'^(?P<seller_id>[0-9]+)/check_in/$', views.check_in, name='check_in'),

    url(r'^statistics/$', views.statistics, name='statistics'),

    # /showcase/<seller_id>/favorite
    # url(r'^(?P<seller_id>[0-9]+)/favorite/$', views.favorite_seller, name='favorite_seller'),

]
