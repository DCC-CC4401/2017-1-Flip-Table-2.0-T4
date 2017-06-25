from django.conf.urls import url
from showcase import views
from showcase.views import SellerDetailView

app_name = 'showcase'

urlpatterns = [
    url(r'^(?P<pk>[0-9]+)/$', SellerDetailView.as_view(), name='seller_detail', ),
    url(r'^statistics/$', views.statistics, name='statistics'),

    # /showcase/<seller_id>/favorite
    # url(r'^(?P<seller_id>[0-9]+)/favorite/$', views.favorite_seller, name='favorite_seller'),

]
